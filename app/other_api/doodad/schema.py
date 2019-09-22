from marshmallow import fields
from marshmallow import Schema


class DoodadSchema(Schema):
    """Doodad schema"""

    doodadId = fields.Number(attribute="doodad_id")
    name = fields.String(attribute="name")
    purpose = fields.String(attribute="purpose")
