class User():

    def __init__(self, id, picture, username, password, first_name, last_name, birthday, join_date, last_login, login_count, is_admin, is_active, profile, follower, following):
        self.id = id
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
        self.follower = follower
        self.following = following
