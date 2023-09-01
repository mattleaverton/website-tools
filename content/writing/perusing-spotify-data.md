Title: Perusing Spotify Streaming Data
Date: 2023-08-30 21:35
Category: Writing
Tags: software, sql
Slug:
Authors: Matt Leaverton
Summary:
Status: draft

Go and get your history!

Several days later, Spotify notified me that the data was ready to download. The streaming history
covers from Sept 24, 2011 (Mansard Roof by Vampire Weekend) through Aug 24, 2023. 

```sql
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
```

Using the incredible and infinitely useful [DB Browser for Sqlite]({filename}db-browser-sqlite.md){: target=_blank},
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

### 

> Thanks to [Designcise](https://www.designcise.com/web/tutorial/how-to-group-by-month-and-year-in-sqlite){: target=_blank}
on how to access the year from timestamps in Sqlite.