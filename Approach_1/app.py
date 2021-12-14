from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse
import requests
from bs4 import BeautifulSoup
import pandas as pd

app = Flask(__name__)

api = Api(app)

class Converter(Resource):
	def get(self):
		data = request.get_json()
		url = f'https://www.calculator.net/currency-calculator.html?eamount={data["value"]}&efrom=USD&eto={data["currency"]}&ccmajorccsettingbox=1&type=1&x=0&y=0'
		page = requests.get(url)
		soup = BeautifulSoup(page.content,"html.parser")
		x = soup.find_all('p',class_='verybigtext')
		htmlcontent = soup.prettify()

		for i in x:
			fetch_currency = i.get_text()

		start_amount_1 = fetch_currency.find("USD = ")+len("USD = ")
		split_amount = fetch_currency.find(" ", start_amount_1)
		amount_1 = fetch_currency[start_amount_1:split_amount]

		start_amount_2 = fetch_currency.find(f"{data['currency']} = ")+len(f"{data['currency']} = ")
		split_amount = fetch_currency.find(" ", start_amount_2)
		amount_2 = fetch_currency[start_amount_2:split_amount]

		## was facing error in this

		# usd_amount = []
		# for i in range(len(fetch_date)):
		# 	if i==1 or i==5:
		# 		amount = list(fetch_date[i].children)
		# 		print(amount)
		# 		final_amount = amount.contents
		# 		print(final_amount)
		# 		usd_amount.append(fetch_date[i])
		# print(usd_amount)

		return jsonify({f"{data['value']} USD": amount_2+" "+data['currency'], f"{data['value']} {data['currency']}": amount_1+" USD"})

api.add_resource(Converter, '/converter')

if __name__ == '__main__':
	app.run(debug=True)