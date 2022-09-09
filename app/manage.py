from models import Userdata
from datetime import date
import sys
import os


operations = ["createsuperuser", "makemigrations",
              "migrate", "runserver", "-h", "--help", "init", "backup-db"]


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

                getuser = Userdata.query.filter_by(username=username).first()
                if getuser:
                    print("username or email already registered.")
                    return False

                new_user = Userdata(
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


def migrate_init():
    try:
        os.system('flask db init')
    except:
        print("makemigrations failed.")


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


def backup_db():
    try:
        os.system('python backup_tool.py')
    except Exception as e:
        print("ERROR OCCURED !!!!! \n"+str(e))


def runserver():
    try:
        os.system('python app.py')
    except:
        print("flask app stopped successfully")


def flaskhelp():
    desp = """
    positional arguments:
    init             initialize the db migrations(run only for first time).
    createsuperuser  create admin user.
    makemigrations   finds possible migrations.
    migrate          migrate the database.
    runserver        Run the flask app.
    backup-db        Backup database.(update backup-tool.py file for configuration)

    optional arguments:
    -h, --help       show this help message and exit
    """

    print(desp)


if len(sys.argv)<2:
    flaskhelp()
elif sys.argv[1] == operations[0]:
    createsuperuser()
elif sys.argv[1] == operations[6]:
    migrate_init()
elif sys.argv[1] == operations[1]:
    makemigrations()
elif sys.argv[1] == operations[2]:
    migrate()
elif sys.argv[1] == operations[3]:
    runserver()
elif sys.argv[1] == operations[7]:
    backup_db()
else:
    flaskhelp()
