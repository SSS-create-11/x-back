from pydantic import BaseModel

import fastapi
app=fastapi.FastAPI()
@app.get("/")
def read_root():
 return {"message":"Hello"}

@app.get("/seiji")
def read_root2():
 return {"seiji"}

@app.get("/hello/{name}")
def read_root3(name:str):
 return {"message":name}

class Tweet(BaseModel):
 content:str

@app.post("/tweet")
def create_tweet(tweet:Tweet):
 return{"status":"投稿完了","postcontens":tweet.content}


@app.post("/tweet_any")
def create_tweet_any(payload: dict):
    content = payload.get("content")
    return {"data": content,"alldata":payload}
