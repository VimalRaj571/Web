from flask import Flask

apppy = Flask(__name__)

@apppy.route("/")
def Slash():
	return "/"

@apppy.route("/<string:name>")     #String(Type) name(variable name)
def greet(name):
	name = name.capitalize()
	return "<h1>Hey {}</h1>".format(name.capitalize())

#@apppy.route("/<integer:number>")
#def print_Number(number):
#	return "This is {}".format(number)
