from sqlalchemy import select

from pytest import fixture

from blogproject import Post
from blogproject.user import User
from sqlalchemy.orm import Session
from main import PG_CONN_URI
from sqlalchemy import create_engine

engine = create_engine(PG_CONN_URI, echo=True)


@fixture(scope='session')
def create_user():
    session = Session(engine)
    user = User(name='John', username='Smith', email='astra@ya.ru')
    session.add(user)
    session.commit()
    yield user
    session.delete(user)
    session.commit()


@fixture(scope='function')
def create_post():
    session = Session(engine)
    stm = select(User).where(User.name == 'John')
    res = session.execute(stm)
    user = res.scalar_one_or_none()
    post = Post(title='Far', body='far, far away', user=user)
    session.add(post)
    session.commit()
    yield post
    session.delete(post)
    session.commit()
