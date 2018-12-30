from flask import Flask
from flask import request

from kernel.template_engine import Template
from views.board import BoardViews

app = Flask(__name__)


@app.route('/')
def root():
    return 'root'


@app.route('/<path:path>')
def router(path):
    print(path)
    if 'board' == path.split('/')[0]:
        return BoardViews().list(request)

    if 'login' == path.split('/')[0]:
        return Template("login.html").render(request)

    if 'template' == path.split('/')[0]:
        return Template("test_template.html").render(request, {
                "name": "Test",
                "age": 20,
                "ouo?": True,
                "secret": "S3CR3T"
            })

    return path


if __name__ == '__main__':
    app.run(debug = True)
