from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from blogproject.database import Base
from blogproject.mixins import TimestampMixin


class User(TimestampMixin, Base):
    name = Column(String(64), nullable=False)
    username = Column(String(64), nullable=False)
    email = Column(String(64), nullable=False, unique=True)

    posts = relationship("Post", back_populates="user")

    def __str__(self):
        return (
            f"{self.__class__.__name__}(id={self.id}), "
            f"name={self.name!r}, username={self.username!r},"
            f"email={self.email!r}"
        )

    def __repr__(self):
        return str(self)

