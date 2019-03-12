from sanic import Sanic

from sanic_jwt import exceptions
from sanic_jwt import Initialize

from olive.models.users import User
from olive.routes.api import api_routes
from olive.routes.base import base_routes
from olive.routes.user import Register

from settings import WEB_PORT


# TODO: Replace with database calls.
users = [
    User(id=1, email="user1@example.com", password="abcxyz"),
    User(id=2, email="user2@example.com", password="abcxyz"),
]
email_table = {u.email: u for u in users}
userid_table = {u.id: u for u in users}


async def authenticate(request, *args, **kwargs):
    email = request.json.get("email", None)
    password = request.json.get("password", None)

    if not email or not password:
        raise exceptions.AuthenticationFailed("Missing email or password.")

    user = email_table.get(email, None)
    if user is None:
        raise exceptions.AuthenticationFailed("User not found.")

    if password != user.password:
        raise exceptions.AuthenticationFailed("Password is incorrect.")

    return user


user_views = (
    ('/register', Register),
)

app = Sanic(__name__)
Initialize(
    app,
    authenticate=authenticate,
    class_views=user_views,
    url_prefix='/api/auth',
    user_id='id')
app.blueprint(api_routes)
app.blueprint(base_routes)
app.static('/', 'dist')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(WEB_PORT))
