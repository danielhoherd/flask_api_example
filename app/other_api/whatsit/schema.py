from marshmallow import fields
from marshmallow import Schema


class WhatsitSchema(Schema):
    """Whatsit schema"""

    whatsitId = fields.Number(attribute="whatsit_id")
    name = fields.String(attribute="name")
    purpose = fields.String(attribute="purpose")
