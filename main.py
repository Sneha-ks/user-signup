from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    return render_template("welcome.html",title="SignUp")

@app.route('/signup', methods=['POST'])
def signup():
    username = request.form['username']
    password = request.form['password']
    password1 = request.form['password1']
    email = request.form['email']

    usernameError = ""
    passwordError = ""
    password1Error = ""
    emailError = ""

    if not username:
        usernameError = "Username can't be empty"
    else:
        if (len(username) < 3) and (len(username)> 20):
            usernameError = "Username should be between 3 and 20 characters in length"
        #else:
    #else
    if not password:
        passwordError = "Password can't be empty"
    #else 


app.run()