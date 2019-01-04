from flask import Flask
from flask import request, render_template, redirect, session
from models.User import User
from controller import urls
import os

app = Flask(__name__)
app.secret_key = os.getenv('TACA_SECRET')
# Generate secret_key:
# $ python -c "import os, binascii;print(binascii.hexlify(os.urandom(24)))"
# $ export TACA_SECRET=***

def set_user():
    user = session.get("user")
    if user:
        request.user = user
    else:
        request.user = None
    return request


@app.route('/')
def root():
    set_user()
    return redirect("/me")


@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def otherpath(path):
    set_user()
    return urls.dispatch(request, path)


if __name__ == '__main__':
    app.run(debug=True)
