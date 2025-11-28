from flask import Flask, render_template, Blueprint, request
from .models import Team, Fixtures, Results
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

@main.route('/contact_us')
def contact_us():
    return render_template('contact_us.html')

@main.route('/about_us')
def about_us():
    return render_template('about_us.html')

@main.route('/results')
def results():
    return render_template('results.html')

@main.route('/fixtures')
def fixtures_page():
    fixtures = Fixtures.query.order_by(Fixtures.date, Fixtures.time).all()
    return render_template('fixtures.html', fixtures=fixtures)

@main.route('/news')
def News_page():
    return render_template('news.html')

@main.route('/team')
def team_page():
    return render_template('team.html')

@main.route('/archive')
def archive():
    return render_template('archive.html')

@main.route('/profile')
def profile():
    return render_template('profile.html')