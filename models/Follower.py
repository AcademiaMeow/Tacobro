from models.model import model


class Follower(model):

    def __init__(self, user_no, follower_no):
        self.user_no = user_no
        self.follower_no = follower_no
