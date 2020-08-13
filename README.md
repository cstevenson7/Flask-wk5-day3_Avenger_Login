README
WeekDay2 FLask database
# This is to make a new virtual env
D:\Coding_Temple\week5\day1\Project>python -m venv avengers_env


# JUST  DO  THIS to get into the VE
D:\Coding_Temple\week5\day1\Project>avengers_env\scripts\activate.bat

(fave_five_env) D:\Coding_Temple\week5\day1\Project>pip install flask

set FLASK_APP=app.py

set FLASK_ENV=development

pip install Flask-WTF

pip install email-validator

pip install Flask-SQLAlchemy Flask-Migrate

flask db init

flask db migrate -m "Create User"

flask db upgrade



Day 3 Commands
pip install flask-mail sendgrid python-dotenv

pip install flask-login

# Ran this after created  users
flask db migrate -m "Create User"

flask db upgrade


 ironman tony im@gmail.com 123456798520

 thor 9999	thor@gmail.com	780-999-5555
