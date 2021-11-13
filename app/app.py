import views
from flask import Flask
from flask_wtf.csrf import CSRFProtect
from models import db
import config
import urls

app = Flask(__name__)


# csrf
csrf = CSRFProtect(app)

# config
app.config.from_object('config.Config')

# database connection
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///registration.db'
db.init_app(app)


#######################


# urls
app = urls.add_url(app)


if __name__ == "__main__":

    try:
        with app.app_context():
            db.create_all()
    except Exception as e:
        print(e)
    app.run(debug=True)
