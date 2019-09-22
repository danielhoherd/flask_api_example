from typing import List

from flask import request
from flask.wrappers import Response
from flask_accepts import accepts
from flask_accepts import responds
from flask_restplus import Namespace
from flask_restplus import Resource

from .interface import WidgetInterface
from .model import Widget
from .schema import WidgetSchema
from .service import WidgetService

api = Namespace("Widget", description="Single namespace, single entity")  # noqa


@api.route("/")
class WidgetResource(Resource):
    """Widgets"""

    @responds(schema=WidgetSchema, many=True)
    def get(self) -> List[Widget]:
        """Get all Widgets"""

        return WidgetService.get_all()

    @accepts(schema=WidgetSchema, api=api)
    @responds(schema=WidgetSchema)
    def post(self) -> Widget:
        """Create a Single Widget"""

        return WidgetService.create(request.parsed_obj)


@api.route("/<int:widgetId>")
@api.param("widgetId", "Widget database ID")
class WidgetIdResource(Resource):
    @responds(schema=WidgetSchema)
    def get(self, widgetId: int) -> Widget:
        """Get Single Widget"""

        return WidgetService.get_by_id(widgetId)

    def delete(self, widgetId: int) -> Response:
        """Delete Single Widget"""
        from flask import jsonify

        id = WidgetService.delete_by_id(widgetId)
        return jsonify(dict(status="Success", id=id))

    @accepts(schema=WidgetSchema, api=api)
    @responds(schema=WidgetSchema)
    def put(self, widgetId: int) -> Widget:
        """Update Single Widget"""

        changes: WidgetInterface = request.parsed_obj
        Widget = WidgetService.get_by_id(widgetId)
        return WidgetService.update(Widget, changes)
