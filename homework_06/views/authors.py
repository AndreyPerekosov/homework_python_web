from flask import (
    Blueprint,
    render_template, redirect, url_for,
)
from flask_login import login_required, current_user

from blogproject import User, Post
from blogproject.database import db
from views.forms import PostForm

authors_app = Blueprint("authors_app", __name__)


@authors_app.route('/<int:user_id>/', endpoint='author', methods=['GET', 'POST'])
def author(user_id):
    current_user
    auth = db.get_or_404(User, user_id)
    posts = db.session.execute(db.select(Post).where(Post.user_id == user_id)).scalars()
    form = PostForm(meta={'csrf': False})
    if form.validate_on_submit() and current_user.is_authenticated and current_user.id == auth.id:
        title = form.title.data
        body = form.body.data
        post = Post(title=title, body=body, user_id=auth.id)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('authors_app.author', user_id=user_id))
    return render_template('authors/author.html', author=auth, posts=posts, form=form, current_user=current_user)


@authors_app.route('<int:user_id>/<int:post_id>/', endpoint='post_delete', methods=['POST'])
@login_required
def post_delete(user_id, post_id):
    if current_user.is_authenticated and current_user.id == user_id:
        post = db.get_or_404(Post, post_id)
        db.session.delete(post)
        db.session.commit()
    return redirect(url_for('authors_app.author', user_id=user_id))
