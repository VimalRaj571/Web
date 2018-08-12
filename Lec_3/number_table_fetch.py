from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker

engine = create_engine("postgresql://vimal:vimal@localhost/postgres")
db = scoped_session(sessionmaker(bind=engine))

data = db.execute("SELECT * FROM number").fetchall()
for val in data:
	print(" %s "%val)