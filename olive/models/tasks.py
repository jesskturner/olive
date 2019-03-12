from datetime import datetime

from sqlalchemy import (
    Column, DateTime, ForeignKey, Integer, String, Table, Text)
from sqlalchemy.orm import relationship

from olive.models import Base


task_tag_table = Table(
    'task_tag',
    Base.metadata,
    Column('task_id', Integer, ForeignKey('task.id')),
    Column('tag_value', String(50), ForeignKey('tag.value')),
    Column('date_created', DateTime, default=datetime.now),
    Column('date_archived', DateTime, nullable=True),
)


class Tag(Base):
    """
    A model representing a tag value that may be applied to Tasks.
    """
    __tablename__ = 'tag'

    value = Column(String(50), nullable=False, primary_key=True)
    tasks = relationship(
        "Task",
        secondary=task_tag_table,
        back_populates="tags")
    date_created = Column(DateTime, default=datetime.now)
    date_modified = Column(DateTime, onupdate=datetime.now)
    date_archived = Column(DateTime, nullable=True)


class Task(Base):
    """
    A model representing a task that may be created by a user.
    """
    __tablename__ = 'task'

    id = Column(Integer, autoincrement=True, primary_key=True)
    user = Column(Integer, ForeignKey("user.id"), nullable=False)
    input_string = Column(Text, nullable=True)
    description = Column(Text, nullable=True)
    priority = Column(Integer, nullable=True)
    size = Column(Integer, nullable=True)
    tags = relationship(
        "Tag",
        secondary=task_tag_table,
        back_populates="tasks")
    date_created = Column(DateTime, default=datetime.now)
    date_modified = Column(DateTime, onupdate=datetime.now)
    date_archived = Column(DateTime, nullable=True)


