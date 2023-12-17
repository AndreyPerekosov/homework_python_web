from flask import (
    Blueprint,
    render_template, redirect, url_for, request, flash,
)
from flask_login import login_user, login_required, logout_user

from blogproject import User
from blogproject.database import db
from views.forms import SignupForm, LoginForm

auth_app = Blueprint("auth_app", __name__)


@auth_app.route('/login', endpoint='login', methods=['GET', 'POST'])
def login():
    form = LoginForm(meta={'csrf': False})
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        remember = True if request.form.get('remember') else False
        user = db.session.execute(db.select(User).filter_by(email=email)).first()[0]
        if not user or not user.check_password(password):
            flash('Please check your login details and try again.')
            return redirect(url_for('auth_app.login'))
        login_user(user, remember=remember)
        return redirect(url_for('index'))
    return render_template('auth/login.html', form=form)


@auth_app.route('/signup', endpoint='signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm(meta={'csrf': False})
    if form.validate_on_submit():
        email = form.email.data
        name = form.name.data
        username = form.username.data
        password = form.password.data
        user = db.session.execute(db.select(User).filter_by(email=email)).one_or_none()

        if user:
            return redirect(url_for('auth_app.signup'))

        new_user = User(email=email, name=name, username=username)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('auth_app.login'))

    return render_template('auth/signup.html', form=form)


@auth_app.route('/logout', endpoint='logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))
