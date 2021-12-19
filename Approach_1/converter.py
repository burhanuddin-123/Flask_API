from flask import jsonify, request
from flask_restful import Resource
import requests
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup
from urllib.error import URLError

class Converter(Resource):
	def get(self):
		# data = request.get_json()
		data = request.args.get()
		if not data:
			return jsonify({"msg": "Pass the parameters"})
		
		# if both or one of the value is not there, except block will be called
		try:
			currency = data["currency"]
			value = data["amount"]
		except KeyError:
			return jsonify({"msg": "Pass both the currency and amount value"})


		url = f'https://www.calculator.net/currency-calculator.html?eamount={value}&efrom=USD&eto={currency}&ccmajorccsettingbox=1&type=1&x=0&y=0'

		try:
			page = requests.get(url)
		except URLError as error:
			return jsonify({"error": "Server not found"})
		except ConnectionError as error:
			return jsonify({"error": "Please Check your internet connection"})

		soup = BeautifulSoup(page.content,"html.parser")
		x = soup.find_all('p',class_='verybigtext')
		htmlcontent = soup.prettify()

		for i in x:
			fetch_currency = i.get_text()

		start_amount_1 = fetch_currency.find("USD = ")+len("USD = ")
		split_amount = fetch_currency.find(" ", start_amount_1)
		amount_1 = fetch_currency[start_amount_1:split_amount]

		start_amount_2 = fetch_currency.find(f"{currency} = ")+len(f"{currency} = ")
		split_amount = fetch_currency.find(" ", start_amount_2)
		amount_2 = fetch_currency[start_amount_2:split_amount]

		return jsonify({f"{value} USD": amount_2+" "+currency, f"{value} {currency}": amount_1+" USD"})