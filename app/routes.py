from flask import render_template, redirect, request, url_for, request, Blueprint
from werkzeug import datastructures
from app import app, db
from werkzeug.security import check_password_hash
from flask_login import login_user, logout_user, login_required, current_user

from app.forms import UserInfoForm
from app.models import User


@app.route('/', methods=['GET', 'POST'])
@app.route('/home')
def signMeUp():
    my_form = UserInfoForm()
    if request.method == "POST":
        if my_form.validate():

            username = my_form.username.data
            email = my_form.email.data
            password = my_form.password.data

            # create instance new user
            user = User(username, email, password)
            # add instance to databse
            db.session.add(user)
            # commit to databse
            db.session.commit()

            return render_template('feed.html')

        else:
            print('Not validated! :(')
    return render_template('home.html', form=my_form)
