from models.model import model


class Board(model):

    def __init__(self, name, description):
        self.name = name
        self.description = description
