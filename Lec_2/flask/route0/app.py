from flask import Flask

app_variable = Flask(__name__)

@app_variable.route("/")
def Hello():
	return "This is app 2"

@app_variable.route("/Hey")
def Hey():
	return "Hey!!!"	
