from models.model import model


class Comment(model):

    def __init__(self, author, post, last_modify=datetime.now(), publish_date=datetime.now(), content):
        self.author = author
        self.post = post
        self.last_modify = last_modify
        self.publish_date = publish_date
        self.content = content
