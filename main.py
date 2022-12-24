from fastapi import FastAPI

app = FastAPI()

id = 1

@app.get("/")
def read_root():
    return {"Hello": "World"}
    return {"id": id}
