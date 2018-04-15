from dao import Base, Dao
import argparse
from sqlalchemy import create_engine
import random

parser = argparse.ArgumentParser(description="Script creating new database refer to schema in quadrocopter/sqlite")
parser.add_argument("-n", help="create database without filling it with example data", action='store_true')
args = parser.parse_args()

print("Creating database")
engine = create_engine('sqlite:///db.sqlite', echo=True)
Base.metadata.create_all(engine)

if not args.n:
    print("Filling database with example data")
    dao = Dao()
    configuration_names = ["Nicolas", "Cage", "Big Daddy"]
    for name in configuration_names:
        dao.add_configuration(name)

    sensor_names = ["Pitch", "Roll", "Yaw", "Thrust"]
    for i in range(1, 4):
        for name in sensor_names:
            dao.add_sensor(name, i)
            # dao.add_sensor(name, i, kp=random.uniform(0, 100), ki=random.uniform(0, 100),
            #                kd=random.uniform(0, 100), tf=random.uniform(0, 100))