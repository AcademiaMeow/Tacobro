from flask import request, render_template, session, redirect
import re

def login(request):
    message = None
    username = request.form.get('username')
    password = request.form.get('password')

    if username or password:
        if not re.match("[A-Za-z0-9]{6,}", username) or not re.match("[A-Za-z0-9]{6,}", password):
            message = "帳號密碼須為大於 6 個字的英文/數字字串"
        else:
            # TBD
            session['username'] = username
            message = "帳號登入成功"
    return render_template("login.html", message=message, username=session.get('username'))

def register(request):
    message = None
    username = request.form.get('username')
    password = request.form.get('password')
    print(request.form.items())

    if username or password:
        if not re.match("[A-Za-z0-9]{6,}", username) or not re.match("[A-Za-z0-9]{6,}", password):
            message = "帳號密碼須為大於 6 個字的英文/數字字串"
        else:
            # TBD
            message = "帳號註冊成功"
    
    return render_template("register.html", message=message)

def logout(request):
    session.clear()
    return redirect('/login')