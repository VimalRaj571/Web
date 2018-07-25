from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
	names = ['alice','bob','john','Mac','Air']
	return render_template("index.html",names=names)
