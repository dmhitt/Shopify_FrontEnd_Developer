from flask import Flask, render_template, redirect

import nasa
from flask import send_from_directory
import os
import json
from bson import json_util


app = Flask(__name__)



@app.route("/")
def home():
	
	nasa_data = {'result' : nasa.api_call()}
	# print ("nasa_data 1 = ",nasa_data)
	return render_template("index.html", api_data = nasa_data)



@app.route("/data")
def nasa_data():
    nasa_data = {'result' : nasa.api_call()}
    # print ("nasa_data 2 = ", nasa_data)
    return json.loads(json_util.dumps(nasa_data))

if __name__ == "__main__":
	app.run(debug=True)	