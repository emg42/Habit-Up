from flask import Flask, render_template, redirect, flash, session

from model import connect_to_db
import crud
from jinja2 import StrictUndefined

app = Flask(__name__)



# Normally, if you refer to an undefined variable in a Jinja template,
# Jinja silently ignores this. This makes debugging difficult, so we'll
# set an attribute of the Jinja environment that says to make this an
# error.
app.jinja_env.undefined = StrictUndefined

@app.route("/signup")
def index():
    """Signup page"""
    
    return render_template('signup.html')

app.route("/users")
def userspage():
    """View all users"""
    users = crud.get_users()

    return render_template('all_users.html', users=users)

app.route("/login")
def login_page():
    """View login page"""

    return render_template('login.html')