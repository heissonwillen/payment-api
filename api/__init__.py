from flask import Flask
from . import config
from api.views import blueprint


def create_app(config_class="api.config"):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.register_blueprint(blueprint)

    return app
