from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from olive.models.tasks import Tag, Task
from olive.models.users import User
