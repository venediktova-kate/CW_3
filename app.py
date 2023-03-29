from flask import Flask

from api import api_bp
from db import db
from views import main_bp


def create_app(config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    app.register_blueprint(api_bp)
    app.register_blueprint(main_bp)
    return app
