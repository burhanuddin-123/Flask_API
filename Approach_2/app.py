from flask import Flask,jsonify,request
from flask_restful import Resource, Api, reqparse
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///converter.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)

db = SQLAlchemy()

def create_tables():
    db.create_all()

class Currency_Table(db.Model):
	__tablename__ = "currencies"

	id = db.Column(db.Integer, primary_key=True)
	USD = db.Column(db.Float)
	INR = db.Column(db.Float)
	EUR = db.Column(db.Float)
	GBP = db.Column(db.Float)
	CNY = db.Column(db.Float)
	JPY = db.Column(db.Float)
	CAD = db.Column(db.Float)
	AUD = db.Column(db.Float)

	@classmethod
	def fetch_currecy(cls):
		return Currency_Table.query.all()

class Currency(Resource):
	def get(self):
		# return "Hello World"
		currency = Currency_Table.fetch_currecy()
		for values in currency:
			final_list = [{
			"USD": values.USD, "INR": values.INR, "EUR": values.EUR, 
			"GBP": values.GBP, "CNY": values.CNY, "JPY": values.JPY,
			"CAD": values.CAD, "AUD": values.AUD
			}]
		return jsonify({"currency": final_list})

api.add_resource(Currency, '/currency')

if __name__ == '__main__':
	db.init_app(app)
	app.run(debug=True)