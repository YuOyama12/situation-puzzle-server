from sqlalchemy import BIGINT, Column, LargeBinary, String

from data.database.db import Base

from .core import TimestampMixin


class User(Base, TimestampMixin):
    __tablename__ = "users"

    id = Column(BIGINT, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    nickname = Column(String(255), nullable=True)
    password = Column(LargeBinary(60), nullable=False)