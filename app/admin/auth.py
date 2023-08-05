from flask import render_template, request, redirect, send_from_directory, flash
import datetime

# from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from models import User
import os
from datetime import date
import warnings


def authenticate(username, password):
    from app import db

    user = User.query.filter_by(username=username).first()
    if not user:
        return None
    if user.password != password:
        return None
    return user


def login():
    from app import db

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = User.query.filter_by(username=username).first()
        if not user:
            flash("User not found.")
            return redirect("/login")
        print(user.id)
        if user.password != password:
            flash("username or password is incorrect.")
            return redirect("/login")
        print(user.role)
        if user.role != "admin":
            flash("User has not admin role.")
            return redirect("/login")
        rem = False
        login_user(user, remember=rem)
        page = request.args.get("next")
        flash("Successfully logged in.")
        if page != "" and page != None:
            return redirect(page)
        return redirect("/admin")

    return render_template("admin/login.html")


def logout():
    if current_user.is_anonymous:
        flash("You are not logged in.")
        return redirect("/")
    logout_user()
    flash("You are successfully Logged out! See you later.")
    return redirect("/")


def is_user():
    if current_user.is_anonymous:
        return None
    else:
        return current_user
