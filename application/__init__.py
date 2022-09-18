"""Initialize Flask app."""
from flask import Flask


def create_app(config=None):
    app= Flask(__name__)

    if config is not None:
        app.config.from_object(config)
    from . import default
    app.register_blueprint(default.bp)
    return app
