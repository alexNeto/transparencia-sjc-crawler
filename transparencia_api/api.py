from flask import Flask
from flask_restful import Resource, Api

from transparencia_api.commons.database_communication import DatabaseCommunication

app = Flask(__name__)
api = Api(app)
db = DatabaseCommunication().connect()


class Index(Resource):
    @classmethod
    def get(cls):
        return ""


api.add_resource(Index, '/')

if __name__ == '__main__':
    app.run(debug=True)
