from flask import Flask, jsonify, request
from dao import Dao
import json
app = Flask(__name__)


@app.route("/configuration-list/all")
def configuration_list():
    dao = Dao()
    response = []
    for i in  dao.get_all_lists():
        response.append(json.loads(i.__repr__()))
    return jsonify(response)


@app.route("/configuration-list/details/<name>")
def single_configuration(name):
    dao = Dao()
    response = json.loads(dao.get_list_by_name(name).__repr__())
    return jsonify(response)


@app.route("/configuration-list/sensors/name/<name>")
def single_configuration_sensors_by_name(name):
    dao = Dao()
    response = json.loads(dao.get_sensor_by_name(name).__repr__())
    return jsonify(response)


@app.route("/configuration-list/sensors/id/<id>")
def single_configuration_sensors_by_id(id):
    dao = Dao()
    response = json.loads(dao.get_sensor_by_id(id).__repr__())
    return jsonify(response)


@app.route("/configuration-list/new", methods=['POST'])
def create_configutration():
    data = json.loads(request.data)
    dao = Dao()
    dao.create_list(data['name'])
    return "CREATED"


#TODO THIS ENDPOINT SHOULD DELETE LIST, TEMPORARY DO NOTHING
@app.route("/configuration-list/delete/<id>", methods=['DELETE'])
def delete_configutration(id):
    dao = Dao()
    dao.delete_list(id)
    return "DELETED"


@app.route("/configuration-list/sensors/update/<id>/<sensor>", methods=['PATCH'])
def update_single_sensor(id, sensor):
    data = json.loads(request.data)
    dao = Dao()
    dao.update_sensor(id, sensor, data['values']['Kp'], data['values']['Ki'],
                      data['values']['Ki'], data['values']['Tf'])
    return "UPDATED"

