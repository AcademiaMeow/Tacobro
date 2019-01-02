from flask import request, session, redirect, render_template

def profile(request):
    return render_template("profile.html", **locals())