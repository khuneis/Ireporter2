from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy

# local import
<<<<<<< HEAD
from app.instance.config import app_config
=======
from instance.config import app_config
>>>>>>> 8faf1f06d2757cd848f7a089ad5d166810f65d09

# initialize sql-alchemy
db = SQLAlchemy()


def create_app(config_name):
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    return app