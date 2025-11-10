# from flask import Flask, render_template, request, redirect, url_for, flash, Blueprint
# import flask_login
# from flask_sqlalchemy import SQLAlchemy
#
# @main.errorhandler(404)
# def page_not_found():
#     return render_template("404.html"), 404
#
#
# @main.route('/')
# def home():
#     return render_template('home.html')
#
#
# @main.route('/contact_us')
# def contact_us():
#     # return render_template('contact_us.html')
#     return page_not_found()
#
#
# @main.route('/for_tutors')
# def for_tutors():
#     # return render_template('for_tutor.html')
#     return page_not_found()
#
#
# @main.route('/pricing')
# def pricing():
#     # return render_template('pricing.html')
#     return page_not_found()
#
# @main.route('/sign_in')
# def sign_in():
#  return render_template('sign_in.html')
#
# if __name__ == "__main__":
#     main.run(debug=True)