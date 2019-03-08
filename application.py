from sanic import Sanic

from olive.routes.api import api_routes
from olive.routes.base import base_routes

from settings import WEB_PORT


app = Sanic(__name__)
app.blueprint(api_routes)
app.blueprint(base_routes)
app.static('/', 'dist')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(WEB_PORT))
