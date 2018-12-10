from flask_restful import Resource, reqparse
from flask import current_app

class Hello(Resource):

    def get(self):
        return "OK",202