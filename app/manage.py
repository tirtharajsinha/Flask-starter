from models import User
from datetime import date
import sys
import os

operations = ["createsuperuser", "makemigrations",
              "migrate", "runserver", "-h", "--help"]


def createsuperuser():
    from app import db, app

    try:
        username = input("Enter Username : ")
        password = input("Enter password : ")
        perm = input("Are your want to continue [Y/n]: ")
        with app.app_context():
            if(perm.lower() != "n"):
                email = ""
                firstname = ""
                lastname = ""
                today = date.today()
                joined = today.strftime("%b-%d-%Y")

                getuser = User.query.filter_by(username=username).first()
                if getuser:
                    print("username or email already registered.")
                    return False

                new_user = User(
                    email=email,
                    username=username,
                    password=password,
                    firstname=firstname,
                    lastname=lastname,
                    joined=joined,
                    permission="admin",
                )

                db.session.add(new_user)
                db.session.commit()
                print(
                    "Superuser created succufully.\n don't forget your username and password.")

    except Exception as e:
        print(e)


def makemigrations():
    try:
        os.system('flask db migrate')
    except:
        print("makemigrations failed.")


def migrate():
    try:
        os.system('flask db upgrade')
    except:
        print("migration failed.")


def runserver():
    try:
        os.system('python app.py')
    except:
        print("flask app stopped successfully")


def flaskhelp():
    desp = """
    positional arguments:
    createsuperuser  create admin user
    makemigrations   finds possible migrations.
    migrate          migrate the database.
    runserver        Run the flask app.

    optional arguments:
    -h, --help       show this help message and exit
    """

    print(desp)


if sys.argv[1] == operations[0]:
    createsuperuser()
elif sys.argv[1] == operations[1]:
    makemigrations()
elif sys.argv[1] == operations[2]:
    migrate()
elif sys.argv[1] == operations[3]:
    runserver()
elif sys.argv[1] == operations[4]:
    flaskhelp()
else:
    flaskhelp()
