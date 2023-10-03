# Flask Starter app

Flask starter template for better structuring and fast programming.

<p align="center">
  <img src="https://i.postimg.cc/xqr8Nmtn/flask.png" height="200px">
</p>

### What is Flask?

Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries. It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions.

### Why flask-starter?

Unlike django this does not have starter pack and developers have to write each and everything to start with flask. This can get pretty much boring. Same for me.

It pushed me to make a flask starter pack to solve the problem. In usual manner flask app are developed as single file app. But as application gets bigger it starts to look clutterd. It gets very herd to manage all the configs, views, models etc from a single file. May be it doesn't make sense when project is small but when project gets expanded we realize that how importent is to scale the project. It enables the freedom of flask with scalability of django. like stuff made in heaven.

#### Advantages of flask-starter

- _Pre-configured_ to use
- Suitable for big applications.
- _Full-Stack_ experience.
- _Admin Dashboard_ with **_Flask-admin_**
- _login or authentication_ with **_flask-login_**
- _ORM features_ with **_FLASK-SQLAlchemy_**
- _DB Migrations_ with **_Flask-Migrate_**

<hr>

# Getting started

## Step 1 : Get the starter app

### Cloning this repo through git

#### 1. clone the repo

```
git clone https://github.com/tirtharajsinha/Flask-starter.git

```

#### 2. if youremove the .git folder. remember that .git folder is a hidden folder. you can do it either manually in the file explorer or from the comand line

For windows use-

```
rmdir /s .git

```

for linux

```
rm -r .git
```

#### 3. initalize a new git repo (in cvase you want to make it a new git repo)

```
git init
echo "# New flask App" > README.md
git add -A
git commit -m "good first commit"
```

#### 4. if you want to connect a remote repo

```
git remote add origin [newGithubURL]
git push origin master
```

#### 5. [create](#set-up-a-virtual-environmentrecommended) a virtual environment and install requirements.(Recommended)

### OR download the code directly from github

> 1. if you want to download the repository | [click here](https://github.com/tirtharajsinha/Flask-starter/archive/refs/heads/main.zip).<br>
> 2. Unzip it and start building your app.<br>
> 3. [create](#set-up-a-virtual-environmentrecommended) a virtual environment and install requirements.(recommended)

<br>

### Set up a Virtual Environment(optional)

#### 1. install virtualenv and enable it and install requirements .

```
virtualenv venv
./venv/Scripts/activate
pip install -r requirements.txt
```

#### Deactivate venv

```
deactivate
```

## Step 2 - Prepare and Run application.

```
python manage.py init
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

From second time only

```
python manage.py runserver
```

If everything go accordingly and does not throw error you are mostly done.

Open Your web Browser and put `http://127.0.0.1:5000` and press enter you should show see a welcome screen.

### To Know about more functionality

```
python manage.py --help
```

#### Now you can carry on your development.

<h1 style="text-align:center;">You are ready to go</h1>

<p align="center">
  <img width="460" src="https://media.giphy.com/media/SJjWgVgBhkNhJ29Ins/giphy.gif">
</p>

<hr>

# DOCS

## Functions of each controller files.

1. <b>urls.py</b> : Direct all the url requests to the assigned functions.

2. <b>views.py</b> : Contains all view functions, or view for short, that takes a web request and returns a web response.

3. <b>app.py</b> : Manage flask settings.

4. <b>Model.py</b> : Stores models. A model is a class that represents table or collection in our DB, and where every attribute of the class is a field of the table or collection.

5. <b>Manage.py</b> : It is a controller of app to perform configuere tasks like starting server, superuser creation, migrate database etc. Run `python manage.py --help` for more info.

6. <b>backup_tools.py</b> : A tool to backup your database or port your data to one database to other database. you can backup form remote database to local sqlite file or vice versa. to use it correctly configuere it properly. Use it if know what you are doing. using it wrong can wipe your data completely or corrupt your files. Distribute it with caution cuz it may contains security access details of your database.

7. <b>admin/config.py</b> : Contains runtime config profiles.

8. <b>admin/auth.py</b> : Contains authentication and authorization rules for users like login, logout, isuser etc.

9. <b>admin/adminconsole.py</b> : Contains settings for admin dashboard. To see your model in the `/admin/` page register the model here. Follow the docs in the following file to know how to register a model.

## Add new Template file(.html)

Put your HTML files in templates and use it in views.

## Add Static files

Put your static files like images,audio,css,js files in it to use it in html files. suppose you have css file named `style.css` or `img.jpg`. import it in html as

```
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
<img src="{{ url_for('static', filename='img.jpg') }}">
```

## Configuere database

if you are using oracle, postgresql, Mysql you must have DB URI Or by default we use SqLite.

Set up your database in `admin/config.py` file and replace your URL with default one.

```
SQLALCHEMY_DATABASE_URI = "<YOUR-DATABASE-URI>"
```

## Create and register new Model

Create model in `models.py` suppose your database name is **_PROJECT_** then create a class called _project_ and add all the attribute for more details follow Flask-SQLALchemy [Docs](https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/quickstart/#define-models).

After creating or altering anything in model.py you have to run

```
python manage.py makemigrations
python manage.py migrate
```

Now you have to register the model in `admin/adminconsole.py`.

- Import your model

```
from models import project
```

- Register your model in `add_adminview` function in line before return statement.

```
admin.add_view(DBModelView(project, db.session))
```

## How to perform Database Operations(Example CRUD)

As we are using **Flask-sqlalchemy** flask-sqlalchemy docs is the best page to refer.

#### To add data in database:

```
from models import *
```

There is your database ready to use. Now to create some users:

```
newuser = User(username='admin', email='admin@example.com')
db.session.add(newuser)
db.session.commit()
```

#### Read the data from database:

```
User.query.all()
>>> [<User u'admin'>, <User u'guest'>]
User.query.filter_by(username='admin').first()
>>> <User u'admin'>
```

#### Update the data from database:

```
ouruser = User.query.filter_by(username='admin').first()
ouruser.email="newemail@example.com"
db.session.commit()

ouruser2 = User.query.get(1)
ouruser2.username = 'New Name'
db.session.commit()
```

#### Delete row from database

```
user = User.query.get(id)
db.session.delete(user)
db.session.commit()

# OR

# Without creating query
User.query.filter_by(id=123).delete()
db.session.commit()
```

#### Execute Raw SQL query

```
allusers = db.engine.execute("select * from users")
```

> Note : Don't ever put `db.create_all()` in your code. It may crash you app on deploy.

## Create new SuperUser

```
python manage.py createsuperuser
```

## Create new view

Put your views in `views.py` file.

## Add Route url to _urls.py_

urls.py contains instruction how flask have to response on perticular request. Python functions in views.py take the web request from urls.py and give the web response to templates.
To register new url to your application and bind it with a view add a like like this in `add_url` functions before return function.

```
app.add_url_rule('/<YOUR-PATH>', view_func=views.<YOUR-VIEW>,methods=['GET', 'POST'])
```

- Replace <YOUR-PATH> with the url path you want to bind your view.
- Replace <YOUR-VIEW> with your view form views.py

## Mail server through Falsk-Mail

> Flask-Mail is configured through the standard Flask config API. These are the available options (each is explained later in the documentation):

1. MAIL_SERVER : Name/IP address of the email server.
2. MAIL_PORT : Port number of server used.
3. MAIL_USE_TLS : Enable/disable Transport Security Layer encryption.
4. MAIL_USE_SSL : Enable/disable Secure Sockets Layer encryption
5. MAIL_DEBUG : Debug support. The default is Flask application’s debug status.
6. MAIL_USERNAME : Username of the sender
7. MAIL_PASSWORD : The password of the corresponding Username of the sender.
8. MAIL_ASCII_ATTACHMENTS : If set to true, attached filenames converted to ASCII.
9. MAIL_DEFAULT_SENDER : sets default sender
10. MAIL_SUPPRESS_SEND : Sending suppressed if app.testing set to true
11. MAIL_MAX_EMAILS : Sets maximum mails to be sent

> Note : Not all of the configuration is to be set.

### SetUp of Mail server

1. Install **Flask-Mail** package using

```
pip install Flask-Mail
pip freeze > requirements.txt
```

2. On `admin/config.py` put you mail server configuration.

```
MAIL_SERVER = "smtp-relay.brevo.com"
MAIL_PORT = 587
MAIL_USERNAME = "<YOUR-Mail-ID>"
MAIL_PASSWORD = "<YOUR-PASSWORD>"
MAIL_USE_TLS = False
MAIL_USE_SSL = False
```

3. Enable mail service in `app.py`

```
import mail as mailConfig
mail,app = mailConfig(app)
```

4. Send mail from your view

```
from flask_mail import Mail, Message
from mail import mail

def send_mail():
  msg = Message(
      '<SUBJECT>',
      sender ='yourId@gmail.com',
      recipients = ['receiver’sid@gmail.com']
  )
  msg.body = f'''Hello Flask message sent from Flask-Mail'''
  mail.send(msg)
  return 'Sent'
```

## Setup a WSGI server insted of development server

```
WARNING: This is a development server. Do not use it in a production deployment.
Use a production WSGI server instead
```

> As of Flask 2.2, the development server always shows this warning, it is not possible to disable it. The development server is not intended for use in production. It is not designed to be particularly efficient, stable, or secure. Use a production WSGI server instead. See the deployment docs from Flask for more information.

> That warning is just a warning though, it's not an error preventing your app from running. If your app isn't working, there's something else wrong with your code.

> That warning applies to the development server, not Flask itself. The Flask framework is appropriate for any type of application and deployment.

Most of the case it is not required still if you want here the step.

```
pip install waitress
```

In `app.py` replace the `__main__` section with this

```
if __name__ == "__main__":
  from waitress import serve
  serve(
    app,
    host=currentAppConfig.host,
    port=currentAppConfig.port
  )
```
