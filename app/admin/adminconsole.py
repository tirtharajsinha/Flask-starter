from models import db, User
from flask_admin import Admin, BaseView, expose, Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask import Flask, redirect, render_template
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, current_user
import urls


class MyView(AdminIndexView):
    @expose("/")
    def index(self):
        return self.render("admin/admin_base.html", user=current_user)

    def is_accessible(self):
        perm = current_user.is_authenticated and current_user.is_active
        return perm

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect("/adminlogin?next=admin")


class PublicationModelView(ModelView):
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
        return redirect("/login")

    def _description_formatter(view, context, model, name):
        return model.desc[:30]

    def _image_formatter(view, context, model, name):
        return model.image[:30]

    def _icon_formatter(view, context, model, name):
        return model.icon[:30]
    column_formatters = {
        'desc': _description_formatter,
        'image': _image_formatter,
        'icon': _icon_formatter
    }


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
        return redirect("/login")


# setting up admin panel
def get_admin(app):
    admin = Admin(
        app,
        name="admin panel",
        index_view=MyView(
            name="Home",
            menu_icon_type="glyph",
            menu_icon_value="glyphicon-home",
            url="/admin",
        )
    )
    admin = add_adminview(admin)

    return admin


def add_adminview(admin):
    admin.add_view(MicroBlogModelView(User, db.session))
    return admin
