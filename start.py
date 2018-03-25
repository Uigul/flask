from flask import Flask, render_template
from flask import jsonify
import random

app = Flask(__name__)


def randomize_params():
    return (random.uniform(0, 100), random.uniform(0, 100), random.uniform(0, 100), random.uniform(0, 100))


@app.route("/")
def hello():
    return render_template("api.html")

@app.route("/parameters/all")
def all_parameters():
    response = []
    for i in ("pitch", "roll", "thrust", "yaw"):
        response.append({ "name": i,
                 "values":{
                     "Kp": random.uniform(0, 100),
                     "Ki": random.uniform(0, 100),
                     "Kd": random.uniform(0, 100),
                     "Tf": random.uniform(0, 100)
                 }
                })
    return jsonify(response)


@app.route("/parameters/<name>")
def get_sensor(name=100):
    response = { "name": name,
                 "values":{
                     "Kp": random.uniform(0, 100),
                     "Ki": random.uniform(0, 100),
                     "Kd": random.uniform(0, 100),
                     "Tf": random.uniform(0, 100)
                 }
                }
    return jsonify(response)

@app.route("/configuration/all")
def get_all_configuration():
    return "hello"

@app.route("/configuration", methods=['GET', 'POST', 'PUT'])
def manage_configurations():
    return "siema"