from flask_sqlalchemy import SQLAlchemy
from pytest import fixture

from .model import Widget
from app.test.fixtures import app
from app.test.fixtures import db


@fixture
def widget() -> Widget:
    return Widget(widget_id=1, name="Test widget", purpose="Test purpose")


def test_Widget_create(widget: Widget):
    assert widget


def test_Widget_retrieve(widget: Widget, db: SQLAlchemy):  # noqa
    db.session.add(widget)
    db.session.commit()
    s = Widget.query.first()
    assert s.__dict__ == widget.__dict__
