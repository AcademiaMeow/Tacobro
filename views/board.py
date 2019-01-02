from flask import request, render_template


def list(request, name):
    return render_template("board.html", **locals())
