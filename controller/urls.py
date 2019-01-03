import re
from flask import Response
from views import board, post, account, user

from kernel.url import path


# 規則：
# 參數1:
# 目前只支援兩種 str & int
# 格式 <name:type>
# name 為參數名稱 / type 為str或int

# 參數2:
# 你的 view function 不用加括號 ^_^

def robots(request):
    resp = Response("Disallow: /admin_panel/")
    resp.headers["content-type"] =  "text/plain; charset=utf-8"
    return resp

def admin(request):
    return 'FLAG{OuO_YOU_ARE_ADMIN_OwO}'

url_patterns = [
    # account
    path('login', account.login),
    path('register', account.register),
    path('logout', account.logout),

    path('robots.txt', robots),
    path('admin_panel', admin),

    # user
    path('me', user.me),
    path('user/<id:int>', user.profile),

    # board
    path('board/<board_id:int>', board.list),

    # post
    path('post/<id:int>', post.post),

    # # # #
    # API #
    # # # #
    path('api/follow/<follow_id:int>', user.follow),
    path('api/unfollow/<follow_id:int>', user.unfollow)
]


def dispatch(request, path):
    for url in url_patterns:
        rule = url[0]
        view_f = url[1]

        # dispatch by rule
        match = re.search(rule, path)
        if match:
            kwargs = match.groupdict()
            kwargs['request'] = request
            return view_f(**kwargs)
    else:
        return '404 not found'
