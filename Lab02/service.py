import pymongo
from flash import Flask,request
from flash_restful import Resource , Api,reqparse

url = "mongodb://[usermame]:[password]@[host]:[port]"
client = pymongo.MongoClient(url)

app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()

