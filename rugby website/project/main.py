from flask import Flask, render_template, Blueprint
from . import db

main = Blueprint('main', __name__)

@main.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/contact_us')
def contact_us():
    return page_not_found(None)

@main.route('/about_us')
def about_us():
    return page_not_found(None)

@main.route('/fixtures')
def fixtures_page():
    return page_not_found(None)

@main.route('/news')
def News_page():
    return page_not_found(None)

@main.route('/the_team')
def team_page():
    return page_not_found(None)

@main.route('/profile')
def profile():
    return render_template('profile.html')