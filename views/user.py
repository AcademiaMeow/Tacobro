from datetime import datetime
from flask import request, session, redirect, render_template
from models.User import User
from models.Post import Post
from models.Following import Following, Friendship


def profile(request, id=None):
    user = User.filter(id=id)[0]
    postlist = Post.filter(author=id)
    following = Following.filter(user_no=id)
    follower = Following.filter(following_no=id)

    friendship = Friendship.filter(user_A=id) + Friendship.filter(user_B=id)
    return render_template("profile.html", **locals())


def me(request):
    user = request.user
    id = user['id']
    postlist = Post.filter(author=id)
    following = Following.filter(user_no=id)
    follower = Following.filter(following_no=id)
    return render_template("profile.html", **locals())


# API

def follow(request, follow_id):
    if request.method == 'POST':
        user_id = int(request.user['id'])
        follow_id = int(follow_id)

        if Following.filter(user_no=user_id, following_no=follow_id):
            # exist
            return '403'
        else:
            Following(user_no=user_id, following_no=follow_id).create()

            if Following.filter(user_no=follow_id, following_no=user_id):
                Friendship(user_A=user_id, user_B=follow_id).create()
            return '200'


def unfollow(request, follow_id):
    if request.method == 'POST':
        user_id = int(request.user['id'])
        follow_id = int(follow_id)

        f = Following.filter(user_no=user_id, following_no=follow_id)
        if len(f):
            Following.delete(f[0]['id'])
            return '403'
        else:
            # not exist
            return '200'
