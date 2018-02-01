from flask import Flask , request ,jsonify
from flask_restful import Resource , Api,reqparse
import json ,time 

app = Flask (__name__)
api = Api(app) 

parser = reqparse.RequestParser()
parser.add_argument('file')
class Upload(Resource):
    def post(self, fname):
        file = request.files['file']
        if file:
            pass
        else:
            return {'False'}

class index(Resource):
	def get(self):
		return '<input type="file" name="file">'
Api.add_resource(Upload, '/upload/<string:fname>')
Api.add_resource(index,'/')
if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5000)