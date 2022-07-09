import functools

from flask import session, redirect, url_for


def login_required(f):
    """If you decorate view with this, it will ensure that the current user 
    has been logged in."""
    @functools.wraps(f)
    def decorator(*args, **kwargs):
        if session.get("user", None) is None:
            return redirect(url_for("main.index"))
        return f(*args, **kwargs)
    return decorator
