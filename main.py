from flask import Flask
from flask_restx import Api

from app.config import Config
from app.dao.model.user import User
from app.setup_db import db
from app.views.directors import director_ns
from app.views.genres import genre_ns
from app.views.movies import movie_ns
from app.views.user import user_ns
from app.views.auth import auth_ns


def create_app(config_object):
    application = Flask(__name__)
    application.config.from_object(config_object)
    application.app_context().push()
    register_extensions(application)

    return application

def register_extensions(application):
    db.init_app(application)
    api = Api(application)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(movie_ns)
    api.add_namespace(user_ns)
    api.add_namespace(auth_ns)
    create_data(application, db)

def create_data(app, db):
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    app_config = Config()
    app = create_app(app_config)
    app.run(host="localhost", port=10001, debug=True)
