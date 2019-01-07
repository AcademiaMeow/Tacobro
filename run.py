from flask import Flask
from flask import request, render_template, redirect, session
from models.User import User
from models.Notifications import Notifications
from controller import urls
from kernel.template_engine import markdown, no_markdown
import jinja2
import re
import os

from views.timeline import timeline

jinja2.filters.FILTERS['markdown'] = markdown
jinja2.filters.FILTERS['no_markdown'] = no_markdown

app = Flask(__name__)
app.config['SESSION_TYPE'] = 'memcached'
app.config['SECRET_KEY'] = os.getenv('TACA_SECRET')



def set_user():
    user = session.get("user")
    if user:
        if User.filter(id=user['id']):
            request.user = User.filter(id=user['id'])[0]
            request.user['notifications'] = Notifications.filter(user=user['id'], has_read=0)
        else:
            request.user = None
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
    app.run(debug=True)
