from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

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