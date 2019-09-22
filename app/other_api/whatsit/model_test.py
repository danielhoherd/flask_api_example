from flask_sqlalchemy import SQLAlchemy
from pytest import fixture

from .model import Whatsit
from app.test.fixtures import app
from app.test.fixtures import db


@fixture
def whatsit() -> Whatsit:
    return Whatsit(whatsit_id=1, name="Test whatsit", purpose="Test purpose")


def test_Whatsit_create(whatsit: Whatsit):
    assert whatsit


def test_Whatsit_retrieve(whatsit: Whatsit, db: SQLAlchemy):  # noqa
    db.session.add(whatsit)
    db.session.commit()
    s = Whatsit.query.first()
    assert s.__dict__ == whatsit.__dict__
