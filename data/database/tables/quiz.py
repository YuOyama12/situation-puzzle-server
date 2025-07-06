import uuid

from sqlalchemy import BIGINT, Column, String, Text
from sqlalchemy.orm import relationship

from data.database.db import Base

from .core import TimestampMixin


class Quiz(Base, TimestampMixin):
    __tablename__ = "quizzes"

    id = Column(String(36), primary_key=True, default=uuid.uuid4)
    user_id = Column(BIGINT, default=0)
    title = Column(String(24))
    question = Column(Text)
    answer = Column(Text)

    favorites = relationship("Favorite")