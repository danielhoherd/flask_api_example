from typing import Any

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from .interface import FizzbarInterface
from app import db  # noqa


class Fizzbar(db.Model):  # type: ignore
    """A snazzy Fizzbar"""

    __tablename__ = "fizzbar"

    fizzbar_id = Column(Integer(), primary_key=True)
    name = Column(String(255))
    purpose = Column(String(255))

    def update(self, changes: FizzbarInterface):
        for key, val in changes.items():
            setattr(self, key, val)
        return self
