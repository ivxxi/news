from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from app.models import Class
from app.requests import get_articles, get_sources, topheadlines

bootstrap = Bootstrap()

def create_app(config_name):
    app = Flask(__name__)

    # Creating app configurations
    app.config.from_object(config_options[config_name])

    # Initializing Flask Extensions
    bootstrap.init_app(app)

    # # Setting the config
    from .requests import configure_request
    configure_request(app)


    return app
