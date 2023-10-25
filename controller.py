import os

import firebase_admin.auth
from flask import Flask, render_template, request, redirect, url_for

from auth import auth, serverless
from form import signin_form
from decorators import required_login

app = Flask(__name__)
app.secret_key = os.urandom(16)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = signin_form()
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        con = auth.sign_in_with_email_and_password(email, password)
        user = firebase_admin.auth.get_user(con['localId'])
        authorization = firebase_admin.auth.verify_id_token(con['idToken'])
        return render_template('profile.html', display_name=user.email, authorization=con['idToken'])
    return render_template('login.html', form=form)


@app.route('/profile')
@required_login
def profile():
    return render_template('profile.html')
