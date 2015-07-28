from flask import Flask, render_template
import yaml, os

app = Flask(__name__)
app.debug = True
config = None

@app.route('/')
def hello_world():
    the_url = config['backend']['url']
    return render_template("index.html", the_url=the_url)


if __name__ == '__main__':
    #Read configuration
    with open("%s/config.yml" % os.path.dirname(os.path.realpath(__file__)), 'r') as f:
        config = yaml.load(f)
    app.run(host="0.0.0.0")
