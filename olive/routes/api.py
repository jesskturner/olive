from sanic import Blueprint
from sanic.response import json

from settings import APP_NAME


api_routes = Blueprint('api_routes', url_prefix='/api')


@api_routes.route("/_health_check")
async def health_check(request):  # noqa
    """
    Return a message indicating that the API is healthy.
    """
    return json({
        "app": APP_NAME,
        "health": "OK",
    })


@api_routes.route("/")
async def meta(request):
    """
    Return information about the API.
    """
    return json({
        "app": APP_NAME,
    })
