from flask import Flask, request, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/signup')
def display_form():
    return render_template("welcome.html",title="SignUp", username="", usernameError="",password="",
    passwordError="", password2="", password2Error="", email="", emailError="")


def validEmail(email):
    valid1 = False
    for char in email:
        if char in '@':
            valid1 = True  
    valid2 = False
    for char in email:
        if char in '.':
            valid2 = True
    if valid1 and valid2:
        return True
    else:
        return False
    
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

    #Username validation
    if not username:
        usernameError = 'Username is required'
    else:
        if len(username)<3 or len(username)>20:
            usernameError = 'Username should be between 3 and 20 characters long'
            username = ''
        else:
            for char in username:
                if char == ' ':
                    usernameError = 'Username should not contain spaces'
                    username = ''

    #Password validation                
    if not password:
        passwordError = 'Password is required'
    else:
        if len(password)<3 or len(password)>20:
            passwordError = 'Password should be between 3 and 20 characters long'
            password = ''
        else:
            for char in password:
                if char == ' ':
                    passwordError = 'Password should not contain spaces'
                    password = ''
        
    #Password confirmation validation
    if not password2:
        password2Error = 'Please confirm the password above'
        password2 = ''
    else:
        if (password != password2):   
            password2Error = 'Passwords should match'
            password2 = ''

    #Email validation
    if email:
        if len(email)<3 or len(email)>20:
            emailError = 'Email should be bewteen 3 and 20 characters long.'
            email = ''
        else:
            for char in email:
                if char == ' ':
                    emailError = 'Email should not contain spaces'
                    email = ''
                else:
                    if not validEmail(email):
                        emailError = 'Enter valid email'
                        email = ''


    #Rendering the form
    if not usernameError and not passwordError and not password2Error and not emailError:
        return render_template("homepage.html", title="Welcome", name=username)
    else:
        return render_template("welcome.html", title='SignUO', username=username, usernameError=usernameError,
        password=password, passwordError=passwordError, password2=password2,
        password2Error=password2Error, email=email, emailError=emailError)


app.run()