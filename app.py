from flask import Flask, render_template, jsonify, request
from flask_bootstrap import Bootstrap
import json
import os

# DATA
my_dir = os.path.dirname(__file__)
with open(os.path.join(my_dir, 'data.json')) as f:
    data = json.load(f)['records']

# APP
app = Flask(__name__)
Bootstrap(app)

@app.route("/")
def home():
	return render_template("index.html", response=data[0])

@app.route("/about")
def about():
	return render_template("about.html")

@app.route("/get")
def get_bot_response():
	key = request.args.get('key')
	records = [r for r in data if r['question'] == key]
	if len(records) > 0:
		record = records[0]
	else:
		record =  {
		"question": "bye",
			"answer": {
			"text": "Bye human! It was great to talk to you!",
			"image": "bye.gif"
			}
		}
	return jsonify(record)

if __name__ == "__main__":
	app.run()
