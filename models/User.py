from models.model import model
from datetime import datetime


class User(model):

    def __init__(self, username, password, first_name, last_name, profile, birthday=None, picture=None, last_login=None, login_count=None, is_admin=False, is_active=True, join_date=datetime.now()):
        self.picture = picture
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.join_date = join_date
        self.last_login = last_login
        self.login_count = login_count
        self.is_admin = is_admin
        self.is_active = is_active
        self.profile = profile
