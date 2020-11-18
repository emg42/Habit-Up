from flask import (Flask, request, render_template, redirect, flash, session)
from twilio.twiml.messaging_response import MessagingResponse
# from model import connect_to_db
import crud
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = 'ABC'



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
    
    #TODO get the user id
    #session['user_id'] = 
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

@app.route("/login", methods=['POST'])
def handle_login():
    """Handle login"""

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


@app.route("/habits")
def show_habits():
    """View habits"""
    user_id = session['user_id']
    
    habits = crud.get_habits_by_user_id(user_id)
    

    return render_template('habits.html', habits=habits)

    
@app.route("/edit-habit/<habit_id>")
def show_edit_habit(habit_id):
    """Display edit habit form"""
    user_id = session['user_id']
    
    habit = crud.get_habit_by_habit_id(user_id, habit_id)

    habit_name = habit.__dict__['habit_name']
  
    if "habit_id" not in session:
        session["habit_id"] = habit.habit_id
    else:
        active_habit = session.get("habit_id")
   

    return render_template("edit-habit.html", habit_name=habit_name, habit=habit)  

@app.route("/edit-habit/<habit_id>", methods=['POST'])
def edit_habit(habit_id):
    """Edit habit"""

    user_id = session['user_id']

    habit_name = request.form.get('habit-name')
   
    habit_id = request.form.get('habit-id')
    habit_difficulty = request.form.get('difficulty')
    habit_type = request.form.get('type')

    crud.update_habit(habit_id, user_id, habit_name, habit_difficulty, habit_type)

    return redirect("/habits")



@app.route("/delete-habit/<habit_id>", methods=['POST'])
def delete_habit():   
    """delete a habit"""

    
    return redirect('/habits')

@app.route("/edit-frequency", methods=['POST'])
def edit_frequency():
    """Update frequency"""
    is_checked = request.form.get('completed-habit').checked
    habit = get_habit_by_habit_id(habit_id)
    if is_checked:
        habit.frequency += 1


if __name__ == '__main__':
    # connect_to_db(app)
    crud.connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)