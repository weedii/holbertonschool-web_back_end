#!/usr/bin/env python3

"""DB module
"""
from sqlalchemy import create_engine, update
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from user import User
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound

from user import Base


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """add_user method that returns a user object"""
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """find_user_by method that return a user object based on the email"""
        if kwargs is None:
            raise InvalidRequestError
        user = self._session.query(User).filter_by(**kwargs)
        for i in user:
            if i is not None:
                return i
        raise NoResultFound

    def update_user(self, user_id: int, **kwargs) -> None:
        """update_user method that update the user’s attributes
        as passed in the method’s arguments then
        commit changes to the database."""
        try:
            user = self.find_user_by(id=user_id)
            self._session.execute(update(User).values(kwargs))
            self._session.commit()
        except Exception:
            raise ValueError
