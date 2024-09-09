# main.py
from fastapi import FastAPI

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    print("FastAPI application is starting...")


@app.get("/")
def read_root():
    print("Hello World!")
    return {"message": "Hello, World! from inside"}
