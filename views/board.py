from flask import request, render_template
from models.User import User
from models.Board import Board
from models.Post import Post


def list(request, board_id):
    board_list = Board.filter()
    board = Board.filter(id=board_id)[0]
    posts = Post.filter(board=board['id'])
    for post in posts:
        post['author_data'] = User.filter(id=post['author'])[0]
    return render_template("board.html", **locals())
