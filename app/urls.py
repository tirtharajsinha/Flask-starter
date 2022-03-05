import views
from admin import auth
# config your urls here


def add_url(app):
    app.add_url_rule('/', view_func=views.index, methods=['GET', 'POST'])
    app.add_url_rule('/adminlogin', view_func=auth.adminlogin,
                     methods=['GET', 'POST'])
    app.add_url_rule('/logout', view_func=auth.logout,
                     methods=['GET', 'POST'])

    return app
