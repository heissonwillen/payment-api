from flask import Flask
from api.config import Config


def create_app(config_class=Config):
	app = Flask(__name__)
	app.config.from_object(Config)

	from api.views.views import blueprint

	app.register_blueprint(blueprint)

	return app
