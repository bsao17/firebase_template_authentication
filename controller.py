import os


from flask import Flask, render_template, request, redirect, url_for


from auth import auth
from decorators import required_login
from form import Signin_form, Signup_form

app = Flask(__name__)
app.secret_key = os.urandom(16)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = Signin_form()
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = auth.sign_in_with_email_and_password(email, password)
        verified_email = auth.get_account_info()
        return render_template('profile.html', user=user)
    return render_template('login.html', form=form)


@app.route("/signup", methods=["GET", "POST"])
def signup():
    form = Signup_form()
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        user = auth.create_user_with_email_and_password(email, password)
        return redirect(url_for('login', user=user))
    return render_template('signup.html', form=form)


@app.route('/profile')
@required_login
def profile():
    return render_template('profile.html')


@app.route('/login/google')
def login_google():
    pass