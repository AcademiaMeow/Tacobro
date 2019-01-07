from flask import Flask
from flask import request, render_template, redirect, session
from models.User import User
from models.Notifications import Notifications
from controller import urls
import re
import jinja2
import os

from views.timeline import timeline

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

@app.template_filter('no_markdown')
def no_markdown(string):
    string = str(jinja2.escape(string))

    def _repl(matched):
        mapping = {'bold': "b", "italics": "i", "strike": "s", "code": "code"}
        markdown_type = matched.lastgroup
        return matched.groupdict()[markdown_type]

    markup = re.sub(r"\*\*(?P<bold>[^**]+)\*\*|__(?P<italics>[^_]+)__|~~(?P<strike>[^~]+)~~|`(?P<code>[^`]+)`",
                    _repl, string, flags=re.MULTILINE)
    return jinja2.Markup(markup)

@app.template_filter('markdown')
def markdown(string):
    string = str(jinja2.escape(string))
    markup = string.replace('\n', '<br/>\n')

    def _repl(matched):
        mapping = {'bold': "b", "italics": "i", "strike": "s", "code": "code"}
        markdown_type = matched.lastgroup

        return "<{tagname}>{content}</{tagname}>".format(
            tagname=mapping[markdown_type],
            content=matched.groupdict()[markdown_type])

    markup = re.sub(r"\*\*(?P<bold>[^**]+)\*\*|__(?P<italics>[^_]+)__|~~(?P<strike>[^~]+)~~|`(?P<code>[^`]+)`",
                    _repl, markup, flags=re.MULTILINE)
    return jinja2.Markup(markup)


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
