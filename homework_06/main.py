import os

import click
from flask import Flask, render_template
from flask_migrate import Migrate

from blogproject import User, Post
from blogproject.database import db
from views.about import about_app
from views.authors import authors_app
from views.posts import posts_app

PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+pg8000://user:password@localhost/postgres"

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = PG_CONN_URI
db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(about_app, url_prefix="/about")
app.register_blueprint(posts_app, url_prefix="/posts")
app.register_blueprint(authors_app, url_prefix="/authors")


@app.cli.command("fill-db")
@click.argument("num")
def fill_in_table(num):
    num = int(num)
    for num in range(num):
        tmp_ath = User(name='user' + str(num),
                       username='suruser' + str(num),
                       email='user' + str(num) + '@mail.com')
        db.session.add(tmp_ath)
        for num_post in range(2):
            tmp_post = Post(title='Far' + str(num * num_post), body='far, far away', user=tmp_ath)
            db.session.add(tmp_post)
    db.session.commit()


@app.route('/', endpoint='index')
def index():
    users = db.session.execute(db.select(User).order_by(User.username)).scalars()
    return render_template('index.html', users=users)
