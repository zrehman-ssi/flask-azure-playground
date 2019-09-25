from flask import Blueprint
from flask_restful import Api

from app.main.controllers.user_controller import Hello

blueprint = Blueprint("api", __name__)
api = Api(blueprint)

api.add_resource(Hello, '/', '/')