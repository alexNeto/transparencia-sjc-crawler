from flask import Flask
from flask_restful import Resource, Api

from headers import Headers

app = Flask(__name__)
api = Api(app)

class Index(Resource):
    @classmethod
    def get(self):
        return ""



api.add_resource(Index, '/')
api.add_resource(Headers, '/headers/<string:type>')

if __name__ == '__main__':
    app.run(debug=False)
