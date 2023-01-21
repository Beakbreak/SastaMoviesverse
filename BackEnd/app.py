from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt
from flask_mysqldb import MySQL
import MySQLdb.cursors

app = Flask(__name__)
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'moviesverse'
 
mysql = MySQL(app)
bcrypt = Bcrypt(app)

@app.route('/')
def home() :
    return "Hello world"

@app.route('/login', methods = ['POST'])
def login():
    cursor = mysql.connection.cursor()

    content = request.json
    email = content['email']
    pwd = content['password']

    query = "SELECT * FROM registered_users WHERE email = '{email}' AND password='{pwd}'"

    cursor.execute(query)
    mysql.connection.commit()
    cursor.close()

@app.route('/register', methods = ['GET','POST'])
def register():
    cursor = mysql.connection.cursor()
    content = request.json

    cursor.execute('SELECT * FROM registered_users')
    count = len(cursor.fetchall())
    email = content['email']
    pwd = content['password']
    
    query = "INSERT INTO registered_users VALUES (%s, %s, %s)"
    data = ( count,email, pwd)

    cursor.execute(query, data)
    mysql.connection.commit()
    cursor.close()


@app.route('/predict', methods = ['POST'])
def predict() : 
    movie_ratings = []


if __name__ == "__main__":
    app.run(debug=False, port=8000)