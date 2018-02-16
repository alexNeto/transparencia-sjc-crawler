from flask import Flask
from flask_restful import Resource, Api

from titulos import *

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return linhas()


api.add_resource(HelloWorld, '/')
api.add_resource(Titulos, '/a')

if __name__ == '__main__':
    app.run(debug=True)
