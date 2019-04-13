from flask import Flask, request, redirect, render_template
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/signup')
def display_form():
    return render_template("welcome.html",title="SignUp", username="", usernameError="",password="",
    passwordError="", password2="", password2Error="", email="", emailError="")

def is_len(string):
    if len(string)<3 or len(string)>20:
        return True
    else:
        return False

def is_space(string):
    for char in string:
        if char == ' ':
            print("space")
            return True
       

@app.route('/signup', methods=['POST'])
def validate_form():
    username = request.form['username']
    password = request.form['password']
    password2 = request.form['password2']
    email = request.form['email']

    usernameError = ''
    passwordError = ''
    password2Error = ''
    emailError = ''

    if not username:
        usernameError = 'Username is required'
    else:
        if is_len(username) or is_space(username):
            usernameError = 'Username should be between 3 and 20 characters long and should not contain spaces'
            username = ''

    if not password:
        passwordError = 'Password is required'
    else:
        if is_len(password) or is_space(password):
            passwordError = 'Password should be between 3 and 20 characters long and should not contain spaces'
            password = ''

    if password != password2:   
        password2Error = 'Passwords should match'
        password2 = ''

    if email:
        if is_len(email) or is_space(email):
            emailError = 'Email should be bewteen 3 and 20 characters long and should not contain spaces'
            email = ''
        else:
            for char in string:
                if char != '.' or char != '@':
                    return True
                else:
                    return False
            email = ''

    if not usernameError and not passwordError and not password2Error and not emailError:
        return render_template("homepage.html", title="Welcome", name=username)
    else:
        return render_template("welcome.html", username=username, usernameError=usernameError,
        password=password, passwordError=passwordError, password2=password2,
        password2Error=password2Error, email=email, emailError=emailError)


app.run()