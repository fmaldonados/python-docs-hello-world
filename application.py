from flask import Flask
app = Flask(__name__)
import pymongo

URI = "mongodb://proyecto:1g1bO6iQ6iotdK3ncd5f3ud5YPmTCACu19ugCeoXLjuF3Zjciqygzlu7wu8exeNq9z7CuT4V4URNdPeEjAVrcw==@proyecto.documents.azure.com:10255/?ssl=true&replicaSet=globaldb"
client = pymongo.MongoClient(URI)
app.DB = client["chess"]
print ("Connected to Database")

@app.route("/")
def hello():
    return "Hello World!"