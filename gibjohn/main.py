from flask import Flask, render_template

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found():
    return render_template("404.html"), 404


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/contact_us')
def contact_us():
    # return render_template('contact_us.html')
    return page_not_found()


@app.route('/for_tutors')
def for_tutors():
    # return render_template('for_tutor.html')
    return page_not_found()


@app.route('/pricing')
def pricing():
    # return render_template('pricing.html')
    return page_not_found()

@app.route('/sign_in')
def sign_in():
 return render_template('sign_in.html')

if __name__ == "__main__":
    app.run(debug=True)