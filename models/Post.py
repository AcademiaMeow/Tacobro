from models.model import model


class Post(model):

    def __init__(self, content, publish_date, last_modify, like_count, dislike_count, author, board):
        self.content = content
        self.publish_date = publish_date
        self.last_modify = last_modify
        self.like_count = like_count
        self.dislike_count = dislike_count
        self.author = author
        self.board = board
