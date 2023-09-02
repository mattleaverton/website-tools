Title: Fixing Gunicorn Hang
Date: 2023-09-02 21:35
Category: Writing
Tags: software, infra, python
Slug:
Authors: Matt Leaverton
Summary:
Status: draft

I am working on deploying a Flask app in Docker and ran into an issue where the first request would hang.

### The Issue
To launch my `flask` app on `gunicorn` in a Docker container, I have a `boot.sh` file based on Miguel Grinberg's recommendations
in this [Flask tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xix-deployment-on-docker-containers){: target=_blank}

```commandline
#!/bin/bash
source .venv/bin/activate
exec gunicorn -b :8000 --access-logfile - --error-logfile - 'run:get_app()'
```

But I see an issue when I launch using `gunicorn` in Docker and make the first database request:

```commandline
[2023-09-02 19:22:20 +0000] [1] [INFO] Starting gunicorn 21.2.0
[2023-09-02 19:22:20 +0000] [1] [INFO] Listening at: http://0.0.0.0:8000 (1)
[2023-09-02 19:22:20 +0000] [1] [INFO] Using worker: sync
[2023-09-02 19:22:20 +0000] [7] [INFO] Booting worker with pid: 7
172.17.0.1 - - [02/Sep/2023:19:22:33 +0000] "GET / HTTP/1.1" 200 1165 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0"
172.17.0.1 - - [02/Sep/2023:19:22:34 +0000] "GET /static/simple.min.css HTTP/1.1" 200 0 "http://127.0.0.1:8000/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0"
172.17.0.1 - - [02/Sep/2023:19:22:34 +0000] "GET /api/static/style.css HTTP/1.1" 304 0 "http://127.0.0.1:8000/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0"
[2023-09-02 19:23:04 +0000] [1] [CRITICAL] WORKER TIMEOUT (pid:7)
[2023-09-02 19:23:04 +0000] [7] [INFO] Worker exiting (pid: 7)
[2023-09-02 19:23:05 +0000] [1] [ERROR] Worker (pid:7) was sent SIGKILL! Perhaps out of memory?
[2023-09-02 19:23:05 +0000] [9] [INFO] Booting worker with pid: 9
172.17.0.1 - - [02/Sep/2023:19:23:06 +0000] "POST /new HTTP/1.1" 302 189 "http://127.0.0.1:8000/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0"
172.17.0.1 - - [02/Sep/2023:19:23:06 +0000] "GET / HTTP/1.1" 200 1362 "http://127.0.0.1:8000/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0"
172.17.0.1 - - [02/Sep/2023:19:23:45 +0000] "POST /new HTTP/1.1" 302 189 "http://127.0.0.1:8000/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0"
172.17.0.1 - - [02/Sep/2023:19:23:45 +0000] "GET / HTTP/1.1" 200 1556 "http://127.0.0.1:8000/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0"
```

### The Resolution
Thanks to [PythonSpeed.com](https://pythonspeed.com/articles/gunicorn-in-docker/){: target=_blank} for
the solutions. 

Changing the work directory:

`--worker-tmp-dir /dev/shm ...`


And updating the number of threads and workers (I changed the number of threads from the recommended 4
down to 2 as `SQLite` did not appreciate 4 threads, and down to 1 worker as it still hung with multiple):

`--workers=1 --threads=2 --worker-class=gthread ...`

And success for all requests! Everything from boot onward processes instantly.

```commandline
[2023-09-02 18:56:37 +0000] [1] [INFO] Starting gunicorn 21.2.0
[2023-09-02 18:56:37 +0000] [1] [INFO] Listening at: http://0.0.0.0:8000 (1)
[2023-09-02 18:56:37 +0000] [1] [INFO] Using worker: gthread
[2023-09-02 18:56:37 +0000] [7] [INFO] Booting worker with pid: 7
[2023-09-02 18:56:37 +0000] [8] [INFO] Booting worker with pid: 8
172.17.0.1 - - [02/Sep/2023:18:56:54 +0000] "GET / HTTP/1.1" 200 1165 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0"
172.17.0.1 - - [02/Sep/2023:18:56:54 +0000] "GET /static/simple.min.css HTTP/1.1" 200 0 "http://127.0.0.1:8000/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0"
172.17.0.1 - - [02/Sep/2023:18:56:54 +0000] "GET /api/static/style.css HTTP/1.1" 200 0 "http://127.0.0.1:8000/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0"
172.17.0.1 - - [02/Sep/2023:18:56:54 +0000] "GET /favicon.ico HTTP/1.1" 404 207 "http://127.0.0.1:8000/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0"
172.17.0.1 - - [02/Sep/2023:18:56:58 +0000] "POST /new HTTP/1.1" 302 189 "http://127.0.0.1:8000/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0"
```
