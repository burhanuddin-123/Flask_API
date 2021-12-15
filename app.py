from flask import Flask
from flask_restful import Api

## Importing resources
from Approach_1.converter import Converter
from Approach_2.currency_resource import Currency

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///converter.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)

api.add_resource(Currency, '/currency')
api.add_resource(Converter, '/converter')

if __name__ == '__main__':
	from Approach_2.currency_model import db
	db.init_app(app)
	app.run(debug=True)