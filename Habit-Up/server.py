from flask import (Flask, request, render_template, redirect, flash, session, jsonify)
from twilio.twiml.messaging_response import MessagingResponse

import crud
from jinja2 import StrictUndefined
from flask_moment import Moment

app = Flask(__name__)
app.secret_key = 'ABC'
moment = Moment(app)


# Normally, if you refer to an undefined variable in a Jinja template,
# Jinja silently ignores this. This makes debugging difficult, so we'll
# set an attribute of the Jinja environment that says to make this an
# error.
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def index():
    """View sign up page"""
    
    return render_template('homepage.html')



@app.route('/signup')
def show_signup():
    """View sign up page"""
    
    return render_template('signup.html')

@app.route("/signup", methods=['POST'])
def signup_user():
    """Sign up a user"""
    
    lname = request.form.get('last-name')
    fname = request.form.get('first-name')
    email = request.form.get('email')
    password = request.form.get('password')
    password2 = request.form.get('password2')
    phone_number = request.form.get('phone')
   
    if password == password2:
        flash("Your passwords match!")
    else:
        flash("Re-enter your passwords so that they match")
    user = crud.get_user_by_email(email)

    """Check to see if user is already in database"""
    if user:
        flash("This email already exists. Try again")
    else:
        crud.create_user(fname, lname, email, password, phone_number)
        flash("Your account was created successfully")


    return redirect('/login')

@app.route("/login")
def show_login():
    """Show login"""

    return render_template('login.html')

@app.route("/logout", methods=['POST'])
def logout():
    """logout user"""
    session.pop('user_id', None)

    return redirect('/')

@app.route("/login", methods=['POST'])
def handle_login():
    """Handle login"""

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

@app.route("/add-habit")
def show_add_habit():
    """show add habit page"""
    user_id = session['user_id']

    return render_template('add-habit.html')


@app.route("/add-habit", methods=['POST'])
def add_habit():
    """Add a habit"""
    user_id = session.get("user_id")

    habit_name = request.form.get('habit-name')
    
    habit_difficulty = request.form.get('difficulty')
    habit_type = request.form.get('type')

    crud.create_habit(user_id, habit_name, habit_difficulty, habit_type )
   
    return redirect('/habits')

@app.route("/start-day")
def change_is_checked():
    """Change is_checked to False for the start of a new day """
    user_id = session['user_id']
    
    habits = crud.get_habits_by_user_id(user_id)
    for habit in habits:
        crud.start_day(habit.habit_id)

    return redirect("/habits")   

@app.route("/habits")
def show_habits():
    """View habits"""
    user_id = session['user_id']
 
    habits = crud.get_habits_by_user_id(user_id)
    
    # check = crud.check_habit(habit_id)

    return render_template('habits.html', habits=habits)

@app.route("/habits/<habit_id>", methods=['POST'])
def check_habit_id(habit_id):
    
    is_habit_checked = request.form.get('completed-habit')
    
    crud.check_habit(habit_id)

    return redirect('/habits')
 
@app.route("/edit-habit/<habit_id>")
def show_edit_habit(habit_id):
    """Display edit habit form"""
    user_id = session['user_id']
    print('*******************')
    print(habit_id)
    habit_id = int(habit_id)
    
    habit = crud.get_habit_by_habit_id(habit_id)

    habit_name = habit.__dict__['habit_name']

    return render_template("edit-habit.html", habit_name=habit_name, habit=habit)  

@app.route("/edit-habit/<habit_id>", methods=['POST'])
def edit_habit(habit_id):
    """Edit habit"""

    user_id = session['user_id']
    habit_name = request.form.get('habit-name')
    
    habit_difficulty = request.form.get('difficulty')
    habit_type = request.form.get('type')
    
    crud.update_habit(habit_id, user_id, habit_name, habit_difficulty, habit_type)

    return redirect("/habits")



@app.route("/delete-habit/<habit_id>", methods=['POST'])
def delete_habit(habit_id):   
    """delete a habit"""
    crud.delete_habit(habit_id)
   
    return redirect('/habits')


@app.route("/OUR_ROUTE")
def stuff():

    stuff = session["user_id"]
    
    return jsonify(stuff)

if __name__ == '__main__':
   
    crud.connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)