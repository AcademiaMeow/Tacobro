import json
from random import choice
from operator import itemgetter

from datetime import datetime
from flask import request, session, redirect, render_template, jsonify
from models.User import User
from models.Post import Post
from models.Following import Following, Friendship


def profile(request, username):
    user = User.filter(username=username)
    if not user:
        return '404 not found'
    user = user[0]
    id = int(user['id'])

    if request.user and request.user.get('id') == int(id):
        return redirect('/me')

    postlist = Post.filter(author=id)
    following = Following.filter(user_no=id)
    follower = Following.filter(following_no=id)

    fs_ = Friendship.filter(user_A=id) + Friendship.filter(user_B=id)
    friendship = list()
    for f in fs_:
        if f['user_A'] == int(id):
            friendship.append(User.filter(id=f['user_B'])[0])
            friendship[-1]['strength'] = f['strength']
        elif f['user_B'] == int(id):
            friendship.append(User.filter(id=f['user_A'])[0])
            friendship[-1]['strength'] = f['strength']
    friendship.sort(key=lambda x: x['strength'], reverse=True)
    if len(friendship) > 5:
        friendship = friendship[:5]

    if request.user:
        is_followed = bool(Following.filter(
            user_no=request.user['id'], following_no=user['id']))
    return render_template("profile.html", **locals())


def me(request):
    user = User.filter(id=request.user['id'])[0]
    id = int(user['id'])
    postlist = Post.filter(author=id)
    following = Following.filter(user_no=id)
    follower = Following.filter(following_no=id)

    fs_ = Friendship.filter(user_A=id) + Friendship.filter(user_B=id)
    friendship = list()
    for f in fs_:
        if f['user_A'] == int(id):
            friendship.append(User.filter(id=f['user_B'])[0])
            friendship[-1]['strength'] = f['strength']
        elif f['user_B'] == int(id):
            friendship.append(User.filter(id=f['user_A'])[0])
            friendship[-1]['strength'] = f['strength']
    friendship.sort(key=lambda x: x['strength'], reverse=True)
    if len(friendship) > 5:
        friendship = friendship[:5]
    is_me = True
    return render_template("profile.html", **locals())


def card(request):
    return render_template("card.html", **locals())


# API

def api_follow(request, follow_id):
    if User.filter(id=user_id):
        return '404 not found'
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


def api_unfollow(request, follow_id):
    if User.filter(id=user_id):
        return '404 not found'
    if request.method == 'POST':
        user_id = int(request.user['id'])
        follow_id = int(follow_id)

        f = Following.filter(user_no=user_id, following_no=follow_id)
        if f:
            Following.delete(f[0]['id'])

            fs_ = (Friendship.filter(user_A=user_id, user_B=follow_id) +
                   Friendship.filter(user_A=follow_id, user_B=user_id))
            if fs_:
                Friendship.delete(fs_[0]['id'])
            else:
                return '403 - fs'
            return '200'
        else:
            # not exist
            return '403 - unfollow'
    else:
        return 'FLAG{you_GET_nothing}'


def api_profile(request):
    if request.method == 'POST':
        POST = json.loads(request.data)
        User.update(id=request.user['id'], profile=POST['content'])
        return '200'
    else:
        return 'FLAG{you_GET_nothing}'


def api_drawcard(request):
    all_users = User.filter()
    avaliable_user = list()
    for user in all_users:
        if (user['id'] != request.user['id'] and
                not Following.filter(user_no=request.user['id'], following_no=user['id'])):
            avaliable_user.append(user)

    if len(avaliable_user) == 0:
        return '400 - 整個網站都是你的好友了！'
    else:
        return jsonify(choice(avaliable_user))
