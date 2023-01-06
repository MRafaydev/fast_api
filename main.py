from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Post(BaseModel):
    title: str
    content: str


@app.get("/")
def home_page():
    return {
        "Welcome": "To Home Page"
    }


@app.post("/create_post")
def create_post(post: Post):
    print(post)
