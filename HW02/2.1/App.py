from flask import Flask , request ,jsonify
from flask_restful import Resource , Api,reqparse
import json ,time 

app = Flask (__name__)
api = Api(app) 

parser = reqparse.RequestParser()
parser.add_argument('Date',type=str)
class CalBD(Resource):
	def post(self):
		args = parser.parse_args()
		Date = str(args['Date'])
		self.SubDate = (Date.split(":"))
		return jsonify(birthdate = Date,age = self.calDate())
	def calDate(self):
		age = time.gmtime().tm_year - int(self.SubDate[2])
		if(int(self.SubDate[1]) > time.gmtime().tm_mon):
			age -= 1;
		return age
api.add_resource(CalBD,'/calbd')

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5000)