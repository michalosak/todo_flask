from main import db


class Todos(db.Model):

    __tablename__ = "todo_items"
    ID = db.Column(db.Integer, primary_key=True)
    item_title = db.Column(db.String, nullable=False)
    status = db.Column(db.String, nullable=False)

    def __init__(self, title, status = 0):
        self.item_title = title
        self.status = status

    def __repr__(self):
        return 'title{}'.format(self.item_title)
