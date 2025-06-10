from .core import TimestampMixin
from sqlalchemy import Column, String, Text
from data.database.db import Base

import uuid

class Quiz(Base, TimestampMixin):
    __tablename__ = "quizzes"

    id = Column(String(36), primary_key=True, default=uuid.uuid4)
    title = Column(String(24))
    question = Column(Text)
    answer = Column(Text)