from models.model import model


class Who_dislikes(model):

    def __init__(self, user_no, dislike_no):
        self.user_no = user_no
        self.dislike_no = dislike_no
