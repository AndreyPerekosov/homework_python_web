from flask import (
    Blueprint,
    render_template,
)

from blogproject import User, Post
from blogproject.database import db

authors_app = Blueprint("authors_app", __name__)


@authors_app.get('/<int:user_id>/', endpoint='author')
def author(user_id):
    auth = db.get_or_404(User, user_id)
    posts = db.session.execute(db.select(Post).where(Post.user_id == user_id)).scalars()
    return render_template('authors/author.html', author=auth, posts=posts)


