from datetime import datetime
from flask import request, session, redirect, render_template
from models.User import User
from models.Post import Post
from models.Following import Following


def profile(request, id=None):
    user = User.filter(id=id)[0]
    postlist = Post.filter(author=id)
    following = Following.filter(user_no=id)
    follower = Following.filter(following_no=id)
    return render_template("profile.html", **locals())


def me(request):
    user = request.user
    id = user['id']
    postlist = Post.filter(author=id)
    following = Following.filter(user_no=id)
    follower = Following.filter(following_no=id)
    return render_template("profile.html", **locals())


# API

def follow(request):
    if request.method == 'POST':
        pass
