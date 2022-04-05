import os
os.system("pip install flask")
os.system("pip install django")

from flask import Flask

app = Flask(__name__)

@app.route('/temperature', methods=['POST'])
def temperature():
    return "Hi Baby"

@app.route('/')
def index():
    return "hi Baby"

if __name__ == '__main__':
    app.run(debug=True)
