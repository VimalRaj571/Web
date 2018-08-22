import csv
import os

# from sqlalchemy import create_engine
# from sqlalchemy.orm import scoped_session,sesssionmaker

# engine = create_engine(os.getenv("DATABASE_URL"))
# db = scoped_session(sesssionmaker(bind=engine))

from flask import Flask,request,render_template
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

def main():
	f = open("flights.csv")
	reader = csv.reader(f)
	for origin,destination,duration in reader:
		flight = Flight(origin=origin,destination=destination,duration=duration)
		db.session.add(flight)
		print("Added flights from {o} to {de} lasting {du}"
			.format(o=flight.origin,de=flight.destination,du=flight.duration))
	db.session.commit()	


if __name__ == "__main__":
	with app.app_context():
		main()