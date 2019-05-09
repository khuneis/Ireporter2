from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy
from flask import request, jsonify, abort
# local import
from instance.config import app_config

# initialize sql-alchemy
db = SQLAlchemy()

def create_app(config_name):
    from app.api.v1.models.models import Ireporter
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    return app
    
    @app.route('/api/v1/ireporter/', methods=['POST', 'GET'])
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
            ireporter = Ireporter.get_all()
            results = []

            for ireporter in Ireporter:
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

    return app
