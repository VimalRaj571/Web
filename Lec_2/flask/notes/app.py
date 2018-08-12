#!/usr/bin/python2
import os
from flask import Flask, render_template, request, session
#from flask.sessions import Session     # flask.sessions
#from flask.ext.session import Session
from flask_session import Session

app = Flask(__name__)    #name

app.config["SESSION_PERMANET"] = False
app.config["SESSION_TYPE"] = "filesystem"

Session(app)

#app.secret_key = "super secret key"

notes = []

@app.route("/V")
def version():
	return os.sys.version

@app.route("/",methods=["GET","POST"])
def index():
	if session.get("notes") is None:
		session["notes"] = []
	elif request.method == "POST":
		note = request.form.get("note")
		session["notes"].append(note)
	return render_template("index.html",notes=session["notes"]) #First app.py variable
	#return render_template("index.html",notes=notes)			#second html notes variable