# main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

moustaphaabdelaal010@cloudshell:~/projects/testapi (cobalt-ship-434308-h6)$ cat Dockerfile 
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8
COPY . /app
