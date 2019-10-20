
for bjoern `apt install libev-dev libevdev2`

`wrk -t12 -c400 -d30s -s post.lua http://localhost:8080/test`

## Resnet - aiohttp

```
python aiohttp_app.py
```

```
wrk -t1 -c1 -d30s --timeout 10s -s post.lua http://localhost:8080/test
Running 30s test @ http://localhost:8080/test
  1 threads and 1 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   153.69ms  119.03ms   1.11s    97.26%
    Req/Sec     8.12      2.63    20.00     61.46%
  213 requests in 30.03s, 50.75KB read
Requests/sec:      7.09
Transfer/sec:      1.69KB

```

## Resnet - aiohttp & gunicorn

```
gunicorn aiohttp_app:app --bind localhost:8080 --worker-class aiohttp.worker.GunicornWebWorker
```

```
wrk -t1 -c1 -d30s --timeout 10s -s post.lua http://localhost:8080/test
Running 30s test @ http://localhost:8080/test
  1 threads and 1 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   153.53ms  126.37ms   1.16s    96.85%
    Req/Sec     8.26      2.72    20.00     63.03%
  215 requests in 30.05s, 51.23KB read
Requests/sec:      7.16
Transfer/sec:      1.71KB
```

## Resnet - flask & gunicorn

```
gunicorn flask_app:app --bind localhost:8080
```

```
wrk -t1 -c1 -d30s --timeout 10s -s post.lua http://localhost:8080/test
Running 30s test @ http://localhost:8080/test
  1 threads and 1 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   161.98ms  121.96ms   1.13s    97.12%
    Req/Sec     7.84      2.62    10.00     58.91%
  202 requests in 30.05s, 46.16KB read
Requests/sec:      6.72
Transfer/sec:      1.54KB
```


## Resnet - flask & bjoern

```
python wsgi.py
```

```
wrk -t1 -c1 -d30s --timeout 10s -s post.lua http://localhost:8080/test
Running 30s test @ http://localhost:8080/test
  1 threads and 1 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   159.91ms  127.41ms   1.17s    96.71%
    Req/Sec     7.94      2.66    20.00     57.92%
  206 requests in 30.03s, 35.61KB read
Requests/sec:      6.86
Transfer/sec:      1.19KB
```
