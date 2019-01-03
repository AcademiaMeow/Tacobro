from models.model import model


class Following(model):

    def __init__(self, user_no, following_no):
        self.user_no = user_no
        self.following_no = following_no


class Friendship(model):

    def __init__(self, user_A, user_B):
        self.user_A = user_A
        self.user_B = user_B
        self.strength = 0
