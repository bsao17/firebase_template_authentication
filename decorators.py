from firebase_admin import auth
from flask import request, redirect, url_for


def required_login(func):
    def wrapper(*args, **kwargs):

        if auth.verify_id_token(request.cookies.get('token')):
            return func(*args, **kwargs)
        else:
            return redirect(url_for('login'))

    return wrapper
