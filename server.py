from flask import Flask, render_template, session, request, redirect
from user import User

app = Flask(__name__)
app.secret_key = '1234567890'

@app.route('/user/new')
def index():
    return render_template('user_new.html')

@app.route("/user/create", methods=['POST'])
def create_user():
    data = {
        'fname' : request.form['fname'],
        'lname' : request.form['lname'],
        'email' : request.form['email'],
        'created_at' : request.form['created_at']
    }
    User.save(data)
    return redirect('/users/show')

@app.route('/users/show')
def show_users_table():
    users = User.get_all()
    return render_template('users.html', users=users)

@app.route('/user/show/<int:id>')
def show(id):
    data ={
        "id" : id
    }
    
    return render_template('show_user.html', user = User.get_one(data))

if __name__ == '__main__':
    app.run(debug=True)