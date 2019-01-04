from flask import request, session, redirect, render_template
from models.User import User
import hashlib
import re
from random import choice

default_profile_picture = [
    'https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/apple/155/thinking-face_1f914.png',
    'https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/google/146/thinking-face_1f914.png',
    'https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/samsung/148/thinking-face_1f914.png',
    'https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/twitter/154/thinking-face_1f914.png',
    'https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/emojione/151/thinking-face_1f914.png',
    'https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/lg/57/thinking-face_1f914.png',
    'https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/htc/122/thinking-face_1f914.png',
    'https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/samsung/148/face-with-tears-of-joy_1f602.png',
    'https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/emojione/151/face-with-tears-of-joy_1f602.png',
    'https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/mozilla/36/face-with-tears-of-joy_1f602.png',
    'https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/samsung/148/smiling-face-with-smiling-eyes-and-three-hearts_1f970.png',
    'https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/emojione/151/smiling-face-with-smiling-eyes-and-three-hearts_1f970.png',
    'https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/apple/155/smiling-face-with-smiling-eyes-and-three-hearts_1f970.png',
    'https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/samsung/148/smiling-face-with-smiling-eyes_1f60a.png',
    'https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/emojione/151/smiling-face-with-smiling-eyes_1f60a.png',
    'https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/facebook/65/smiling-face-with-smiling-eyes_1f60a.png',
    'https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/mozilla/36/smiling-face-with-smiling-eyes_1f60a.png',
]


def login(request):
    message = None
    username = request.form.get('username')
    password = request.form.get('password')

    if username or password:
        hash_password = hashlib.sha256(
            password.encode('utf-8')).hexdigest()
        user = User.filter(username=username, password=hash_password)
        if user:
            session['user'] = User.filter(username=username)[0]
            request.user = User.filter(username=username)[0]
            return redirect('/')
        else:
            message = "帳號或密碼錯誤"

    return render_template("login.html", **locals())


def register(request):
    message = None
    if request.method == 'POST':
        username = request.form.get('username').lower()
        password = request.form.get('password')
        first_name = request.form.get('first_name')

        if username or password:
            if not re.match("[A-Za-z0-9]{6,}", username) or not re.match("[A-Za-z0-9]{6,}", password):
                message = "帳號密碼須為大於 6 個字的英文/數字字串"
            else:
                if User.filter(username=username):
                    message = "帳號已存在 :("
                else:
                    hash_password = hashlib.sha256(
                        password.encode('utf-8')).hexdigest()
                    User(
                        picture=choice(default_profile_picture),
                        username=username,
                        password=hash_password,
                        first_name=first_name,
                        last_name=None,
                        last_login=None,
                        login_count=None,
                        is_admin=False,
                        is_active=True,
                        profile='我還沒有寫自我介紹喔！ :-)'
                    ).create()
                    session['user'] = User.filter(username=username)[0]
                    request.user = User.filter(username=username)[0]
                    return redirect('/')
    return render_template("register.html", **locals())


def logout(request):
    session.clear()
    return redirect('/login')
