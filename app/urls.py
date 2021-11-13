import views

# config your urls here


def add_url(app):
    app.add_url_rule('/', view_func=views.index, methods=['GET', 'POST'])

    return app
