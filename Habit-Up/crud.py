from model import db, User, Habit, connect_to_db

from datetime import datetime

def create_user(fname,lname, email, password, phone_number):
    """Create and return a new user."""

    user = User(fname=fname, 
                lname=lname, 
                email=email, 
                password=password,
                phone_number=phone_number)

    db.session.add(user)
    db.session.commit()

    return user

def check_user_login_info(email, password):
    """check if the users email and password match in the database"""

    return User.query.filter((User.email == email) & (User.password == password)).first()

def get_users():
    """Return all users."""

    return User.query.all()

def get_user_by_email(email):
    """Return a user by email."""

    return User.query.filter(User.email == email).first()

def get_user_by_id(user_id):
    """Return a user by primary key."""

    return User.query.get(user_id)



def create_habit(user_id, habit_name, habit_difficulty, habit_type):
    habit = Habit(
        user_id=user_id,
        habit_name=habit_name,
        habit_difficulty=habit_difficulty, 
        habit_type=habit_type)
    
    db.session.add(habit)
    db.session.commit()
    return habit

def get_habits_by_user_id(user_id):
    habits = Habit.query.filter_by(user_id=user_id).order_by(Habit.habit_id.asc()).all()
    
    print(habits)
    return habits

def get_habit_by_habit_id(habit_id):

    habit = Habit.query.get(habit_id)
    print(habit)
    

    return habit

def update_habit(habit_id, user_id, habit_name, habit_difficulty, habit_type):
    habit = get_habit_by_habit_id(habit_id)
    habit.habit_name = habit_name
    habit.habit_difficulty = habit_difficulty
    habit.habit_type = habit_type
    db.session.add(habit)
    db.session.commit()

def delete_habit(habit_id):
    habit = Habit.query.get(habit_id)
    db.session.delete(habit)
    db.session.commit()

def check_habit(habit_id):
    # habit = get_habit_by_habit_id(habit_id)
    habit = Habit.query.get(habit_id)
    print('******************************')
    print(habit)
    print(habit_id)
    habit.is_checked = not habit.is_checked
    db.session.add(habit)
    db.session.commit()

    return habit