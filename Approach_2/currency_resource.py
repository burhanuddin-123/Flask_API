from flask import jsonify
from Approach_2.currency_model import Currency_Table
from flask_restful import Resource
import json

class Currency(Resource):
	def get(self):
		currency = Currency_Table.fetch_currecy()
		currency.save_to_db()
		for values in currency:
			final_list = [{
			"USD": values.USD, "INR": values.INR, "EUR": values.EUR,
			"GBP": values.GBP, "CNY": values.CNY, "JPY": values.JPY,
			"CAD": values.CAD, "AUD": values.AUD
			}]
		
		return jsonify({"currency": final_list})


######################## JSON #################
# JSON error:- https://www.datacamp.com/community/tutorials/json-data-python?utm_source=adwords_ppc&utm_medium=cpc&utm_campaignid=14989519638&utm_adgroupid=127836677279&utm_device=m&utm_keyword=&utm_matchtype=&utm_network=g&utm_adpostion=&utm_creative=332602034364&utm_targetid=aud-438999696719:dsa-429603003980&utm_loc_interest_ms=&utm_loc_physical_ms=9040245&gclid=Cj0KCQiA5OuNBhCRARIsACgaiqXqGTkus38wBxpVWjZBvpV15Y2UpLBYk3N7gwcn57l1vb60YARRqVUaAttbEALw_wcB

# from flask import jsonify
# from Approach_2.currency_model import Currency_Table
# from flask_restful import Resource
# import json


# class Currency(Resource):
# 	def get(self):
# 		# return "Hello World"
# 		currency = Currency_Table.fetch_currecy()
# 		# b = 5
		
# 		# this gives error
# 		# my_json_string = """{
#   #  			"article": [
# 	 #         "id": """+str(b)+""",
# 	 #         "language": "JSON",
# 	 #         "edition": "first",
# 	 #         "author": "Derrick Mwiti"
# 	 #      ]
#   #     	}
#   #     	"""

# 		# this gives o/p
# 		# my_json_string = """{
#   #  			"article": [
# 		#  {
# 	 #         "id": """+str(b)+""",
# 	 #         "language": "JSON",
# 	 #         "edition": "first",
# 	 #         "author": "Derrick Mwiti"
# 	 #      }
# 	 #      ]
#   #     	}
#   #     	"""

# 		for values in currency:
# 			final_list = [{
# 			"USD": values.USD, "INR": values.INR, "EUR": values.EUR,
# 			"GBP": values.GBP, "CNY": values.CNY, "JPY": values.JPY,
# 			"CAD": values.CAD, "AUD": values.AUD
# 			}]
			
# 		# 	# gives format error
# 		# 	final_list = f"""
# 		# 	"[
# 		# 	"USD": {values.USD}, "INR": {values.INR}, "EUR": {values.EUR},
# 		# 	"GBP": {values.GBP}, "CNY": {values.CNY}, "JPY": {values.JPY},
# 		# 	"CAD": {values.CAD}, "AUD": {values.AUD}
# 		# 	]"
# 		# 	""" 

# 			# my_json_string = {"currency": final_list}
# 			# print(my_json_string)

# 		# 	final_list = f"""[
# 		# 			"USD": {values.USD},
# 		# 			"INR": {values.INR},
# 		# 			"EUR": {values.EUR},
# 		# 			"GBP": {values.GBP},
# 		# 			"CNY": {values.CNY},
# 		# 			"JPY": {values.JPY},
# 		# 			"CAD": {values.CAD},
# 		# 			"AUD": {values.AUD},
# 		# 		]
# 		# 	"""

# 		# final_list_to_json = json.loads(my_json_string)
# 		# return final_list_to_json

		
# 		return jsonify({"currency": final_list})