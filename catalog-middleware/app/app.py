from flask import Flask, send_from_directory
from flask_restful import Resource, Api
from flask_cors import CORS
from flask import render_template

app = Flask(__name__)
CORS(app)

api = Api(app)

from api.catalog import Catalog
api.add_resource(Catalog, '/catalog', '/catalog/search')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
