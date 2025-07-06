from flask import Flask

app=Flask(__name__)
@app.route("/info")
def lwinfo():
	return "I am mhk"

@app.route("/phone")
def lwphone():
	return "8559800000"

app.run(host="0.0.0.0")
