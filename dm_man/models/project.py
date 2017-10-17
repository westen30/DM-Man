from ..dm import db
from . import BaseQuery
from .user import User

class ProjectQuery(BaseQuery):

    def all_projects(self):
        return self.all()

class Project(db.Document):
    query_class = ProjectQuery

    Name = db.StringField()
    Owner = db.DocumentField(User)