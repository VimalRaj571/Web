import os

from flask import Flask,request,render_template
from models import *

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

def main():
	# flights = Flight.query.all()
	# for flight in flights:
	# 	print("{o} to {de} lasting {du}".format(o=flight.origin,de=flight.destination,du=flight.duration))

	# # SELECT * FROM flights
	# fl = Flight.query.all()
	# for i in fl:
	# 	print(i.origin,i.destination,i.duration)

	# # SELECT * FROM flights WHERE origin = 'Paris';
	# a = Flight.query.filter_by(origin="Paris").all()
	# print(a.origin,a.destination,a.duration)

	# # SELECT * FROM flights WHERE origin = 'Paris' LIMIT 1;
	# b = Flight.query.filter_by(origin='Paris').first()
	# print(b.origin,b.destination,b.duration)

	# # SELECT COUNT(*) FROM flights WHERE origin = 'Paris';
	# c = Flight.query.filter_by(origin='Paris').count()
	# print(c)

	# # SELECT * FROM flights WHERE id=28
	# d=Flight.query.filter_by(id=23).first()
	# e=Flight.query.get(23)
	# print(d,e)

	# # UPDATE flights SET duration = 280 WHERE id = 6;
	# flight = Flight.query.get(6)
	# flight.duration = 280

	# # DELETE FROM flights WHERE id = 28;
	# flight = Flight.query.get(28)
	# db.session.delete(flight)

	# # COMMIT;
	# db.session.commit()

	# SELECT * FROM flights WHERE origin = "Paris" OR duration > 500;
	# f=Flight.query.filter(or_(Flight.origin == 'Paris',
	# 						Flight.duration > 500 )).all()
	# print(f)

	z = db.session.query(Flight,Passenger).filter(Flight.id == Passenger.id).all()
	print(z)
if __name__ == '__main__':
		with app.app_context():
			main()