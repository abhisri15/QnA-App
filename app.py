from flask import Flask, render_template, g,request, session
from database import get_db
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24) # necessary for sessions to work

@app.teardown_appcontext # teardown any active databases to avoid memory leaks
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/register', methods=['POST','GET'])
def register():
    if request.method=='POST':

        db=get_db()
        hashed_password=generate_password_hash(request.form['password'], method='pbkdf2:sha256')
        db.execute('insert into user (name, password, expert, admin) values (?,?,?,?)', [request.form['name'], hashed_password, '0', '0'])
        db.commit()

        return 'User Created!'

    return render_template('register.html')

@app.route('/login', methods=['POST','GET'])
def login():
    if request.method=='POST':

        db=get_db()
        name=request.form['name']
        password=request.form['password']

        user_curr=db.execute('select id,name, password from user where name=?', [name])
        user_result=user_curr.fetchone()

        if(check_password_hash(user_result['password'], password)):
            return 'Logged in successfully'
        else:
            return 'Invalid username or password'

    return render_template('login.html')

@app.route('/question')
def question():
    return render_template('question.html')

@app.route('/answer')
def answer():
    return render_template('answer.html')

@app.route('/ask')
def ask():
    return render_template('ask.html')

@app.route('/unanswered')
def unanswered():
    return render_template('unanswered.html')

@app.route('/users')
def users():
    return render_template('users.html')

if __name__ == '__main__':
    app.run(debug=True)