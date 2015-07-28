from flask import Flask, render_template
from TLK import get_persons, get_person

app = Flask(__name__)
app.debug = True
config = None

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route("/persons/")
def persons():
    return render_template("persons.html", persons=get_persons())

@app.route("/person/<path:id>")
def person(id):
    return render_template("person.html", person=get_person(id))


if __name__ == '__main__':
    app.run(host="0.0.0.0")
