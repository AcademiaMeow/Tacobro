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
    if request.method == 'POST' and request.user:
        check_url = lambda url: url.startswith("https://") or url.startswith("http://")
        try:
            ad_data = json.loads(request.data)
            user_id = int(request.user['id'])

            if check_url(ad_data['img_url']) and check_url(ad_data['link_url']):
                return jsonify({"success": False, "message": "網址要是 http(s):// 開頭啦幹"})

            ad_position = AdBoard.filter(position=ad_data['positoin'])[0]
            aid = Ad(ad=ad_data['img_url'], poster=user_id, URL=ad_data['link_url'],
                        start_date=None, end_date=None, board=ad_position['id']).create()

            return jsonify({"success": True, "id": aid})
        except:
            return jsonify({"success": False, "message": "我也不知道發生ㄌ啥，反正出錯ㄌ"})

    return "FLAG{you_GET_nothing}"
