import os,json
from flask import Flask,render_template,request,jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker
from flask_session import Session

engine = create_engine(os.getenv("DATABASE_URL_2"))
db = scoped_session(sessionmaker(bind=engine))

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)



@app.route("/")
def main():
	return render_template("index.html")


@app.route("/login",methods=["POST","GET"])
def login():
	if request.method == "POST":
		session["user_id"] = request.form.get('uname')
	else:
		return render_template("index.html")


@app.route("/register")
def register():
	return render_template("register.html")

@app.route("/rpost",methods=["POST"])
def rpost():
	name = request.form.get('name')
	email = request.form.get('email')
	password = request.form.get('pass')
	print(name,email,password)
	return render_template("index.html")

@app.route("/search",methods=["POST"])
def search():
	uname = request.form.get('uname')
	pword = request.form.get('pword')

	usr_is = db.execute("SELECT name FROM users WHERE name=:uname",
		{ "uname" : uname }).fetchone()
	pword_is = db.execute("SELECT password FROM users WHERE password=:pword",
		{ "pword" : pword }).fetchone()

	if usr_is != None:
		if pword_is != None:
			u_p = db.execute("SELECT name FROM users WHERE name=:uname AND password=:pword",
			{ "uname" : uname , "pword" : pword }).fetchone()
			if u_p != None:
				return render_template("searchbook.html")
			else:
				return "User name password not found"
		else:
			return "password is worng"
	else:
		return render_template("err.html")

@app.route("/listbook")
def listbook():
	return render_template("listbook.html")

@app.route("/bookdetail",methods=["POST"])
def bookdetail():
	isbn = request.form.get('isbn')
	title = request.form.get('title')
	author = request.form.get('author')
	print(isbn,title,author)

	if isbn == '' and title == '' and author == '':
		return "Enter Atmost One"
	# isbn_var = db.execute("SELECT isbn,title,author,year FROM books WHERE isbn=:isbn",
	# 	{ "isbn" : isbn }).fetchone()
	

	# List all the book mactched things title,authour


	if isbn != '':
		isbn_var = db.execute("SELECT isbn,title,author,year FROM books WHERE isbn=:isbn",
		{ "isbn" : isbn }).fetchone()
		if isbn_var == None:
			return render_template("err.html")
		return render_template("details.html", detail=isbn_var)

	elif title != '':
		title_var = db.execute("SELECT isbn,title,author,year FROM books WHERE title=:title",
		{ "title" : title }).fetchone()
		if title_var == None:
			return render_template("err.html")
		return render_template("details.html", detail=title_var)

	elif author != '':
		author_var = db.execute("SELECT isbn,title,author,year FROM books WHERE author=:author",
		{ "author" : author }).fetchone()
		if author_var == None:
			return render_template("err.html")
		return render_template("details.html", detail=author_var)

	


@app.route("/addreview",methods=["POST"])
def addreview():
	user = request.form.get('name')
	book_id = request.form.get('bookid')
	rate = request.form.get('rate')
	review = request.form.get('review')
	userid = db.execute("SELECT id FROM users WHERE name=:user",
		{"user" : user }).fetchone()
	print(userid,userid[0])
	print(user,book_id,review,rate)
	row = db.execute("SELECT user_id FROM reviews WHERE user_id=:userid AND book_id =:bookid",
		{"userid" : userid[0],"bookid" : book_id}).rowcount
	print(row)
	if userid != None and row == 0:
		db.execute("INSERT INTO reviews (review,rating,book_id,user_id) VALUES (:review,:rating,:bookid,:userid)",
			{"review" : review ,"rating": rate,"bookid" : book_id ,"userid" : userid[0] })
	return "hkjhk"


@app.route("/book/<string:isbn>")
def book(isbn):
	isbn_var = db.execute("SELECT isbn,title,author,year FROM books WHERE isbn=:isbn",
		{ "isbn" : isbn }).fetchone()
	review_is = db.execute("SELECT review,user_id FROM reviews WHERE book_id=:isbn",
	 	{ "isbn" : isbn }).fetchall()
	review_count = db.execute("SELECT COUNT(book_id) FROM reviews WHERE book_id=:isbn",
		{ "isbn" : isbn }).fetchone()
	average_score = db.execute("SELECT SUM (rating) AS total FROM reviews WHERE book_id =:isbn",
		{ "isbn" : isbn }).fetchone()
	user_rev = {}
	for review,userid in review_is:
		# print(userid,review)
		user = db.execute("SELECT name FROM users WHERE id=:uname",
			{ "uname" : userid }).fetchone()
		user_rev[user[0]] = review
	# print(user_rev)
	# print(review_count[0])
	avg = average_score[0]/review_count[0]
	# print(average_score,review_count,avg)
	return render_template('detailbook.html',book=isbn_var ,review=review_is, avg=avg,user_rev=user_rev,count=review_count[0])

@app.route("/api/<string:isbn>")
def apiisbn(isbn):
	''' 
	{
    "title": "Memory",
    "author": "Doug Lloyd",
    "year": 2015,
    "isbn": "1632168146",
    "review_count": 28,
    "average_score": 5.0
	}

	'''
	isbn_var = db.execute("SELECT isbn,title,author,year FROM books WHERE isbn=:isbn",
		{ "isbn" : isbn }).fetchone()
	review_count = db.execute("SELECT COUNT(book_id) FROM reviews WHERE book_id=:isbn",
		{ "isbn" : isbn }).fetchone()
	sum_score = db.execute("SELECT SUM (rating) AS total FROM reviews WHERE book_id =:isbn",
		{ "isbn" : isbn }).fetchone()

	if isbn_var == None:
		return jsonify({ "error" : "book is not found" }),422

	print(sum_score,review_count)
	
	if sum_score == None:
		avg = sum_score[0]/review_count[0]
	else:
		avg = review_count[0]

	return jsonify({
		"title" : isbn_var.title,
		"author" : isbn_var.author,
		"year" : isbn_var.year,
		"isbn" : isbn_var.isbn,
		"review_count" : review_count[0],
		"average_score" : avg
		}),200

	# return "API Endpoint"