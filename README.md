# CeleryAsync


   - This repo shows how to use celery with redis broker

Steps

1. Install Celery using 

    apt install python-celery-common
    
Add
```
   export LC_ALL=C.UTF-8
   export LANG=C.UTF-8
```
2. Install Redis server using
```
    wget http://download.redis.io/redis-stable.tar.gz
    tar xvzf redis-stable.tar.gz
    cd redis-stable
    make
```
    see full instruction in https://redis.io/topics/quickstart


3. Install dependencies using 
 ```
    pip3 install -r requirements.txt
```
4. Start worker Celery with command in new console
```
    celery -A parallelproject worker -l info
```
5. Fire query
```http://{YOUR_URL:PORT}/test?q1=hello```
to the server the response will come as
```{"response": "request string for q1 is hello"}```
instantaneously
6. The celery worker will perform the task in background.
7. Final response in celery logs is
```
[2021-10-31 12:28:22,721: INFO/ForkPoolWorker-3] Task parallelproject.tasks.process[e1432eab-0fec-4a2f-a1fa-563062f501c5] succeeded in 60.16269509999984s: 'wt{{~'
```
