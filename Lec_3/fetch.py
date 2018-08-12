import os 	

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker

engine = create_engine(os.getenv("DATABASE_URL")) 
# DATABASE_URL="postgresql://postgres:root@localhost/test"

# engine = create_engine(DATABASE_URL) 

db = scoped_session(sessionmaker(bind=engine))


def main():
	flights = db.execute("SELECT origin,destination,duration FROM flights").fetchall()
	for i in flights:
		print("{origi} to {dest} Minutes {dur}".format(origi=i.origin,dest=i.destination,dur=i.duration))

if __name__ == "__main__":
	main()