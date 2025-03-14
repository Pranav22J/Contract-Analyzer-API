from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from openai import OpenAI
from config import Config
from routes.routes import contract_analyzer, generate_api_key

app = Flask(__name__)
api = Api(app)

api.add_resource(contract_analyzer, '/contract_analyzer/<string:text_file>')
api.add_resource(generate_api_key, '/generate_api_key/<string:email>')

if __name__=="__main__":
    app.run(debug=True)