from datetime import date
from email.policy import default
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

# create your db model here

db = SQLAlchemy()


class User(UserMixin, db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    firstname = db.Column(db.String(100), nullable=True)
    email = db.Column(db.String(100), nullable=True, unique=True)
    lastname = db.Column(db.String(100), nullable=True)
    joined = db.Column(db.String(100), nullable=False)
    permission = db.Column(db.String(100), nullable=False,
                           default="user")  # value=admin for superuser

    def get_id(self):
        return self.username


class admin_history(UserMixin, db.Model):
    __tablename__ = 'admin_history'
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(100), nullable=False)
    table = db.Column(db.String(100), nullable=False)
    event = db.Column(db.String(100), nullable=False)
    row_id = user = db.Column(db.String(100), nullable=False)
    time = db.Column(db.String(100), nullable=False)


class dummy(UserMixin, db.Model):
    __tablename__ = 'dummy'
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(100), nullable=False)


# to create migration run in terminal $ flask db init
# to migrate run in terminal $ flask db migrate
# to upgade  run in terminal $ flask db upgrade
