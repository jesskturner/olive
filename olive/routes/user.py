from sanic_jwt import BaseEndpoint
from olive.models.users import User
from olive.utils.database import scoped_session, Session


class Register(BaseEndpoint):
    async def post(self, request, *args, **kwargs):
        email = request.json.get('email', None)
        first_name = request.json.get('first_name', None)
        last_name = request.json.get('last_name', None)
        password = request.json.get('password', None)

        with scoped_session() as session:
            user = User(
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
            )
            session.add(user)

        access_token, output = await self.responses.get_access_token_output(
            request,
            user,
            self.config,
            self.instance)

        response = self.responses.get_token_reponse(
            request,
            access_token,
            output,
            config=self.config)
        return response
