from fastapi import FastAPI

app = FastAPI()

@app.get("/greet")
def greet():
    return {"message": "Hello world!!"}