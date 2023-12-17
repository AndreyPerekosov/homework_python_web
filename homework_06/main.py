import os

import click
from flask import Flask, render_template
from flask_migrate import Migrate
from flask_login import LoginManager

from blogproject import User, Post
from blogproject.database import db
from views.about import about_app
from views.auth import auth_app
from views.authors import authors_app
from views.posts import posts_app

PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+pg8000://user:password@pg:5432/postgres"

app = Flask(__name__)
# simple key only for develop purpose
app.config['SECRET_KEY'] = 'secret-key-goes-here'

app.config['SQLALCHEMY_DATABASE_URI'] = PG_CONN_URI

db.init_app(app)

migrate = Migrate(app, db)

app.register_blueprint(about_app, url_prefix="/about")
app.register_blueprint(posts_app, url_prefix="/posts")
app.register_blueprint(authors_app, url_prefix="/authors")
app.register_blueprint(auth_app, url_prefix="/auth")

login_manager = LoginManager()
login_manager.login_view = 'auth_app.login'
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return db.session.execute(db.select(User).filter_by(id=int(user_id))).first()[0]


@app.cli.command("fill-db")
@click.argument("num")
def fill_in_table(num):
    num = int(num)
    for num in range(num):
        tmp_ath = User(name='user' + str(num),
                       username='suruser' + str(num),
                       email='user' + str(num) + '@mail.com')
        tmp_ath.set_password('test' + str(num))
        db.session.add(tmp_ath)
        for num_post in range(2):
            tmp_post = Post(title='Far' + str(num * num_post), body='far, far away', user=tmp_ath)
            db.session.add(tmp_post)
    db.session.commit()


@app.route('/', endpoint='index')
def index():
    users = db.session.execute(db.select(User).order_by(User.username)).scalars()
    return render_template('index.html', users=users)
