from flask import request, render_template
from models.Board import Board

def list(request, name):
    print(Board.filter())
    return render_template("board.html", **locals())
