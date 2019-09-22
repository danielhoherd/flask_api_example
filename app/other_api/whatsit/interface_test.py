from pytest import fixture

from .interface import WhatsitInterface
from .model import Whatsit


@fixture
def interface() -> WhatsitInterface:
    return WhatsitInterface(whatsit_id=1, name="Test whatsit", purpose="Test purpose")


def test_WhatsitInterface_create(interface: WhatsitInterface):
    assert interface


def test_WhatsitInterface_works(interface: WhatsitInterface):
    whatsit = Whatsit(**interface)
    assert whatsit
