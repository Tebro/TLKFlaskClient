from flask import Flask, render_template
import yaml, os
from TLK import get_persons

app = Flask(__name__)
app.debug = True
config = None

@app.route('/')
def hello_world():
    return render_template("index.html", persons=get_persons())


if __name__ == '__main__':
    app.run(host="0.0.0.0")
