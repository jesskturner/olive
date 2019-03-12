from sanic import Sanic
from sanic_jwt import Initialize

from olive.routes.api import api_routes
from olive.routes.base import base_routes
from olive.routes.user import user_views
from olive.utils.authentication import authenticate

from settings import WEB_PORT


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
