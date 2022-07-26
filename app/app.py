import views
from admin import auth, adminconsole
from flask import Flask, redirect
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, current_user
from models import *
import urls
from flask_migrate import Migrate
from flask_admin import Admin, BaseView, expose, Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from models import User

app = Flask(__name__)


# csrf
csrf = CSRFProtect(app)

# config
app.config.from_object("admin.config.Config")

# database connection

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "sqlite:///registration.db"
db.init_app(app)

# setting up flask migrate
migrate = Migrate(app, db)


#######################


# urls
app = urls.add_url(app)


# Loading the admin panel
admin = adminconsole.get_admin(app)


# authentication and authorization
login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)


@login_manager.user_loader
def load_user(get_id):
    return User.query.filter_by(username=get_id).first()


# @app.cli.command("create-superuser")
# def create_superuser():
#     username = input("Enter username: ")
#     password = input("Enter password: ")
#     email = input("Enter email: ")

#     newsuper = User(
#         username=username,
#         password=password
#         firstname=""
#         email=email
#         lastname=""
#         joined="00/00/00"
#         permission="admin"
#     )

#     db.session.add(newsuper)
#     db.session.commit()


if __name__ == "__main__":
    app.run(debug=True)


# this is a custom template from Tirtharaj Sinha (https://github.com/tirtharajsinha/Flask-starter.git)
