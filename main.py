from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "root path"}


@app.get("/hello")
async def root():
    return {"message": "Hello World"}
