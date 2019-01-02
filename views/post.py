from flask import request, render_template

def post(request, id):
    return render_template("post.html", **locals())


def meow(request, id, id2):
    return id + id2
