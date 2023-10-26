from firebase_admin import auth
from flask import request, redirect, url_for


def required_login(func):
    """
        Decorator function that checks if a user is logged in before executing the decorated function.

        Args:
            func (function): The function to be decorated.

        Returns:
            function: The decorated function.
    """

    def wrapper(*args, **kwargs):
        """
        This function is a wrapper that performs authentication before executing the provided function.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            The return value of the provided function if the authentication is successful, otherwise redirects to the login page.
        """
        if auth.get_user_by_email(request.form['email']):
            return func(*args, **kwargs)
        else:
            return redirect(url_for('login'))

    return wrapper
