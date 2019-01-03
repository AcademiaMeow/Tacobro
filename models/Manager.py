from models.model import model


class Manager(model):

    def __init__(self, board_no, user_no):
        self.board_no = board_no
        self.user_no = user_no
