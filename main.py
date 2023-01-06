from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home_page():
    return {
        "Welcome": "To Home Page"
    }

@app.post("/login")
def login_user(username, password):
    return (username,password)
    