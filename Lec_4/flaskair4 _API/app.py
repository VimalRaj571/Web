import os
import json

from flask import Flask,request,render_template,jsonify
from models import *
# from sqlalchemy import create_engine
# from sqlalchemy.orm import scoped_session,sessionmaker

# engine = create_engine(os.getenv("DATABASE_URL"))
# db = scoped_session(sessionmaker(bind=engine))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

@app.route("/")
def slash():
	# db_table = db.execute("SELECT * FROM flights").fetchall()
	# print(db_table)
	flights = Flight.query.all()
	return render_template("index.html",flights = flights)

@app.route("/putdb",methods=["POST"])
def putdb():
	'''
	<!-- 
		## If want get the var from html to app.py
		## Get it using the name="variable"
		## variable in the tag < values >
		## If send to the app.py 
		## Use the same things name = value -->
	'''
	# In models.py we created the add_passenger in Class Flight:
	value = request.form.get("value")

	fli_id = request.form.get("flight.id")

	# Add using the Flight class
	flight.add_passenger(value)

	flight = Flight.query.get(fli_id)


	# print(fli_id,value)  DEBUG on terminal

	# r_c = db.execute("SELECT * FROM flights WHERE id=:id",{"id":fli_id}).rowcount

	# db.execute("INSERT INTO passengers (name,flight_id) VALUES (:value,:id)",
	# 	{"value" : value ,"id": fli_id })

	# pas_table = db.execute("SELECT * FROM passengers").fetchall()

	# db.commit()
	
	# Add pasenger using SQLAlchemy
	# passenger = Passenger(name=value,flight_id=fli_id)
	# # Add using the Passenger class
	# db.session.add(passenger)
	# db.session.commit()

	

	return render_template("sucess.html",value_sucess="You are registered Successfully") 

@app.route("/flights")
def flights():
	# flights = db.execute("SELECT * FROM flights").fetchall()
	
	# GET flights using SQLAlchemy
	flights = Flight.query.all()
	return render_template("flights.html",flights=flights)

@app.route("/flight/<int:flight_id>")
def flight(flight_id):
	#First html varibale and app.py variable
	# flight_table = db.execute("SELECT * FROM flights WHERE id = :id",
	# 	{"id":flight_id}).fetchone()

	# passengers_table = db.execute("SELECT name FROM passengers WHERE flight_id = :flight_id",
	# 	{"flight_id":flight_id}).fetchall()

	flight_table = Flight.query.get(flight_id)

	# passengers_table = Passenger.query.filter_by(flight_id=flight_id)

	# print(passengers_table,flight_table)
	passengers_table = flight_table.passengers

	return render_template("flight.html",flight = flight_table,passengers = passengers_table)

@app.route("/delent",methods=["POST"])
def delent():
	del_val = request.form.get("del_val")

	# db.execute("DELETE FROM passengers WHERE name=:name",
	#  	{"name" : del_val})

	# db.commit()

	# Delete using SQLAlchemy
	# First get the roe by following
	passenger = Passenger.query.filter_by(name=del_val).one()
	# Using that object get and delete that row
	# by following
	db.session.delete(passenger)
	db.session.commit()

	return render_template("del.html", val=del_val)

@app.route("/api/flights/<int:flight_id>")
def flightAPI(flight_id):
	"""Return detail about the single flights as JSON"""

	# Query the filght
	flight = Flight.query.get(flight_id)

	# Check the flight is exists
	if flight is None:
		return jsonify({"error" : "Invalid flight number"}),422

	# Get all passenger
	passengers = flight.passengers
	names = []
	for pasenger in passengers:
		names.append(pasenger.name)

	return jsonify({
		"origin" : flight.origin ,
		"destination": flight.destination ,
		"duration": flight.duration ,
		"passengers": names
		}),200