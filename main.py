from fastapi import FastAPI

app = FastAPI()

@app.get("/")

def read_root():

    return {"platypus": 'Welcome to my Api'}

@app.get("/posts")
def get_posts():
    return {"data": "your post was submitted"}

@app.post("/createposts")
def create_posts():
    return {"data": "your post was not submitted"}
