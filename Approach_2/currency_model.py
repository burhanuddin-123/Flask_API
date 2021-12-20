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

	def __init__(self):
		self.USD = 1.0
		self.INR = 75.8725
		self.EUR = 0.0886336
		self.GBP = 0.75665
		self.CNY = 6.3626
		self.JPY = 113.66525
		self.CAD = 1.28115
		self.AUD = 1.403125
		
	def save_to_db(self):
		db.session.add(self)
		db.session.commit()

	@classmethod
	def fetch_currecy(cls):
		return Currency_Table.query.all()