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



def get_users():
    """Return all users."""

    return User.query.all()

def get_user_by_email(email):
    """Return a user by email."""

    return User.query.filter(User.email == email).first()

def get_user_by_id(user_id):
    """Return a user by primary key."""

    return User.query.get(user_id)


# TODO Complete create habit function
def create_habit(timestamp, habit_name, habit_type):
    habit = Habit(timestamp=timestamp, 
    habit_name=habit_name, 
    habit_type=habit_type)
    
    db.session.add(habit)
    db.session.commit()

# TODO
def update_habit():
    pass

# TODO
def delete_habit():
    pass
    

def create_type(habit_type):
    type = Type(habit_type=habit_type)
    db.session.add(type)
    db.session.commit()

def create_difficulty(habit_difficulty):
    difficulty = Difficulty(habit_difficulty=habit_difficulty)
    db.session.add(difficulty)