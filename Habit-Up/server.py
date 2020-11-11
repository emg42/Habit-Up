from flask import (Flask, render_template, redirect, flash, session)

# from model import connect_to_db
import crud
from jinja2 import StrictUndefined

app = Flask(__name__)



# Normally, if you refer to an undefined variable in a Jinja template,
# Jinja silently ignores this. This makes debugging difficult, so we'll
# set an attribute of the Jinja environment that says to make this an
# error.
app.jinja_env.undefined = StrictUndefined



@app.route("/signup", methods=['POST'])
def index():
    """Signup page"""
    
    #TODO get the user id
    #session['user_id'] = 

    return redirect('/login')


app.route("/login")
def login_page():
    """View login page"""

    #TODO get the user id
    #session['user_id'] = 
   
    return render_template('login.html')

app.route("/habits")
def show_habits():
    """View habits"""

    return render_template('habits.html')

if __name__ == '__main__':
    # connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)