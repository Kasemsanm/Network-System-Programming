from flask import Flask , request ,jsonify
from flask_restful import Resource , Api,reqparse
import json ,time 

app = Flask (__name__)
api = Api(app) 

parser = reqparse.RequestParser()
parser.add_argument('ID',type=str)
class BinaryId(Resource):
	def post(self):
		args = parser.parse_args()
		ID = str(args['ID'])
        result = ""
        for x in ID:
            result += str(bin(int(x)))
		return jsonify(BinaryId = result)
api.add_resource(BinaryId,'/')

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5000)