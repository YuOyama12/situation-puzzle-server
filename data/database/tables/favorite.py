from .core import TimestampMixin
from sqlalchemy import BIGINT, Column, ForeignKey, String, UniqueConstraint
from data.database.db import Base

import uuid

class Favorite(Base, TimestampMixin):
    __tablename__ = "favorites"
    __table_args__ = (
        ## 同一ユーザーが同一問題をお気に入り登録することは不可とする。
        UniqueConstraint("user_id", "quiz_id", name="favorite_unique"),
    )
    

    id = Column(String(36), primary_key=True, default=uuid.uuid4)
    user_id = Column(BIGINT, ForeignKey("users.id", ondelete="CASCADE"), default=0, nullable=False)
    quiz_id = Column(String(36), ForeignKey("quizzes.id", ondelete="CASCADE"), nullable=False)