Title: Perusing Spotify Streaming Data
Date: 2023-08-30 21:35
Category: Writing
Tags: software, sql
Slug:
Authors: Matt Leaverton
Summary:
Status: published

I found how to download my full streaming history from Spotify! Let's dig in to see what is inside.

## Get the Data
Go to the [Spotify account privacy page](https://www.spotify.com/us/account/privacy/){: target=_blank} and scroll to the bottom.
At the time of this writing, there are three request forms available - Account data, Technical log information, and 
Extended streaming history. Check the box under Extended streaming history and click request data. Spotify estimates
30 days until it is ready - they emailed me with a download link a week or two after the request. 

The data package I received has a README PDF and several JSON files covering video (unclear why this exists)
and audio streaming history. My history goes from Sept 24, 2011 
([Mansard Roof](https://open.spotify.com/track/30CU4qvNUUtd8GN4zDV5Oz){: target=_blank} by Vampire Weekend) 
through Aug 24, 2023 in 4 JSON files.

## Explore the Data - Setup
To explore the data, I took the interesting JSON fields and built a schema for SQLite to let me learn
what I wanted to from my data. The following python script loads each JSON file, walks through each streaming
entry to grab the useful fields, then inserts the records into a new SQLite database.

```python
import json
import os
import sqlite3

DATABASE = 'database.db'
pth = r'<somewhere on windows>\my_spotify_data_extended_history\MyData'

files = os.listdir(pth)
# Audio only, please no video data
files = [f for f in files if os.path.splitext(f)[1] == '.json' and 'Audio' in f]

db = sqlite3.connect(DATABASE)
db.row_factory = sqlite3.Row
c = db.cursor()

c.execute('''
CREATE TABLE IF NOT EXISTS song (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    track_name TEXT NOT NULL,
    artist_name TEXT,
    album_name TEXT,
    shuffle INTEGER,
    skipped INTEGER,
    ms_played INTEGER,
    created_at TIMESTAMP UNIQUE
);
''')

for file in files:
    with open(os.path.join(pth, file), 'r', encoding="utf8") as f:
        data = json.load(f)

        for t in data:
            created_at = t['ts']
            ms_played = t['ms_played']
            track_name = t['master_metadata_track_name']
            artist_name = t['master_metadata_album_artist_name']
            album_name = t['master_metadata_album_album_name']
            shuffle = t['shuffle']
            skipped = t['skipped']

            c.execute('INSERT or IGNORE INTO song (created_at, ms_played, track_name, '
                      'artist_name, album_name, shuffle, skipped) ' 
                      'VALUES (?, ?, ?, ?, ?, ?, ?);', 
                      (created_at, ms_played, track_name, artist_name,
                       album_name, shuffle, skipped))

db.commit()
db.close()
```

And with that, we're in. 12 years of audio data at my fingertips.

## Explore the Data - In Earnest

Using the incredible and infinitely useful [DB Browser for SQLite]({filename}db-browser-sqlite.md){: target=_blank},
I have been able to explore the data and find all sorts of fun information.

### Total hours streamed

3929 hours streamed over 12 years - in those 12 years, I have spent 163 full days listening to music on Spotify. 

```sql
SELECT
	COUNT(*),
	printf("%.2f", SUM(ms_played) / 3600000.) AS hours
FROM song
```

### Tracks streamed and total hours listened per year:

Peaked in 2015 with 509, but well on my way in 2023 with 438 already.

```sql
SELECT
	COUNT(*),
	printf("%.2f", SUM(ms_played) / 3600000.) AS hours,
	strftime('%Y', created_at) year
FROM song
GROUP BY year
```

> Thanks to [Designcise](https://www.designcise.com/web/tutorial/how-to-group-by-month-and-year-in-sqlite){: target=_blank}
on how to access the year from timestamps in Sqlite.

### Who is my top artist by streaming time?

[Brian Eno](https://open.spotify.com/artist/7MSUfLeTdDEoZiJPDSBXgi){: target=_blank} for the win with a whopping 949 hours. 
Mr Eno and I have spent well over a month solid together at 40 complete days of music.

```sql
SELECT
	artist_name,
	COUNT(*) as count,
	SUM(ms_played) / 3600000. AS hours
FROM song
GROUP BY
	artist_name
ORDER BY
	hours DESC
```

### Top track from Brian Eno?

[Thursday Afternoon](https://open.spotify.com/album/6AKF0REZoFiXMorWDpSiZt){: target=_blank} with 419 streams
for 674 hours (this is my study/work/chill jam of all time as noted already [here]({filename}../pages/about.md){: target=_blank})

The song is exactly one hour long, so that math does not quite add up. My hypothesis is that this is due to me
restarting the song to near the beginning using the progress slider instead of the track skip buttons, which
must not register as a new stream.

Second place is [Reflection](https://open.spotify.com/track/0YITCj5hDVGfGuL9DguTg8){: target=_blank}
with 162 streams for 244 hours.

```sql
SELECT
	track_name,
	artist_name,
	COUNT(*) as count,
	SUM(ms_played) / 3600000. AS hours
FROM song
WHERE
	artist_name = "Brian Eno"
GROUP BY
	track_name
ORDER BY
	hours DESC
```

### Top 5 artists by stream count

1. [Disasterpeace](https://open.spotify.com/artist/7rSMEcqv4Ez0OLgJKDjrvq){: target=_blank} - **1376**
2. [Brian Eno](https://open.spotify.com/artist/7MSUfLeTdDEoZiJPDSBXgi){: target=_blank} - **1106**
3. [Qumu](https://open.spotify.com/artist/0LzeyDrlLtuyBqMSBN4z3U){: target=_blank} - **946**
4. [Hans Zimmer](https://open.spotify.com/artist/0YC192cP3KPCRWx8zr8MfZ){: target=_blank} - **899**
5. [Big Giant Circles](https://open.spotify.com/artist/6xgUHoQfcHv3MuB9I9z6RO){: target=_blank} - **775**

```sql
SELECT
	artist_name,
	COUNT(*) as count,
	SUM(ms_played) / 3600000. AS hours
FROM song
GROUP BY
	artist_name
ORDER BY
	count DESC
LIMIT 5
```

## Who knows what other goodies await?
I plan to keep digging to see what I can unearth in my listening habits. I hope to rediscover some artists
and albums from my early streaming years that have fallen off my map.

I also want to bring this data online in a searchable, filterable, chartable fashion - brainstorming what 
that would take.

TBD on how long Spotify enforces between requests - maybe I can refresh my data every 6 months or so.