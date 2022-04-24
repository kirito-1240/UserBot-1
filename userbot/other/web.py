import os
os.system("pip install flask")
from threading import Thread
from flask import Flask

file = __file__

app = Flask(__name__)

@app.route('/<text>', methods=['GET'])
def banner(text: str):
    return text

thread = Thread(target=lambda: app.run(host='0.0.0.0', debug=False))
thread.start()
