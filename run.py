from flask import Flask
from flask import request, render_template

from controller import urls

app = Flask(__name__)


@app.route('/')
def root():
    return render_template("default.html")


@app.route('/<path:path>')
def otherpath(path):
    return urls.dispatch(request, path)

if __name__ == '__main__':
    app.run(debug=True)
