from typing import Any

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from .interface import DoodadInterface
from app import db  # noqa


class Doodad(db.Model):  # type: ignore
    """A snazzy Doodad"""

    __tablename__ = "doodad"

    doodad_id = Column(Integer(), primary_key=True)
    name = Column(String(255))
    purpose = Column(String(255))

    def update(self, changes: DoodadInterface):
        for key, val in changes.items():
            setattr(self, key, val)
        return self
