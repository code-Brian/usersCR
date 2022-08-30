from flask import Flask, render_template, session, request, redirect
from user import User

app = Flask(__name__)
app.secret_key = '1234567890'

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)