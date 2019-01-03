from flask import render_template
from models.User import User
from models.Following import Following
from models.Board import Board
from models.Post import Post


def timeline(request):
    board_list = Board.filter()
    p_ = Post.filter(sort=['publish_date'], desc=[True])
    posts = list()
    for post in p_:
        post['author_data'] = User.filter(id=post['author'])[0]
        if post['author'] == request.user['id']:
            posts.append(post)
        if Following.filter(user_no=request.user['id'], following_no=post['author']):
            posts.append(post)
    return render_template('timeline.html', **locals())
