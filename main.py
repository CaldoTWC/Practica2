# main.py
from flask import Flask

# Esta variable 'app' es la que buscará el servidor
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Cloud!"