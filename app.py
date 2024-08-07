from namer import Namer
from flask import Flask, render_template, request
import os

GIGACHAT_KEY = os.environ.get("GIGACHAT_KEY")
GIGACHAT_MODEL = os.environ.get("GIGACHAT_MODEL", "GigaChat")

app = Flask(__name__)

namer = Namer(GIGACHAT_KEY, gigachat_model=GIGACHAT_MODEL)


@app.route('/', methods=['GET'])
def hello_world():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def generate():
    description = request.json['description']
    template = request.json['template']
    return namer.generate(description, template)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
