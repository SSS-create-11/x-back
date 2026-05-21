import json
from fastapi import FastAPI
from pydantic import BaseModel
import os
from fastapi.middleware.cors import CORSMiddleware


app=FastAPI()

# 👇 ここから「魔法の設定」を追加だわん！
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # どこからのアクセスも許可するよ！という意味だわん
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


db=[]
class Tweet(BaseModel):
 content: str


if os.path.exists("tweets.json"):
 with open("tweets.json","r",encoding="utf-8") as f:
  json_data=json.load(f)
  for i in json_data:
   db.append(Tweet(**i))


#記録をファイルに書き込む関数
def save_to_file():
 with open("tweets.json","w",encoding="utf-8") as f:
  json_data=[]
  for t in db:
   kona=t.model_dump()
   json_data.append(kona)
  json.dump(json_data,f,ensure_ascii=False, indent=4)

@app.post("/tweet")
def create_tweet(tweet:Tweet):
 db.append(tweet)
 save_to_file()
 return{"status":"登録"}

@app.get("/tweets")
def check():
 return{"checktweets":db}


