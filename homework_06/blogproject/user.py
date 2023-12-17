from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from blogproject.database import Base
from blogproject.mixins import TimestampMixin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, login_manager
from blogproject.database import db


class User(TimestampMixin, UserMixin, Base):
    name = Column(String(64), nullable=False)
    username = Column(String(64), nullable=False)
    email = Column(String(64), nullable=False, unique=True)
    password_hash = Column(String(300), nullable=False)

    posts = relationship("Post", back_populates="user")

    def __str__(self):
        return (
            f"{self.__class__.__name__}(id={self.id}), "
            f"name={self.name!r}, username={self.username!r},"
            f"email={self.email!r}"
        )

    def __repr__(self):
        return str(self)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
