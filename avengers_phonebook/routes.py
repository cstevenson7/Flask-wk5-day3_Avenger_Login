from avengers_phonebook import app, db, Message, mail
from flask import render_template, request, redirect, url_for

#Import the form
from avengers_phonebook.forms import UserInfoForm
from avengers_phonebook.forms import LoginForm

#Import from Models
from avengers_phonebook.models import User, check_password_hash


#Import for Flask-logins - loginrequired, current usaer and logout _user
from flask_login import login_required, login_user, current_user, logout_user



#Home page route
@app.route('/')  # decorator
def home():
    return render_template("home.html")

#HPhone_book route
@app.route('/phone_book')  # decorator
@login_required 
def phone_book():
    return render_template("phone_book.html")

#Register route
@app.route('/register', methods= ['GET','POST'])  # decorator
def register():
    form = UserInfoForm()
    #form.validate is checking the CSFR token thing, if the request is a GET it just renders the form
    # if the request == post then the user info entered is SENT
    if request.method == 'POST' and form.validate():
        #Get Information
        username = form.username.data
        email = form.email.data  
        phone_number = form.phone_number.data      
        password = form.password.data     
        print("\n", username, email, phone_number, password)  # this will print out in terminal

        #Create and instance of User-- look at the __init__ in models
        user = User(username, email, phone_number, password)
        #Open and insert into db - connecting to db like an insert statement
        db.session.add(user)
        # lik git add and then commit Save info to db
        db.session.commit()

        # #Flask email sender
        # msg = Message(f'Thanks for signing up, {username}', recipients= [email])
        # msg.body= ('Congrats on signing up!')
        # msg.html = ('<h1>Great to have your contact info</h1>' '<p> I can do this all day</p>')
        # mail.send(msg)

    return render_template("register.html", form=form)

#Add phone route
# @app.route('/add_phone', methods= ['GET','POST'])  # decorator
# def add_phone():
#     form = PhoneForm()
#     #form.validate is checking the CSFR token thing, if the request is a GET it just renders the form
#     # if the request == post then the user info entered is SENT
#     if request.method == 'POST' and form.validate():
#         #Get Information
#         realname = form.readname.data
#         email = form.email.data
#         phone_number = form.phone_number.data
#         print("\n", realname,phone_number)  # this will print out in terminal

#         #Create and instance of User-- look at the __init__ in models
#         user = User(realname, phone_number)
#         #Open and insert into db - connecting to db like an insert statement
#         db.session.add(user)
#         # lik git add and then commit Save info to db
#         db.session.commit()

#     return render_template("add_phone", form=form)


# Login route
@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm() # create instance of login form
    if request.method == 'POST' and form.validate():
        email = form.email.data
        password = form.password.data
        logged_user = User.query.filter(User.email == email).first()
         # runs the same hash method on the entered password and then matches
         #  the hash  - returns True or false
        if logged_user and check_password_hash(logged_user.password, password):
            login_user(logged_user)
            return redirect(url_for('home'))
        else:
            return redirect(url_for('login')) # this is a GET request, like a refresh
        
    return render_template('login.html', form = form)

