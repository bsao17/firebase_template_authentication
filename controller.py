import os
import firebase_admin.auth
from flask import Flask, render_template, request
from auth import auth, serverless
from form import Signin_form
from decorators import required_login

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
        con = auth.sign_in_with_email_and_password(email, password)
        user = firebase_admin.auth.get_user(con['localId'])
        authorization = con['idToken']
        return render_template('profile.html', display_name=user.email, authorization=authorization)
    return render_template('login.html', form=form)


@app.route('/profile')
@required_login
def profile():
    return render_template('profile.html')
