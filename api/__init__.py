from flask import Flask
from api.config import Config


def create_app(config_class=Config):
	app = Flask(__name__)
	app.config.from_object(Config)

	from flaskblog.users.routes import users

	app.register_blueprint(users)

	return app
