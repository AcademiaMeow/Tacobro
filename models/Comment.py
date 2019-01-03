from models.model import model
from datetime import datetime

class Comment(model):

    def __init__(self, author, post, content, last_modify=datetime.now(), publish_date=datetime.now()):
        self.author = author
        self.post = post
        self.last_modify = last_modify
        self.publish_date = publish_date
        self.content = content
