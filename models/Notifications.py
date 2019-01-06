from models.model import model
from datetime import datetime


class Notifications(model):

    def __init__(self, link, content, user, has_read=0, notified_date=datetime.now()):
        self.notified_date = notified_date
        self.link = link
        self.content = content
        self.has_read = has_read
        self.user = user
