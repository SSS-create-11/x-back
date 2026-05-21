from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
#ここでシェフ爆誕
app=FastAPI()
db=[]
#型はめ
class Tweet(BaseModel):
 content:str

@app.get("/")
def read1():
 return {"status":"active"}

#たまったツイートをすべて確認できる場所
@app.get("/alltweetcheck")
def check():
 return {"allcheck:": db}

#ツイートを保存する場所
@app.post("/tweet")
def create_tweet(tweet:Tweet):
 db.append(tweet)
 return{"status":"保存完了","kazu":len(db)}
