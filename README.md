# Flask Starter app

> Flask starter template for better structuring.


# use the starter plate

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
> 4. if you want to connect a remote git repo
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

# Set up a Virtual Environment(recommended)
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