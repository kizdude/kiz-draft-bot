from flask import Flask
from threading import Thread

app = Flask('nuts')

@app.route('/')
def home():
    return "Hello. I am alive!"

def run():
  app.run()

def keepalive():
    t = Thread(target=run)
    t.start()
