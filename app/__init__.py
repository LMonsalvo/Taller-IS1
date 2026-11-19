import os

from flask import Flask

from app.blueprints.health import health_bp
from app.extensions import db, migrate


def create_app() -> Flask:
    app = Flask(__name__)

    db_url = os.getenv("DATABASE_URL", "sqlite:///app.db")
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    migrate.init_app(app, db)

    from models import pregunta, respuesta, usuario  # noqa: F401

    app.register_blueprint(health_bp)

    return app
