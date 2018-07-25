from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index_var():
	headline = "Hii"
	return render_template("index.html",headline = headline)

@app.route("/Bye")
def bye():
	headline = "Good Bye!!!"
	return render_template("index.html",headline = headline)

if __name__ ==  "__main__":
	app.run(debug=True)
