from flask import Flask, render_template, session, request, redirect
from flask_app.models.user import User
from flask_app import app

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

@app.route('/user/delete/<int:id>')
def delete(id):
    data={
        "id": id
    }
    User.delete_one(data)
    return redirect('/users/show')

@app.route('/user/edit/<int:id>')
def edit(id):
    data ={
        "id" : id
    }
    return render_template('edit_user.html', user=User.get_one(data))

@app.route('/user/update/', methods=['POST'])
def update():
    User.update(request.form)
    return redirect('/users/show')