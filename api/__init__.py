from flask import Flask
from api.config import Config
from api.views import blueprint


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(blueprint)

    return app
