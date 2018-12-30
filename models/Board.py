from models.model import model


class Board(model):

    def __init__(self, name, description, bucket_list, manager):
        self.name = name
        self.description = description
        self.bucket_list = bucket_list
        self.manager = manager
