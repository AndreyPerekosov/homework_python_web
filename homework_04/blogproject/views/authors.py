from flask import (
    Blueprint,
    render_template,
)

authors_app = Blueprint("authors_app", __name__)


@authors_app.get('/', endpoint='author')
def author():
    return render_template('authors/author.html')


