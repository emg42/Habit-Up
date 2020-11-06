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

@app.route("/")
def index():
    """Return homepage."""
    pass
    # return render_template("homepage.html")