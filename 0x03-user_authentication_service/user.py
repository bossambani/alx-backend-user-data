#!/usr/bin/env python3
"""
Module: models
Defines the SQLAlchemy User model for the users table.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """
    Represents a user in the application.

    Attributes:
        id (int): The primary key, unique identifier for the user.
        email (str): The email address must be unique and not null.
        hashed_password (str): The hashed password must not be null.
        session_id (str): The current session ID can be null.
        reset_token (str): The reset token for password recovery
        can be null.
    """

    __tablename__ = 'users'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    email: str = Column(String(250), nullable=False, unique=True)
    hashed_password: str = Column(String(250), nullable=False)
    session_id: str = Column(String(250), nullable=True)
    reset_token: str = Column(String(250), nullable=True)

    def __repr__(self) -> str:
        """
        Returns a string representation of the User instance.
        Returns:
            str: The string representation of the user.
        """
        return f"<User(id={self.id}, email='{self.email}')>"
