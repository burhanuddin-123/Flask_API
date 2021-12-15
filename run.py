from app import app
from Approach_2.currency_model import db

db.init_app(app)

# create tables
@app.before_first_request
def create_tables():
    db.create_all()
