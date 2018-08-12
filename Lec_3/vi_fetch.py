import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


def main():

	flights = db.execute("SELECT origin,destination,duration FROM flights ").fetchall()

	for flight in flights:
		print(flight.origin,flight.destination,flight.duration)

	i = input("Enter Destination ")

	# out = flights = db.execute("SELECT origin FROM flights WHERE duration = :value",{"value":i}).fetchone()

	out = flights = db.execute("SELECT origin,destination FROM flights WHERE destination = :value",{"value":i}).fetchall()
	# out = flights = db.execute("SELECT origin FROM flights WHERE duration = :value",{"value":i}).fetchone()

	print(out)

if __name__ == "__main__":
	main()