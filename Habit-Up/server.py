from flask import (Flask, request, render_template, redirect, flash, session)

# from model import connect_to_db
import crud
from jinja2 import StrictUndefined

app = Flask(__name__)



# Normally, if you refer to an undefined variable in a Jinja template,
# Jinja silently ignores this. This makes debugging difficult, so we'll
# set an attribute of the Jinja environment that says to make this an
# error.
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def index():
    """View sign up page"""
    
    #TODO create home.html
    return render_template('base.html')

@app.route('/signup')
def show_signup():
    """View sign up page"""
    
    return render_template('signup.html')

@app.route("/signup", methods=['POST'])
def signup_user():
    """Sign up a user"""
    
    #TODO get the user id
    #session['user_id'] = 
    lname = request.form.get('last-name')
    fname = request.form.get('first-name')
    email = request.form.get('email')
    password = request.form.get('password')
    password2 = request.form.get('password2')
    phone = request.form.get('phone')
    print("HHHHHHHHHHHHHHHHHIIIIIIIIIIIIIIIIIIIIII" + email)
    # if password = password2:
    # else:
    #     alert("This is not a valid password")
    user = crud.get_user_by_email(email)

    """Check to see if user is already in database"""
    if user:
        flash("This email already exists. Try again")
    else:
        crud.create_user(fname, lname, email, password, phone_number)
        flash("Your account was created successfully")


    return render_template('login.html')



@app.route("/login")
def login_page():
    """Login a user"""

    #TODO get the user id
    #session['user_id'] = 
    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.check_user_login_info(email, password)

    if "user_id" not in session:
        session["user_id"] = user.user_id
    else:
        active_user = session.get("user_id")

    if user:
        flash("Successful login")
    else:
        flash("Login info incorrect, please try again")
    
    
    return redirect('/habits')

@app.route("/habits")
def show_habits():
    """View habits"""

    return render_template('habits.html')

if __name__ == '__main__':
    # connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)