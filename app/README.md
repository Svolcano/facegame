# Run
```
uvicorn main:app --reload --host=0.0.0.0 --port=8008
```
or with monitor
```
gunicorn main:app -b 0.0.0.0:8001 -w 4 -k uvicorn.workers.UvicornWorker
```
# Doc
```
http://127.0.0.1:8000/docs
```
