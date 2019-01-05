import json
from flask import request, render_template, redirect, jsonify
from models.Post import Post
from models.User import User
from models.Comment import Comment
from models.Board import Board
from models.Following import Friendship
from datetime import datetime


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


def api_comment(request, id):
    if request.method == 'POST':
        post_data = json.loads(request.data)
        if len(post_data['content']) > 150:
            return '403'
        Comment(author=request.user['id'], post=id,
                content=post_data['content'],
                publish_date=datetime.now()).create()
        return '200'
    else:
        return 'FLAG{you_GET_nothing}'


def api_post_like(request, id):
    if request.method == 'POST':
        Post.update(id=id, like_count=Post.filter(id=id)[0]['like_count'] + 1)

        author_id = Post.filter(id=id)[0]['author']
        fs = (Friendship.filter(
            user_A=author_id,
            user_B=request.user['id']) +
            Friendship.filter(
            user_A=request.user['id'],
            user_B=author_id))

        if fs:
            Friendship.update(id=fs[0]['id'], strength=fs[0]['strength'] + 10)

        user = User.filter(id=author_id)[0]
        User.update(id=user['id'], tacobit=user['tacobit'] + 1)

        user = User.filter(id=request.user['id'])[0]
        User.update(id=user['id'], tacobit=user['tacobit'] - 1)

        return '200'
    else:
        return 'FLAG{you_GET_nothing}'


def api_post_dislike(request, id):
    if request.method == 'POST':
        Post.update(id=id, dislike_count=Post.filter(
            id=id)[0]['dislike_count'] + 1)
        fs = Friendship.filter(user_A=Post.filter(
            id=id)[0]['id'], user_B=request.user['id']) + Friendship.filter(user_A=request.user['id'], user_B=Post.filter(
                id=id)[0]['id'])
        if fs:
            Friendship.update(id=fs[0]['id'], strength=fs[0]['strength'] - 10)

        user = User.filter(id=request.user['id'])[0]
        User.update(id=user['id'], tacobit=user['tacobit'] - 1)
        return '200'
    else:
        return 'FLAG{you_GET_nothing}'


def api_post_delete(request):
    if request.method == "POST":
        post_data = json.loads(request.data)
        id = post_data['postId']
        post = Post.filter(id=id)
        if not post:
            return jsonify({"success": False})
        Post.delete(post[0]['id'])
        return jsonify({"success": True})
    else:
        return 'FLAG{you_GET_nothing}'


def api_post_article(request):
    if request.method == 'POST':
        try:
            user = User.filter(id=request.user['id'])[0]
            User.update(id=user['id'], tacobit=user['tacobit'] + 10)

            post_article = json.loads(request.data)

            if len(post_article) > 150:
                return jsonify({"success": False})

            ID = Post(content=post_article['content'],
                      board=post_article['board'],
                      author=request.user['id'],
                      publish_date=datetime.now()).create()
            return jsonify({"success": True, "post": ID})
        except:
            return jsonify({"success": False})
    else:
        return 'FLAG{you_GET_nothing}'
