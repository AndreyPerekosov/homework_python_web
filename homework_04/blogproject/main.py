import os
from sqlalchemy import create_engine
from flask import Flask, render_template

from blogproject.database import Base

from views.about import about_app
from views.authors import authors_app
from views.posts import posts_app

PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+pg8000://user:password@localhost/postgres"

engine = create_engine(PG_CONN_URI, echo=True)

if __name__ == '__main__':
    Base.metadata.create_all(engine)

app = Flask(__name__)

app.register_blueprint(about_app, url_prefix="/about")
app.register_blueprint(posts_app, url_prefix="/posts")
app.register_blueprint(authors_app, url_prefix="/authors")


@app.route('/', endpoint='index')
def index():
    return render_template('index.html')


