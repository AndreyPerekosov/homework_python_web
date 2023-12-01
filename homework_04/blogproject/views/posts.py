from flask import (
    Blueprint,
    render_template,
)

posts_app = Blueprint("posts_app", __name__)


@posts_app.get('/', endpoint='posts')
def posts():
    return render_template('posts/posts.html')


@posts_app.get('/post', endpoint='post')
def posts():
    return render_template('posts/post.html')
