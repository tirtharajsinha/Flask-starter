# Flask Starter app

> Flask starter template for better structuring.

### What is Flask?
Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries. It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions.

### Why flask-starter?
Unlike django this does not have starter pack and developers have to write each and everything to start with flask. This can get pretty much boring. Same for me.


It pushed me to make a flask starter pack to solve the problem. In usual manner flask app are developed as single file app. But as application gets bigger it starts to look clutterd. It gets very herd to manage all the configs, views, models etc from a single file.  May be it doesn't make sense when project is smalled but when project gets expanded we realize that how importent is to scale the project. It enable the freedom of flask with scalability of django like stuff made in heaven. 

#### Advantages of flask-starter
- *Pre-configured* to use 
- Suitable for big applications.
- *Full-Stack* experience.
- *Admin site* with ***Flask-admin***
- *login or authentication* with ***flask-login***
- *ORM features* with ***FLASK-SQLAlchemy***
- *DB Migrations* with ***Flask-Migrate***

<hr>

# Getting started
## Step 1 : cloning this repo through git

> 1. clone the repo

```
git clone https://github.com/tirtharajsinha/Flask-starter.git

```

> 2.  if youremove the .git folder. remember that .git folder is a hidden folder. you can do it either manually in the file explorer or from the comand line

For windows use-

```
rmdir /s .git

```

for linux

```
rm -r .git
```

> 3. initalize a new git repo (in cvase you want to make it a new git repo)

```
git init
echo "# New flask App" > README.md
git add -A
git commit -m "good first commit"
```

> 4. if you want to connect a remote repo

```
git remote add origin [newGithubURL]
git push origin master
```

> 5. [create](#set-up-a-virtual-environmentrecommended) a virtual environment and install requirements.(Recommended)

### OR download the code directly from github

> 1. if you want to download the repository | [click here](https://github.com/tirtharajsinha/Flask-starter/archive/refs/heads/main.zip).<br>
> 2. Unzip it and start building your app.<br>
> 3. [create](#set-up-a-virtual-environmentrecommended) a virtual environment and install requirements.(recommended)

<br>

## Set up a Virtual Environment(optional)

> install virtualenv and enable it and install requirements .

```
virtualenv venv
./venv/Scripts/activate
pip install -r requirements.txt
```

> Deactivate venv

```
deactivate
```

## Step 2 - Run application for the first time.
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

Open Your web Browser and put ```http://127.0.0.1:5000``` and press enter you should show see a welcome screen.

### To Know more run 
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
Put your static files like images,audio,css,js files in it to use it in html files. suppose you have css file named ```style.css``` or ```img.jpg```. import it in html as 
```
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
<img src="{{ url_for('static', filename='img.jpg') }}">
```
## Configuere database
if you are using oracle, postgresql, Mysql you must have DB URI Or by default we use SqLite.

Set up your database in ```app.py``` file and replace your URL with default one. 
```
app.config["SQLALCHEMY_DATABASE_URI"] = "<YOUR-DATABASE-URI>"
```

## Create and register new Model 
Create model in ```models.py``` suppose your database name is ***PROJECT*** then create a class called *project* and add all the attribute for more details follow Flask-SQLALchemy [Docs](https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/quickstart/#define-models).

After creating or altering anything in model.py you have to run
```
python manage.py makemigrations
python manage.py migrate
```

Now you have to register the model in ```admin/adminconsole.py```.

- Import your model
```
from models import project
``` 
- Register your model in ```add_adminview``` function in line before return statement.
```
admin.add_view(DBModelView(project, db.session))
```

## Create new SuperUser
```
python manage.py createsuperuser
```

## Create new view
Put your views in ```views.py``` file. 

## Add new url to *urls.py*
urls.py contains instruction how flask have to response on perticular request. Python functions in views.py take the web request from urls.py and give the web response to templates.
To register new url to your application and bind it with a view add a like like this in ```add_url``` functions before return function.
```
app.add_url_rule('/<YOUR-PATH>', view_func=views.<YOUR-VIEW>,methods=['GET', 'POST'])
```
- Replace <YOUR-PATH> with the url path you want to bind your view.
- Replace <YOUR-VIEW> with your view form views.py 

