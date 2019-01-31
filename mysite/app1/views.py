from django.shortcuts import render
from django.http.response import HttpResponse
from django.http import HttpResponse
from . import aaaa
import requests
import json
import re

REPLY_ENDPOINT = 'https://api.line.me/v2/bot/message/reply'
ACCESS_TOKEN = '6SbncqMyX6Q6PqUFulq8qeUMEgQPvs2pQzLxIi6v7Gy/l2mtg3ziW958dn+0mkSvrpld5p9hA7KxDIM9egsE3pXl7YZnxq8JirkP9oOXkUvBWP+0nZsDauLC5wUgHeWZUL1wdB04t89/1O/w1cDnyilFU='
HEADER = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + ACCESS_TOKEN
}

# Create your views here.
def index(request):
    return HttpResponse("hello")
    
def reply_text(reply_token,id,text):
    reply = "abcdef" #返す文字列
    payload = {
          "replyToken":reply_token,
          "messages":[
                {
                    "type":"text",
                    "text": reply
                }
            ]
    }
    
    
    
    if(text=='きろくを見る'):
        print("This is kiroku")
    elif(text=='キャンセル'):
        print("cancel")
    elif([]!=re.findall(r"\w+を始める",text)):
       print("start")
    elif([]!=re.findall(r"\w+を終わる",text)):
        print("end")
    else:
        print("no")
        
    
    print(text)
    aaaa.write(id,text)
    requests.post(REPLY_ENDPOINT, headers=HEADER, data=json.dumps(payload)) # LINEにデータを送信
    return None
    
#ラインからのリクエストを受け取る関数
def callback(request):
    # requestの情報をdict形式で取得
    request_json = json.loads(request.body.decode('utf-8')) 
    for e in request_json['events']:
        reply_token = e['replyToken'] # 返信先トークンの取得
        message_type = e['message']['type'] # typeの取得

        if message_type == 'text':
            id = e['message']['id'] # 受信メッセージの取得
            text = e['message']['text'] # 受信メッセージの取得
            reply_text(reply_token, id,text) # LINEにセリフを送信する関数
    return HttpResponse("reply") # テスト用
    