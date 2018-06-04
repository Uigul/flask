from flask import Flask, jsonify, request
from dao import Dao
import json
app = Flask(__name__)


@app.route("/configuration-list/all")
def configuration_list():
    dao = Dao()
    response = []
    for i in dao.get_all_lists():
        response.append(json.loads(i.__repr__()))
    return jsonify(response)


@app.route("/configuration-list/details/<id>")
def single_configuration(id):
    dao = Dao()
    response = json.loads(dao.get_list_by_id(id).first().__repr__())
    return jsonify(response)


@app.route("/configuration-list/sensors/<id>")
def single_configuration_sensors_by_id(id):
    dao = Dao()
    response = json.loads(dao.get_sensor_by_id(id).__repr__())
    return jsonify(response)


@app.route("/configuration-list/new", methods=['POST'])
def create_configutration():
    print(request.json)
    data = request.json
    dao = Dao()
    dao.create_list(data['name'])
    return "CREATED"


@app.route("/configuration-list/delete/<id>", methods=['DELETE'])
def delete_configutration(id):
    dao = Dao()
    print(type(id))
    dao.delete_list(id)
    return "DELETED"


@app.route("/configuration-list/sensors/<id>/<sensor>", methods=['PATCH'])
def update_single_sensor(id, sensor):
    data = request.json
    dao = Dao()
    dao.update_sensor(id, sensor, data['values']['Kp'], data['values']['Ki'],
                      data['values']['Ki'], data['values']['Tf'])
    return "UPDATED"
