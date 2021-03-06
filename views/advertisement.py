import json
from flask import request, session, redirect, render_template, jsonify
from models.User import User
from models.Post import Post
from models.Ad import Ad
from models.AdBoard import AdBoard
import random


def buy_ad(request):
    return render_template("ad.html", **locals())


def api_buy_ad(request):
    if request.method == 'POST':
        def check_url(url, domain=""): return url.startswith(
            "https://"+domain+"/") or url.startswith("http://"+domain+"/")

        try:
            ad_data = json.loads(request.data)
            user_id = int(request.user['id'])
            
            if not re.match(r"^https?:\/\/(\w+\.)?imgur.com\/[\w\d]+(\.[a-zA-Z]{3})?$", ad_data['img_url']) or not check_url(ad_data['link_url']):
                return jsonify({"success": False, "message": "網址怪怪ㄉ喔"})

            ad_position = AdBoard.filter(position=ad_data['positoin'])[0]

            if ad_position['price'] > request.user['tacobit']:
                return jsonify({"success": False, "message": "錢不夠 = ="})

            User.update(
                id=user_id,
                tacobit=request.user['tacobit']-ad_position['price'])

            aid = Ad(ad=ad_data['img_url'], poster=user_id, URL=ad_data['link_url'],
                     start_date=None, end_date=None, board=ad_position['id']).create()

            return jsonify({"success": True, "id": aid})
        except:
            return jsonify({"success": False, "message": "我也不知道發生了啥，反正出錯ㄌ"})

    return "FLAG{you_GET_nothing}"


def get_ads():
    def choice(ls): return random.choice(ls) if ls else None

    ad_list = {
        "left": choice(Ad.filter(board=1)),
        "bottom": choice(Ad.filter(board=2)),
        "right": choice(Ad.filter(board=3))
    }
    return ad_list
