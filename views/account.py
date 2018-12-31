from flask import request, render_template

def login(request):
    return render_template("login.html")