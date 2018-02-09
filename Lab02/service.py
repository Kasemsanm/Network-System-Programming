import pymongo
from flash import Flask,request
from flash_restful import Resource , Api,reqparse


url = "mongodb://munu:test1234@139.59.234.0:27017/admin"
client = pymongo.MongoClient(url)

app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()
parser.add_argument('information')

class Registration(Resource):
  def post(self):
    args = parser.parse_args()
    data = args['information']
    print(data)
    return {"data":data}

api.add_resource(Registeration,'/api/regis')

if __name__ == '__main__': 
  app.run(host='0.0.0.0',port=5565)
