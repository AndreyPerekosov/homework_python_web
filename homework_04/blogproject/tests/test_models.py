from sqlalchemy import select
from sqlalchemy.orm import Session

from blogproject import Post
from main import engine
from blogproject.user import User


# Note! Please run tests with active DB
class TestUser:
    def test_user_exists(self, create_user):
        session = Session(engine)
        user = create_user
        us = session.get(User, user.id)
        assert us.id == user.id


class TestPost:
    def test_post_exists(self, create_post):
        session = Session(engine)
        post = create_post
        ps = session.get(Post, post.id)
        assert ps.id == post.id

    def test_posts_user_exists(self, create_post):
        session = Session(engine)
        post = create_post
        ps = session.get(Post, post.id)
        stm = select(User).where(User.name == 'John')
        res = session.execute(stm)
        us = res.scalar_one_or_none()
        assert us.id == post.user_id
