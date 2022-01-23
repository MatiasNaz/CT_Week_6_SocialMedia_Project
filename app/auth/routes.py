from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug.security import check_password_hash
from flask_login import login_user, logout_user, login_required, current_user

from .forms import LoginForm
from app.models import User, Post

auth = Blueprint('auth', __name__, template_folder='auth_templates')


@auth.route('/login', methods=['GET', "POST"])
def logMeIn():
    form = LoginForm()
    if request.method == "POST" and form.validate():
        username = form.username.data
        password = form.password.data
        remember_me = form.remember_me.data

        # check if user exists
        user = User.query.filter_by(username=username).first()

        if user is None or not check_password_hash(user.password, password):
            return redirect(url_for('auth.logMeIn'))

        # log me in
        login_user(user, remember=remember_me)
        print(current_user)
        return redirect(url_for('post.feedHome'))

    return render_template('login.html', form=form)
