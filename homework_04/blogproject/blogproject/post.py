from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Text
)
from sqlalchemy.orm import relationship
from blogproject.database import Base
from blogproject.mixins import TimestampMixin


class Post(TimestampMixin, Base):
    title = Column(String(120), nullable=False, default="", server_default="")
    body = Column(Text, nullable=False, default="", server_default="")

    user_id = Column(Integer, ForeignKey("astra_users.id"), nullable=False)
    user = relationship("User", back_populates="posts")

    def __str__(self):
        return (
            f"{self.__class__.__name__}(id={self.id}), "
            f"title={self.title!r}, user_id={self.user_id}"

        )

    def __repr__(self):
        return str(self)
