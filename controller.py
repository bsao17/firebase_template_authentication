import os

import firebase_admin
from flask import Flask, render_template, request, redirect, url_for

from auth import auth
from form import signin_form

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
        auth.sign_in_with_email_and_password(email, password)
        return redirect(url_for('profile'))
    return render_template('login.html', form=form)


@app.route('/profile')
def profile():
    return render_template('profile.html')
