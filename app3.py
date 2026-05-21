#fastapiのインポート
import fastapi
import json
import os
from pydantic import BaseModel
#データの入る配列も必要
db=[]

#basemodelはガードマン保存する情報の補正
class Tweet(BaseModel):
  content : str

#Fastapiのオブジェクトの作成
app=fastapi.FastAPI()
#登録した情報を保存する場所も必要
def save():
 #データ変換したものを入れるよう配列
 file_db=[]
#ファイルを作成して開いていくよ
 with open("tweet3.json","w",encoding="utf-8")as f:
  #オブジェクトを辞書になしていく
  for i in db:
    #辞書に直す
    a=i.model_dump()
    file_db.append(a)
  #まとめて変換m文字化け防止とindent
  json.dump(file_db,f,ensure_ascii=False,indent=4)
    
    

#つなぐやりとり口を作る(表示)getここの階層きたら表示、ここなら登録のようにやっていく
@app.post("/tweet")
def createtweet(tweet:Tweet):
  db.append(tweet)
  save()
  #fastapi側に返す
  return  {"status":"githubでもvsでもつながったよ"}
#つなぐやり取り口を作る(登録)post

#登録用
@app.get("/tweetget")
def tourokutweet():
  return db
  
