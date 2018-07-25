from flask import Flask,render_template
import datetime

app = Flask(__name__)

@app.route("/")
def index():
	now = datetime.datetime.now()
	new_year = now.month == 1 and now.day == 1
	# new_year = 1
	# text = "Yes" if new_year else "NO"
	return render_template("index.html",new_year=new_year)
	# return render_template("index.html",text=text)