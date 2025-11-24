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
    return render_template('about_us.html')

@main.route('/fixtures')
def fixtures_page():
    return page_not_found(None)

@main.route('/news')
def News_page():
    return render_template('news.html')

@main.route('/team')
def team_page():
    return render_template('team.html')

@main.route('/profile')
def profile():
    return render_template('profile.html')