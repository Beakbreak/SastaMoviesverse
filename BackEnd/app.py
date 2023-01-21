from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt
from flask_mysqldb import MySQL
 
app = Flask(__name__)
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'moviesverse'
 
mysql = MySQL(app)
bcrypt = Bcrypt(app)

cursor = mysql.connection.cursor()

@app.route('/')
def home() :
    return "Hello world"

@app.route('/login', methods = ['POST'])
def login():
    email = request.form['email']
    pwd = request.form['password']

    query = "SELECT password FROM users WHERE email = {email}"

    cursor.execute(query)

    data = cursor.fetchall()

    print(data)

@app.route('/register', methods = ['POST'])
def register():
    name = request.form['username']
    email = request.form['email']
    pwd = request.form['password']
    
    query = "INSERT INTO users VALUES (%s, %s, %s)"
    data = (name, email, pwd)

    cursor.execute(query, data)


if __name__ == "__main__":
    app.run(debug=False, port=8000)