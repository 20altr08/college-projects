from flask import Flask, render_template, Blueprint, request, redirect, url_for, session
# from .models import Team, Fixtures, Results
from datetime import datetime
from datetime import date, time
from . import db, create_app

main = Blueprint('main', __name__)

@main.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@main.route('/')
def home():
    return render_template('home.html')

