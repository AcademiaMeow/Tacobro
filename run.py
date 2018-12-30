from flask import Flask
from flask import request

from kernel.template_engine import Template
from controller import urls

app = Flask(__name__)


@app.route('/')
def root():
    return Template("default.html").render(request)


@app.route('/<path:path>')
def otherpath(path):
    return urls.dispatch(request, path)

if __name__ == '__main__':
    app.run(debug=True)
