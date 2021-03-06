"""Models for habit tracker app."""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
# import crud

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

   

    def __repr__(self):

        return f'<User user_id={self.user_id} fname={self.fname} lname={self.lname} email={self.email} password={self.password} phone_number={self.phone_number}>'
                


class Habit(db.Model):
    """A Habit"""

    __tablename__ = 'habits'

    habit_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    habit_name = db.Column(db.String(50), nullable=False)
    habit_type = db.Column(db.String(30), nullable=False)
    frequency = db.Column(db.Integer, default=0)
    habit_difficulty = db.Column(db.String(30), nullable=False)
    is_checked = db.Column(db.Boolean, default=False)
   
    user = db.relationship("User", backref="habits")
    def __repr__(self):
        return f'<Habit user_id={self.user_id} habit_id={self.habit_id} timestamp={self.timestamp} habit_name={self.habit_name} habit_type={self.habit_type} frequency={self.frequency} habit_difficulty={self.habit_difficulty} is_checked={self.is_checked}>'

            
   

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