import os

from flask import Flask 
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy

from .utils import generate_basedir

bootstrap = Bootstrap()
db = SQLAlchemy()
moment = Moment()
sio = SocketIO()


def create_app(debug=False):
    """Application factory.
    
    :param debug: run application with debug mode.
    """
    app = Flask(__name__)
    app.secret_key = "8cwyja9fql"
    app.debug = debug
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(generate_basedir(), "database.sqlite")
    
    bootstrap.init_app(app)
    db.init_app(app)
    moment.init_app(app)
    sio.init_app(app)
    
    from .views import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    return app 
