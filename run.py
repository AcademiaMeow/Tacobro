from flask import Flask
from flask import request, render_template, redirect, session
from models.User import User
from controller import urls

from views.timeline import timeline

app = Flask(__name__)
app.config['SESSION_TYPE'] = 'memcached'
app.config['SECRET_KEY'] = os.getenv('TACA_SECRET')


def set_user():
    user = session.get("user")
    if user:
        request.user = User.filter(id=user['id'])[0]
    else:
        request.user = None
    return request


@app.route('/')
def root():
    set_user()
    if not request.user:
        return redirect('/login')
    return timeline(request)


@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def otherpath(path):
    set_user()
    return urls.dispatch(request, path)


if __name__ == '__main__':
    import os
    app.run()
    # Generate secret_key:
    # $ python -c "import os, binascii;print(binascii.hexlify(os.urandom(24)))"
    # $ export TACA_SECRET=4061e68c69c9046c45f4669001283d6ba4c919127c212488
