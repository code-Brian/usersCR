from flask import Flask, render_template, session, request, redirect
from user import User

app = Flask(__name__)
app.secret_key = '1234567890'

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/create_user", methods=['POST'])
def create_user():
    data = {
        'fname' : request.form['fname'],
        'lname' : request.form['lname'],
        'email' : request.form['email'],
        'created_at' : request.form['created_at']
    }
    User.save(data)
    return redirect('/show_users_table')

@app.route('/show_users_table')
def show_users_table():
    users = User.get_all()
    return render_template('users_table.html', all_users=users)

if __name__ == '__main__':
    app.run(debug=True)