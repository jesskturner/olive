from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String

from olive.models import Base


class User(Base):
    """
    A model representing a user.
    """
    __tablename__ = 'user'

    id = Column(Integer, autoincrement=True, primary_key=True)
    email = Column(String(255), nullable=False)
    first_name = Column(String(35), nullable=True)
    last_name = Column(String(35), nullable=True)
    date_created = Column(DateTime, default=datetime.now)
    date_modified = Column(DateTime, onupdate=datetime.now)
    date_archived = Column(DateTime, nullable=True)
