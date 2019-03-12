from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy_utils import EmailType, PasswordType, force_auto_coercion

from olive.models import Base


force_auto_coercion()


class User(Base):
    """
    A model representing a user.
    """
    __tablename__ = 'user'

    id = Column(Integer, autoincrement=True, primary_key=True)
    email = Column(EmailType, nullable=False, unique=True)  # Username
    password = Column(PasswordType(schemes=['pbkdf2_sha512']), nullable=False)
    first_name = Column(String(35), nullable=True)
    last_name = Column(String(35), nullable=True)
    date_created = Column(DateTime, default=datetime.now)
    date_modified = Column(DateTime, onupdate=datetime.now)
    date_archived = Column(DateTime, nullable=True)

    def __repr__(self):
        return "User(id='{}')".format(self.id)

    def to_dict(self):
        return {"id": self.id, "email": self.email}
