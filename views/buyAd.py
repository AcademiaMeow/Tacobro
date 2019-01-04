from flask import request, session, redirect, render_template
from models.User import User
from models.Post import Post
from models.Ad import Ad
from models.AdBoard import AdBoard

def buyAd(request):
    if request.method == 'POST':
        #user_id = int(request.user['id'])
        ad_img = request.form.get('ad_img')
<<<<<<< Updated upstream
        print(ad_img)
=======
>>>>>>> Stashed changes
        ad_URL = request.form.get('ad_URL')

        Ad(ad=ad_img, poster=None , URL=ad_URL, start_date=None, end_date=None, board=None).create()

        position = request.form.get('ad')

        if position == "left":
            AdBoard(position="(0,0)", width=200, height=200, price=128).create()
        elif position == "middle":
            AdBoard(position="(0.5,0)", width=200, height=200, price=256).create()
        elif position == "right":
            AdBoard(position="(1,0)", width=200, height=200, price=512).create()

    return render_template("ad.html", **locals())
