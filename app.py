from flask import Flask, render_template, request, redirect, session
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "supersecretkey"

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="e3@#45@oilh@51",
    database="edu_db"
)
cursor = db.cursor(dictionary=True)

@app.route('/')
def index():
    return redirect('/login')

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = generate_password_hash(request.form['password'])
        
        cursor.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)", 
                       (username, email, password))
        db.commit()
        return redirect('/login')
    return render_template('register.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
        user = cursor.fetchone()
        
        if user and check_password_hash(user['password'], password):
            session['user_id'] = user['id']
            session['username'] = user['username']
            return redirect('/dashboard')
        else:
            return "Invalid login"
    return render_template('login.html')

@app.route('/dashboard', methods=['GET'])
def dashboard():
    if 'user_id' not in session:
        return redirect('/login')
    cursor.execute("SELECT * FROM details WHERE user_id=%s", (session['user_id'],))
    details = cursor.fetchall()
    return render_template('dashboard.html', username=session['username'], details=details)

@app.route('/add_detail', methods=['POST'])
def add_detail():
    if 'user_id' not in session:
        return redirect('/login')
    info = request.form['info']
    cursor.execute("INSERT INTO details (user_id, info) VALUES (%s, %s)", (session['user_id'], info))
    db.commit()
    return redirect('/dashboard')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')

if __name__ == "__main__":
    app.run(debug=True)
