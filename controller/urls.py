import re
from views import board, post, account

from kernel.url import path


# 規則：
## 參數1:
    # 目前只支援兩種 str & int
    # 格式 <name:type>
    # name 為參數名稱 / type 為str或int

## 參數2:
    # 你的 view function 不用加括號 ^_^

url_patterns = [
    path('login/', account.login),
    path('board/<name:str>', board.list),
    path('post/<id:int>', post.single),
    path('post/<id:int>/<id2:int>', post.meow)
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
