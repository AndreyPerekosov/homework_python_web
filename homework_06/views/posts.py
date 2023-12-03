from flask import (
    Blueprint,
    render_template,
)

from blogproject import Post
from blogproject.database import db

posts_app = Blueprint("posts_app", __name__)


@posts_app.get('/', endpoint='posts')
def posts():
    poss = db.session.execute(db.select(Post).order_by(Post.title)).scalars()
    return render_template('posts/posts.html', posts=poss)


@posts_app.get('<int:auth_id>/<int:post_id>/', endpoint='post')
def post(auth_id, post_id):
    pos = db.get_or_404(Post, post_id)
    return render_template('posts/post.html', auth_id=auth_id, post=pos)
