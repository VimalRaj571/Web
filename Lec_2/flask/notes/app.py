from flask import Flask, render_template, request, session
#from flask.sessions import Session     # flask.sessions
#from flask.ext.session import Session

app = Flask(__name__)    #name

app.config["SESSION_PERMANET"] = False
app.config["SESSION_TYPE"] = "filesystem"
#Session(app)

notes = []

@app.route("/",methods=["GET","POST"])
def index():
	# session["notes"] = []
	if request.method == "POST":	
		note = request.form.get("note")
		notes.append(note)

	# return render_template("index.html",notes=session["notes"]) #First app.py variable
	return render_template("index.html",notes=notes)			#second html notes variable