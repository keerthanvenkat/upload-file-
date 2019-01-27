from flask_login.mixins import UserMixin



class User(UserMixin):
    def __init__(self,id):
        self.id = id

    def __repr__(self):
        return "%d" % self.id