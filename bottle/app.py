import os
from bottle import route, run

@route('/')
def hello():
    return 'helloworld'
    
run(host="0.0.0.0",port=int(os.environ.get("PORT",8080)))
