"""Models for habit tracker app."""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import crud

db = SQLAlchemy()

class User(db.Model):
    """A User"""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    fname = db.Column(db.String(30), nullable=False)
    lname = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), unique=True)
    password = db.Column(db.String(30), nullable=False)
    phone_number = db.Column(db.String(15))

    #habits = db.relationship("Habit", backref="users")

    def __repr__(self):

        return f'<User user_id={self.user_id} fname={self.fname} lname={self.lname} email={self.email} password={self.password} phone_number={self.phone_number}>'
                


class Habit(db.Model):
    """A Habit"""

    __tablename__ = 'habits'

    habit_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    timestamp = db.Column(db.DateTime, nullable=False)
    habit_name = db.Column(db.String(50))
    habit_type = db.Column(db.String(30), db.ForeignKey('types.habit_type'))
    frequency = db.Column(db.Integer, default=0)
    habit_difficulty = db.Column(db.String(30), db.ForeignKey('difficulties.habit_difficulty'), nullable=False)

    #relationship("Address", backref="user")
    types = db.relationship("Type", backref='habits')
    difficulties = db.relationship("Difficulty", backref='habits')    
    user = db.relationship("User", backref="habits")
    def __repr__(self):
        return f'<Habit habit_id={self.habit_id} timestamp={self.timestamp} habit_name={self.habit_name} habit_type={self.habit_type} frequency={self.frequency} habit_difficulty={self.habit_difficulty}>'

            

class Type(db.Model):
    """A Habit Type"""
    __tablename__ = 'types'

    habit_type = db.Column(db.String(10), primary_key=True)

    # habits = db.relationship("Habit", backref="types")
    def __repr__(self):
        return '<Type habit_type={self.habit_type}>'
    
   

class Difficulty(db.Model):
    """A Habit Difficulty"""
    __tablename__ = 'difficulties'
    
    habit_difficulty = db.Column(db.String(10), primary_key=True, nullable=False)

    # habits = db.relationship("Habit", backref="difficulties")
    def __repr__(self):
        return f'<Difficulty habit_difficulty={self.habit_difficulty}>'

   

def connect_to_db(flask_app, db_uri='postgresql:///habitupdb', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')

if __name__ == '__main__':
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)