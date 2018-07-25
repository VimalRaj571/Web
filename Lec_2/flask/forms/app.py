from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/hello", methods=["POST","GET"])
def hello():
	if request.method == "GET":		#method instead methods
		return "Enter the form instead on here <a href=\"/\">Form</a> "  
	else:
		name = request.form.get("name")
		return render_template("hello.html",name=name)	