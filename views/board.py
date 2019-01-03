from flask import request, render_template, jsonify
from models.User import User
from models.Board import Board
from models.Post import Post
import json

def list(request, name):
    board_list = Board.filter()

    board = Board.filter(name=name)
    if not board:
        return render_template("board.html", **locals())
    board = board[0]
    posts = Post.filter(board=board['id'])
    for post in posts:
        post['author_data'] = User.filter(id=post['author'])[0]
    return render_template("board.html", **locals())

def api_board_add(request):
    if request.method == "POST":
        print("test")
        post_data = json.loads(request.data)
        board_name = post_data.get('board_name')
        board_content = post_data.get('board_content')
        Board(name=board_name, description=board_content).create()
        return jsonify({'success': True, 'boardname': board_name})
