import views
from admin import auth
from flask import Flask, redirect
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, current_user
from models import *
import urls
from flask_migrate import Migrate
from flask_admin import Admin, BaseView, expose, Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView


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


class MyView(AdminIndexView):
    @expose("/")
    def index(self):
        return self.render("admin/admin_base.html", user=current_user)

    def is_accessible(self):
        perm = current_user.is_authenticated and current_user.is_active
        return perm

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect("/adminlogin")


class MicroBlogModelView(ModelView):
    create_template = "admin/microblog_create.html"
    edit_template = "admin/microblog_edit.html"

    def is_accessible(self):
        perm = (
            current_user.is_authenticated
            and current_user.permission == "admin"
            and current_user.is_active
        )
        return perm

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect("/adminlogin")


# setting up admin panel
admin = Admin(
    app,
    name="admin panel",
    index_view=MyView(
        name="admin panel",
        menu_icon_type="glyph",
        menu_icon_value="glyphicon-home",
        url="/admin",
    ),

)

admin.add_view(MicroBlogModelView(User, db.session))

#######################


# urls
app = urls.add_url(app)


# authentication and authorization
login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)


@login_manager.user_loader
def load_user(get_id):
    return User.query.filter_by(username=get_id).first()


if __name__ == "__main__":
    app.run(debug=True)


# this is a custom template from Tirtharaj Sinha (https://github.com/tirtharajsinha/Flask-starter.git)
