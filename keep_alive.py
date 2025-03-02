from flask import Flask
from threading import Thread
import requests
import time

app = Flask('')

@app.route('/')
def home():
    return "I'm alive"

def run():
    app.run(host='0.0.0.0', port=8080)

def ping():
    while True:
        try:
            requests.get("http://127.0.0.1:8080/")
        except requests.exceptions.RequestException:
            print("Failed to reach the server.")
        time.sleep(30)  # 30초마다 호출

def keep_alive():
    t = Thread(target=run)
    t.start()

    t2 = Thread(target=ping, daemon=True)
    t2.start()