from flask import Flask
from config import config
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()


def create_app(ConfigName='DefultConfigName'):
	app = Flask(__name__)

	app.config.from_object(config[ConfigName])
	bootstrap.init_app(app)

	from .main import main
	app.register_blueprint(main)
	from .city import city
	app.register_blueprint(city, url_prefix='/city')
	from .job import job
	app.register_blueprint(job, url_prefix='/keyword')
	from .salary import salary
	app.register_blueprint(salary, url_prefix='/salary')


	return app