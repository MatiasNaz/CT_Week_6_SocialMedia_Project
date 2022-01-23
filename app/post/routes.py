from app.models import db
from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import current_user, login_required
from flask.helpers import flash
from werkzeug.datastructures import ContentRange

### IMPORT FORMS HERE ONCE WE HAVE THEM
from .forms import PostForm

from app.models import Post

# create instance of blueprint
post = Blueprint('post', __name__, template_folder='post_templates')


@post.route('/feed')
def feedHome():
    posts = Post.query.all()
    return render_template('feed.html', posts=posts)


# Added Post Page route. - MN
@post.route('/create-post', methods=['GET', 'POST'])
@login_required
def add_post():
    posts = Post.query.all()
    form = PostForm()
    if form.validate_on_submit():
        # Clear the form after submitting. - MN
        title = form.title.data
        image = form.image.data
        content = form.content.data
        # Add post data to database. - MN
        post = Post(title, image, content, current_user.id)
        db.session.add(post)
        db.session.commit()
        # Return a message to user. - MN
        return redirect(url_for('post.feedHome'))
    return render_template('createpost.html', posts=posts, form=form)


@post.route('/posts/update/<int:id>', methods=["GET", "POST"])
@login_required
def updatePost(id):
    post = Post.query.filter_by(id=id).first()
    if post.user_id != current_user.id:
        return redirect(url_for('post.feedHome'))


@post.route('/posts/delete/<int:id>', methods=["POST"])
@login_required
def deletePost(id):
    post = Post.query.filter_by(id=id).first()
    if post.user_id != current_user.id:
        return redirect(url_for('post.feedHome'))

    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('post.feedHome'))


@post.route('/profile')
@login_required
def profile():
    posts = Post.query.filter_by(user_id=current_user.id)
    return render_template('profilepage.html', posts=posts)
