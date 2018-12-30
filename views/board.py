# 版

from flask import request


def list(request, name):
    return 'this is <h2>{}</h2> board'.format(name)
