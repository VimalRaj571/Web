import os 	
import csv

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker

engine = create_engine(os.getenv("DATABASE_URL")) 
# DATABASE_URL="postgresql://postgres:root@localhost/test"

# engine = create_engine(DATABASE_URL) 

db = scoped_session(sessionmaker(bind=engine))

def main():
	f = open("flights.csv")
	reader = csv.reader(f)
	#print(reader)
	# reader obj
	for origin,destination,duration in reader:
		db.execute("INSERT INTO flights (origin,destination,duration) VALUES (:origin,:destination,:duration)",
			{"origin":origin,"destination":destination,"duration":duration})
		print("Added from {o} to {des} minutes {dur}".format(o=origin,des=destination,dur=duration))
		db.commit()


if __name__ == "__main__":
	main()