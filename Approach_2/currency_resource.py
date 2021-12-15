from flask import jsonify
from Approach_2.currency_model import Currency_Table
from flask_restful import Resource

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