from ..dm import db
from . import BaseQuery

class UserQuery(BaseQuery):

    def all_users(self):
        return self.all()

class User(db.Document):
    query_class = UserQuery
    Name = db.StringField()
    Role = db.StringField()