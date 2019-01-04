import json
from flask import request, session, redirect, render_template, jsonify
from models.User import User
from models.Post import Post
from models.Ad import Ad
from models.AdBoard import AdBoard


def buy_ad(request):
    print(AdBoard.filter())
    return render_template("ad.html", **locals())


def api_buy_ad(request):
    if request.method == 'POST':
        check_url = lambda url: url.startswith("https://") or url.startswith("http://")

        try:
            ad_data = json.loads(request.data)
            user_id = int(request.user['id'])

            if not check_url(ad_data['img_url']) or not check_url(ad_data['link_url']):
                return jsonify({"success": False, "message": "網址要是 http(s):// 開頭啦幹"})

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
