from marshmallow import fields
from marshmallow import Schema


class WidgetSchema(Schema):
    """Widget schema"""

    widgetId = fields.Number(attribute="widget_id")
    name = fields.String(attribute="name")
    purpose = fields.String(attribute="purpose")
