# Flask Starter app

> Flask starter template for better structuring.

# DOCS


## step 1 : cloning this repo through git

> 1. clone the repo 
```
git clone https://github.com/tirtharajsinha/Flask-starter.git

```
>  2. if youremove the .git folder. remember that .git folder is a hidden folder. you can do it either manually in the file explorer or from the comand line

For windows use-
```
rmdir /s .git

```
for  linux
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

## step 2 : download the code directly from github

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


## Function of each controller files.

1. <b>urls.py</b> : Direct all the url requests to the assigned functions.

2. <b>views.py</b> : Contains all view functions, or view for short, that takes a web request and returns a web response.

3. <b>app.py</b> : Manage flask settings.

4. <b>Model.py</b> : Stores models. A model is a class that represents table or collection in our DB, and where every attribute of the class is a field of the table or collection.

5. <b>Manage.py</b> : It is a controller of app to perform configuere tasks like starting server, superuser creation, migrate database etc. Run ```python manage.py --help``` for more info.

6. <b>backup_tools.py</b> : A tool to backup your database or port your data to one database to other database. you can backup form remote database to local sqlite file or vice versa. to use it correctly configuere it properly. Use it if know what you are doing. using it wrong can wipe your data completely or corrupt your files. Distribute it with caution cuz it may contains security access details of your database.  

7. <b>admin/config.py</b> : Contains runtime config profiles.

8. <b>admin/auth.py</b> : Contains authentication and authorization rules for users like login, logout, isuser etc.

9. <b>admin/adminconsole.py</b> : Contains settings for admin dashboard. To see your model in the ```/admin/``` page register the model here. Follow the docs in the following file to know how to register a model. 




<h1 style="text-align:center;">Now you are ready to go</h1>

<p align="center">
  <img width="460" src="https://media.giphy.com/media/SJjWgVgBhkNhJ29Ins/giphy.gif">
</p>