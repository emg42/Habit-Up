from model import db, User, Habit, Collection_user_habit, connect_to_db

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



def create_habit(timestamp, habit_name, habit_type, habit_type)
    habit = Habit(timestamp=timestamp, 
                habit_name=habit_name, 
                habit_type=habit_type,
                habit_type=habit_type
                )
    
    db.session.add(habit)
    db.session.commit()