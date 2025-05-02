from flask import Blueprint, render_template, request
from app import models 

routes = Blueprint('routes', __name__)

@routes.route('/', methods=['GET', 'POST'])
def login():
    message = ''
    if request.method == 'POST':
        username = request.form['username']  
        password = request.form['password']

        if models.validate_user(username, password):
            message = 'Login Successful'
        else:
            message = 'Invalid Credentials'

    return render_template('login.html', message=message)
