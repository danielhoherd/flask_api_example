from pytest import fixture

from .interface import FizzbarInterface
from .model import Fizzbar
from .schema import FizzbarSchema


@fixture
def schema() -> FizzbarSchema:
    return FizzbarSchema()


def test_FizzbarSchema_create(schema: FizzbarSchema):
    assert schema


def test_FizzbarSchema_works(schema: FizzbarSchema):
    params: FizzbarInterface = schema.load({"fizzbarId": "123", "name": "Test fizzbar", "purpose": "Test purpose"}).data
    fizzbar = Fizzbar(**params)

    assert fizzbar.fizzbar_id == 123
    assert fizzbar.name == "Test fizzbar"
    assert fizzbar.purpose == "Test purpose"
