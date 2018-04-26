import flask
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf.csrf import CSRFProtect

from flask_login import UserMixin, LoginManager
from flask_login import login_user, logout_user, login_required, current_user

from db_utils import *
from forms import *

app = Flask(__name__)

login_manager = LoginManager()

@login_manager.user_loader
def load_user(username):
    if username in user_credentials:
        return User(username)
    return None

class User(UserMixin):
    def __init__(self, username):
        self._name = username
        self._email = user_email[username]
        self._data = user_data[username]

    def get_id(self):
        return self._name

    def todo_list(self):
        return self._data

@app.route("/")
def main():
    return render_template('index.html')

@app.route('/signup', methods=['POST', 'GET'])
def sign_up():
    if current_user.is_authenticated:
        return redirect('/')

    form = SignupForm()

    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data

        user_email[name] = email
        user_credentials[name] = password
        user_data[name] = {}
        store_database()

        return redirect(url_for('login', name=request.form.get("name"),
                                password=request.form.get("password")),code=307)
    else:
        return render_template('signup.html', form=form)

@app.route('/login', methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect('/')

    form = LoginForm()
    if form.validate_on_submit():
        login_user(User(form.name.data))
        return redirect('/')
    else:
        return render_template('login.html', form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect('/')

if __name__ == "__main__":
    app.secret_key = 'key'
    csrf = CSRFProtect(app)
    csrf.init_app(app)
    load_database()
    login_manager.init_app(app)

    app.run(port=60)

