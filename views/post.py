import json
from flask import request, render_template, redirect, jsonify
from models.Post import Post
from models.User import User
from models.Comment import Comment
from models.Board import Board


def post(request, id):
    board_list = Board.filter()

    post = Post.filter(id=id)
    if not post:
        return redirect("/")
    post = post[0]
    author = User.filter(id=post['author'])[0]
    comments = Comment.filter(post=post['id'])
    post['comment_count'] = len(comments)

    for comment in comments:
        comment['author_data'] = User.filter(id=comment['author'])[0]

    return render_template("post.html", **locals())


def api_post_article(request):
    try:
        post_article = json.loads(request.data)
        ID = Post(content=post_article['content'],
                  board=post_article['board'],
                  author=request.user['id']).create()
        print(ID)
        return jsonify({"success": True, "post": ID})
    except:
        return jsonify({"success": False})
