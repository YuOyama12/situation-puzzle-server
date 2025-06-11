from .core import TimestampMixin
from sqlalchemy import Column, String, BIGINT, LargeBinary
from data.database.db import Base

class User(Base, TimestampMixin):
    __tablename__ = "users"

    id = Column(BIGINT, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    nickname = Column(String(255), nullable=True)
    password = Column(LargeBinary(60), nullable=False)