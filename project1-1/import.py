import os
import csv

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker

engine = create_engine(os.getenv("DATABASE_URL_2"))
db = scoped_session(sessionmaker(bind=engine))

def main():
	f = open("books.csv")
	reader = csv.reader(f)
	header = next(reader)
	for isbn,title,author,year in reader:
		db.execute("INSERT INTO books (isbn,title,author,year) VALUES (:isbn,:title,:author,:year)",
			{ "isbn" : isbn , "title" : title, "author" : author , "year" : year})
		print("The following {isbn} {title} {author} {year} are inserted into Database".format(isbn=isbn,title=title,author=author,year=year))
	db.commit()
if __name__ == '__main__':
	main()