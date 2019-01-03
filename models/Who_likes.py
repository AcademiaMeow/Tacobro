from models.model import model


class Who_likes(model):

    def __init__(self, user_no, like_no):
        self.user_no = user_no
        self.like_no = like_no
