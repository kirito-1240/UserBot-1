from flask import Flask

app = Flask(__name__)

@app.route("/")
def index(): 
    return "<html><body><h1>Site Running!</h1></body></html>"
@app.route("/hi")
def hello(): 
    return "<html><body><h1>Site Running 2!</h1></body></html>"

if __name__ == "__main__":
    app.run()