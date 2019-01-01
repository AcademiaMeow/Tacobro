from flask import Flask
from flask import request, render_template

from controller import urls

app = Flask(__name__)


@app.route('/')
def root():
    return render_template("default.html")


@app.route('/<path:path>', methods = ['GET', 'POST', 'PUT', 'DELETE'])
def otherpath(path):
    return urls.dispatch(request, path)

if __name__ == '__main__':
    import os
    app.secret_key = os.getenv('TACA_SECRET')
    # Generate secret_key:
    # $ `python -c "import os, binascii;print(binascii.hexlify(os.urandom(24)))"`
    # $ export TACA_SECRET=***
    app.run(debug=True)
