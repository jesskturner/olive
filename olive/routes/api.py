from sanic import Blueprint
from sanic.response import json
from sanic_jwt.decorators import inject_user

from olive.models.users import User
from olive.utils.database import scoped_session

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


@api_routes.route("/user")
@inject_user()
def user(request):
    return json({"user_id": user.id})
