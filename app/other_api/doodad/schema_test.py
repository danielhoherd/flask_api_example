from pytest import fixture

from .interface import DoodadInterface
from .model import Doodad
from .schema import DoodadSchema


@fixture
def schema() -> DoodadSchema:
    return DoodadSchema()


def test_DoodadSchema_create(schema: DoodadSchema):
    assert schema


def test_DoodadSchema_works(schema: DoodadSchema):
    params: DoodadInterface = schema.load({"doodadId": "123", "name": "Test doodad", "purpose": "Test purpose"}).data
    doodad = Doodad(**params)

    assert doodad.doodad_id == 123
    assert doodad.name == "Test doodad"
    assert doodad.purpose == "Test purpose"
