from fastapi import FastAPI

app = FastAPI()

@app.get("/home")
def read_root():
    return {"hello": "mcc student!!!!"}

@app.get("/about")
def about():
    return {"msg": "about us"}