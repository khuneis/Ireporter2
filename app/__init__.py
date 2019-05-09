from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy
<<<<<<< HEAD

# local import
from app.instance.config import app_config
=======
from flask import request, jsonify, abort
# local import
from instance.config import app_config
>>>>>>> 8faf1f06d2757cd848f7a089ad5d166810f65d09

# initialize sql-alchemy
db = SQLAlchemy()

<<<<<<< HEAD
from flask import request, jsonify, abort

def create_app(config_name):
    from app.api.v1.models.models import Ireporter
=======

def create_app(config_name):
    from app.api.v1.models.models import Ireporter2
>>>>>>> 8faf1f06d2757cd848f7a089ad5d166810f65d09
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
<<<<<<< HEAD

    return app

    @app.route('/ireporter', methods=['POST', 'GET'])
=======
    

    @app.route('/api/v1/ireporter2/', methods=['POST', 'GET'])
>>>>>>> 8faf1f06d2757cd848f7a089ad5d166810f65d09
    def ireporter():
        if request.method == "POST":
            name = str(request.data.get('name', ''))
            if name:
                ireporter = Ireporter(name=name)
                ireporter.save()
                response = jsonify({
                    'id': ireporter.id,
                    'name': ireporter.name,
                    'date_created': ireporter.date_created,
                    'date_modified': ireporter.date_modified
                })
                response.status_code = 201
                return response
        else:
            # GET
<<<<<<< HEAD
            ireporter = Ireporter.get_all()
            results = []

            for ireporter in Ireporters:
=======
            Ireporter2 = Ireporter.get_all()
            results = []

            for ireporter in Ireporter2:
>>>>>>> 8faf1f06d2757cd848f7a089ad5d166810f65d09
                obj = {
                    'id': ireporter.id,
                    'name': ireporter.name,
                    'date_created': ireporter.date_created,
                    'date_modified': ireporter.date_modified
                }
                results.append(obj)
            response = jsonify(results)
            response.status_code = 200
            return response

<<<<<<< HEAD
    return app 
=======
    return app
>>>>>>> 8faf1f06d2757cd848f7a089ad5d166810f65d09
