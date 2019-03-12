from sanic_jwt import exceptions

from olive.models.users import User


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
