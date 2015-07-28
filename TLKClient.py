from flask import Flask, render_template
from TLK import get_persons, get_person, get_light_persons, get_light_person

app = Flask(__name__)
app.debug = True
config = None

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/persons/")
def persons():
    return render_template("persons.html", persons=get_light_persons())

@app.route("/person/<pk>")
@app.route("/person/<pk>/<more>")
def person(pk, more="less"):
    person = None
    if more is not "less":
        more = True
        person = get_person(pk)
    else:
        more = False
        person = get_light_person(pk)

    return render_template("person.html", person=person, more=more)


if __name__ == '__main__':
    app.run(host="0.0.0.0")
