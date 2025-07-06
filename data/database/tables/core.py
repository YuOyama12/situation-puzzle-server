from sqlalchemy import Column, DateTime
from sqlalchemy.ext.declarative import declared_attr

from domain.utils import get_datetime_as_jst


class TimestampMixin(object):
    @declared_attr
    def created_at(cls):
        return Column(DateTime, default=get_datetime_as_jst(), nullable=False)

    @declared_attr
    def updated_at(cls):
        return Column(
            DateTime, default=get_datetime_as_jst(), onupdate=get_datetime_as_jst(), nullable=False
        )
    
    @declared_attr
    def deleted_at(cls):
        return Column(
            DateTime, onupdate=get_datetime_as_jst(), nullable=True
        )