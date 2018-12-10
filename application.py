from flask import Flask
from flask_restful import Api,Resource
import pymongo
from controllers.Match import Match
from controllers.Hello import Hello

app = Flask(__name__)

URI = "mongodb://proyecto:1g1bO6iQ6iotdK3ncd5f3ud5YPmTCACu19ugCeoXLjuF3Zjciqygzlu7wu8exeNq9z7CuT4V4URNdPeEjAVrcw==@proyecto.documents.azure.com:10255/?ssl=true&replicaSet=globaldb"
client = pymongo.MongoClient(URI)
app.DB = client["chess"]
print "Connected to Database"

#Routes
api = Api(app)
api.add_resource(Match,"/match")
api.add_resource(Hello,"/")

app.run(debug=True)