from flask_restful import Resource, reqparse
from flask import current_app

class Match(Resource):

    def post(self):
        dataBase = current_app._get_current_object().DB
        collection = dataBase["matches_collection"]

        parser = reqparse.RequestParser()
        parser.add_argument("match")
        args = parser.parse_args()

        id = collection.count() + 1
        post = {
            "id": id,
            "match" : args["match"]
        }
        
        collection.insert(post)
        
        return "OK",202
       