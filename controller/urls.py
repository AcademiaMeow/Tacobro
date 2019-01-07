import re
from flask import Response, redirect
from views import board, post, account, user, advertisement

from kernel.url import path


# 規則：
# 參數1:
# 目前只支援兩種 str & int
# 格式 <name:type>
# name 為參數名稱 / type 為str或int

# 參數2:
# 你的 view function 不用加括號 ^_^

# 參數3:
# login_required 預設為 False

def robots(request):
    resp = Response("Disallow: /admin_panel/")
    resp.headers["content-type"] = "text/plain; charset=utf-8"
    return resp


def admin(request):
    return 'FLAG{OuO_YOU_ARE_ADMIN_OwO}'


url_patterns = [
    # account
    path('login', account.login),
    path('register', account.register),
    path('logout', account.logout, login_required=True),

    path('robots.txt', robots),
    path('admin_panel', admin),

    # user
    path('me', user.me, login_required=True),
    path('card', user.card, login_required=True),
    path('user/<username:str>', user.profile),

    # board
    path('board/<name:str>', board.list),
    path('api/board_add', board.api_board_add, admin_required=True),

    # post
    path('post/<id:int>', post.post),
    path('api/post_delete', post.api_post_delete, login_required=True),

    path('ad', advertisement.buy_ad, login_required=True),

    # # # # # # # # #
    # SOME COOL API #
    # # # # # # # # #
    path('api/user/profile', user.api_profile, login_required=True),
    path('api/user/avatar', user.api_avatar, login_required=True),

    path('api/follow/<follow_id:int>', user.api_follow, login_required=True),
    path('api/unfollow/<follow_id:int>', user.api_unfollow, login_required=True),
    path('api/drawcard', user.api_drawcard, login_required=True),

    path('api/post_article', post.api_post_article, login_required=True),
    path('api/comment/<id:int>', post.api_comment, login_required=True),

    path('api/post/edit/<id:int>', post.api_edit, login_required=True),
    path('api/post/like/<id:int>', post.api_post_like, login_required=True),
    path('api/post/dislike/<id:int>', post.api_post_dislike, login_required=True),

    path('api/ad', advertisement.api_buy_ad, login_required=True),
    path('api/read_notification/<id:int>', user.api_read_notification, login_required=True),
    
]


def dispatch(request, path):
    for url in url_patterns:
        rule = url[0]
        view_f = url[1]
        login_required = url[2]
        admin_required = url[3]

        # dispatch by rule
        match = re.match(rule, path)
        if match:
            if login_required and not request.user:
                return redirect('/login')
            if admin_required and not request.user['is_admin']:
                return '403 permission dinied'

            kwargs = match.groupdict()
            kwargs['request'] = request
            return view_f(**kwargs)
    else:
        return '404 not found'
