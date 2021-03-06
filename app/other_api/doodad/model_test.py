from flask_sqlalchemy import SQLAlchemy
from pytest import fixture

from .model import Doodad
from app.test.fixtures import app
from app.test.fixtures import db


@fixture
def doodad() -> Doodad:
    return Doodad(doodad_id=1, name="Test doodad", purpose="Test purpose")


def test_Doodad_create(doodad: Doodad):
    assert doodad


def test_Doodad_retrieve(doodad: Doodad, db: SQLAlchemy):  # noqa
    db.session.add(doodad)
    db.session.commit()
    s = Doodad.query.first()
    assert s.__dict__ == doodad.__dict__
