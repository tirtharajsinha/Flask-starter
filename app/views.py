from flask import render_template, request
from models import db
import os
from datetime import date
import warnings

warnings.filterwarnings("ignore")

# put your views here.


def index():
    if request.method == "POST":
        return "got a post request"

    return render_template("index.html")
