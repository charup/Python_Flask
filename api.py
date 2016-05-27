from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class CreateUser(Resource):
    def post(self):
        return {'status': 'success'}

api.add_resource(CreateUser, '/CreateUser')

if __name__ == '__main__':
    #app.run(debug=True)
	app.run(host = '0.0.0.0') # tell OS to listen to all public IP's

