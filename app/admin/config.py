# set your app config here

class Config(object):
    DEBUG = True
    DEVELOPMENT = True
    SECRET_KEY = 'hlky288dnp10eskj'
    # FLASK_HTPASSWD_PATH = '/secret/.htpasswd'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///registration.db'
    STATIC_FOLDER = 'static',
    TEMPLATE_FOLDER = 'templates'
    FLASK_SECRET = SECRET_KEY


class ProductionConfig(Config):
    DEVELOPMENT = False
    DEBUG = False
    SECRET_KEY = 'hlky288dnp10eskj'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///registration.db'
    FLASK_SECRET = SECRET_KEY
    STATIC_FOLDER = 'static',
    TEMPLATE_FOLDER = 'templates'
