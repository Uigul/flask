from flask import Flask, render_template
from flask import jsonify
import random

app = Flask(__name__)


def randomize_params():
    return (random.uniform(0, 100), random.uniform(0, 100), random.uniform(0, 100), random.uniform(0, 100))


@app.route("/")
def hello():
    return render_template("api.html")


@app.route("/v1/configuration/all")
def all_configurations():
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


@app.route("/v1/configuration/<name>", methods=['GET'])
def get_configutration(name=100):
    response = { "method": "GET",
                 "name": name,
                 "values":{
                     "Kp": random.uniform(0, 100),
                     "Ki": random.uniform(0, 100),
                     "Kd": random.uniform(0, 100),
                     "Tf": random.uniform(0, 100)
                 }
                }
    return jsonify(response)


@app.route("/v1/configuration/<name>", methods=['POST'])
def create_configutration(name=100):
    response = { "method": "POST",
                 "name": name,
                 "values":{
                     "Kp": random.uniform(0, 100),
                     "Ki": random.uniform(0, 100),
                     "Kd": random.uniform(0, 100),
                     "Tf": random.uniform(0, 100)
                 }
                }
    return jsonify(response)


@app.route("/v1/configuration/<name>", methods=['PUT'])
def modify_configutration(name=100):
    response = { "method": "PUT",
                 "name": name,
                 "values":{
                     "Kp": random.uniform(0, 100),
                     "Ki": random.uniform(0, 100),
                     "Kd": random.uniform(0, 100),
                     "Tf": random.uniform(0, 100)
                 }
                }
    return jsonify(response)


@app.route("/v1/configuration/<name>", methods=['DELETE'])
def delete_configutration(name=100):
    response = { "method": 'DELETE',
                 "name": name,
                 "values":{
                     "Kp": random.uniform(0, 100),
                     "Ki": random.uniform(0, 100),
                     "Kd": random.uniform(0, 100),
                     "Tf": random.uniform(0, 100)
                 }
                }
    return jsonify(response)