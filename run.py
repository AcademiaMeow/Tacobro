from flask import Flask
from flask import request

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
    return path


if __name__ == '__main__':
    app.run(debug=True)
