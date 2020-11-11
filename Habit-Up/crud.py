from model import db, User, Habit, Type, Difficulty, connect_to_db

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



def create_habit(user_id, timestamp, habit_name, habit_type, frequency, habit_difficulty):
    habit = Habit(
        user_id=user_id,
        timestamp=DateTime.now(), 
        habit_name=habit_name, 
        habit_type=habit_type,
        frequency=frequency,
        habit_difficulty=habit_difficulty)
    
    db.session.add(habit)
    db.session.commit()

# TODO
def update_habit():
    
    pass

# TODO
def delete_habit():
    habit = Habit(
        habit_id=habit_id,
        user_id=user_id,
        timestamp=DateTime.now(), 
        habit_name=habit_name, 
        habit_type=habit_type,
        frequency=frequency,
        habit_difficulty=habit_difficulty)
    db.session.delete(habit)
    db.session.commit()

# TODO
def create_type(habit_type):
    type = Type(habit_type=habit_type)
    db.session.add(type)
    db.session.commit()

# TODO
def update_type():
    pass


def create_difficulty(habit_difficulty):
    difficulty = Difficulty(habit_difficulty=habit_difficulty)
    db.session.add(difficulty)
    db.session.commit()

# TODO
def update_difficulty():
    pass