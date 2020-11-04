"""Models for habit tracker app."""

from flask_sqlalchemy import SQLAlchemy

import datetime
db = SQLAlchemy()

class User(db.Model):
    """A User"""

    __tablename__ = 'users'


    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    fname = db.Column(db.String(30), nullable=False)
    lname = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), unique=True)
    password = db.Column(db.String(30), nullable=False)

    # phone_number = db.Column(db.)
class collection_user_habit(db.Model):
    """An intermediate table connecting the users and habits tables"""

    collection_user_habit_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    habit_id = db.Column(db.Integer, db.ForeignKey('habits.habit_id'), nullable=False)

class Habit(db.Model):
    """A Habit"""

    __tablename__ = 'habits'

    habit_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    timestamp = db.Column(db.datetime, nullable=False)
    habit_name = db.Column(db.String(50))
    habit_type = db.Column(db.String(30))
    frequency = db.Column(db.Integer, default=0)
    habit_difficulty = db.Column(db.String(30), nullable=False)


    def __repr__(self):

        return f'<User user_id={self.user_id} fname={self.fname} lname={self.lname} email={self.email} password={self.password}>'



if __name__ == '__main__':
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    
    connect_to_db(app)