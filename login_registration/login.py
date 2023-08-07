import sqlite3
from flask import Flask, render_template, request, redirect, url_for

# Create databse of users/passwords
def create_user_table():
    conn = sqlite3.connect("registered_users.db")
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS registered_users (
              id INTEGER PRIMARY KEY,
              username TEXT,
              password TEXT,
              )''')
    
    conn.commit()
    conn.close()

# New register, add to registered_users database
def register_user(username, password):
    conn = sqlite3.connect("registered_users.db")
    c = conn.cursor()

    # Get input username/password, search in database to match, return result

    # if len(password) < 8:
    #     print('Password too short. \nPassword must be 8 chracters or more. ')
    #     return ''   
    # elif username.lower() in database:
    #     print('Username already registered.')
    #     return ''
    # else:
    #     print('Username registered.')
    #     return username
    
    c.execute("INSERT INTO registered_users.db (username, password) VALUES ?,?" (username, password))

    conn.commmit()
    conn.close()
    pass


# Login, check against existing database
def login(database, username, password):
    conn = sqlite3.connect("registered_users.db")
    c = conn.cursor()
    # Get input username, search in database to match, return result


    # if username in database:
    #     if database[username] == password:
    #         print(f'You are logged in as: {username}')
    #         return username - ###Send to index.html
    #     else:
    #         print('Invalid password') ###Send to registration.html
    #         return ''
    # else:
    #     print('Invalid username')
    #     return ''
    
    conn.commmit()
    conn.close()
    pass


   
@app.route('/')
def login():
    return render_template('login.html')

@app.route('/registration', methods=['POST'])
def login_route():
    username = request.form['username']
    password = request.form['password']
    register_user(username, password)
    return redirect(url_for('login'))