import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system('dropdb habitupdb')
os.system('createdb habitupdb')

model.connect_to_db(server.app)
model.db.create_all()

with open('data/fakeUsers.json') as f:
    user_data = json.loads(f.read())


users_in_db = []

for user in user_data:
    fname = user['firstname']
    lname = user['lastname']
    email = user['email']
    password = user['password']
    phone_number = user['phone']
    
    db_user = crud.create_user(fname, lname, email, password, phone_number)
    users_in_db.append(db_user)

habits_in_db = []
habit_names_list = ["eat 3 healthy meals a day", "read 30 minutes a day", "meditate 15 minutes", "work out for 30 minutes", "draw for 15 minutes a day"]
habit_difficulties = ["Easy", "Medium", "Hard"]
habit_types = ["Work", "Exercise", "Health & Wellness", "School", "Chores", "Creativity", "General Self Improvement"]

for user in users_in_db:
    user_id = user[user_id]
    timestamp = DateTime.now()
    habit_name = "read a book for 15 minutes"
    habit_type = ""
    frequency = 0
    habit_difficulty = "Easy"

    db_habit = crud.create_habit(user_id, timestamp, habit_name,)
    habits_in_db.append(db_habit)




