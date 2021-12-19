from flask import Flask
from flask_restful import Api

## Importing resources
from Approach_1.converter import Converter
from Approach_2.currency_resource import Currency
import os

app = Flask(__name__)

# fetch connection strings
uri = os.environ.get('DATABASE_URL', 'sqlite:///new_data.db')  # or other relevant config var
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)
# rest of connection code using the connection string `uri`

app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)

api.add_resource(Currency, '/currency')
# api.add_resource(Converter, '/converter')

if __name__ == '__main__':
	app.run(debug=True)