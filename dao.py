import sqlite3
from sqlalchemy import create_engine, delete
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import sessionmaker


Base = declarative_base()

class Configuration(Base):
    __tablename__ = 'configurations'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    def __init__(self, name):
        # self.id = id
        self.name = name

        print(name)
        print(self.name)


    def __repr__(self):
        return """{
            "id": "%s",
            "name": "%s"
        }""" % (self.id, self.name)


class Sensor(Base):
    __tablename__='sensors'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    kp = Column(Float, nullable=False)
    ki = Column(Float, nullable=False)
    kd = Column(Float, nullable=False)
    tf = Column(Float, nullable=False)
    configuration_id = Column(Integer, ForeignKey("configurations.id"), nullable=False)

    def set_values(self, kp, ki, kd, tf):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.tf = tf

    def __init__(self, name, configuration_id, kp=0, ki=0, kd=0, tf=0):
        self.name = name
        self.configuration_id = configuration_id
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.tf = tf
        # print("%s %s %s %s " % self.kp, self.ki, self.kd, self.tf)

    def __repr__(self):
        return """{
                "name": "%s",
                "values": {
                    "dd": %d,
                    "Ki": %d,
                    "Kp": %d,
                    "Tf": %d
                },
                "configuration_id": "%s"
            }""" % (self.name, self.kp, self.ki, self.kd, self.tf, self.configuration_id)


class Dao():
    def __init__(self):
        engine = create_engine('sqlite:///db.sqlite', echo=True)
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def add_configuration(self, name):
        conf = Configuration(name)
        self.session.add(conf)
        self.session.commit()

    def add_sensor(self, name, configuration_id):
        sensor = Sensor(name, configuration_id)
        self.session.add(sensor)
        self.session.commit()

    def get_list_id(self, conf_name):
        return self.session.query(Configuration).filter_by(name=conf_name).one().id

    def get_all_lists(self):
        return self.session.query(Configuration)

    def get_list_by_name(self, list_name):
        return self.session.query(Configuration).filter_by(name=list_name).all()

    def get_sensor_by_id(self, conf_id):
        return self.session.query(Sensor).filter_by(configuration_id=conf_id).all()

    def get_sensor_by_name(self, conf_name):
        conf_id = self.get_list_id(conf_name)
        return self.get_sensor_by_id(conf_id)

    def create_list(self, conf_name):
        self.add_configuration(conf_name)
        sensor_names = ["Pitch", "Roll", "Yaw", "Thrust"]
        conf_id = self.get_list_id(conf_name)
        for i in sensor_names:
            self.add_sensor(i, conf_id)

    def update_sensor(self, conf_id, name, kp, ki, kd, tf):
        sensor = self.session.query(Sensor).filter_by(configuration_id=conf_id).filter_by(name=name).first()
        sensor.set_values(kp, ki, kd, tf)
        self.session.commit()

    def delete_list(self, to_delete_conf_id):
        conf = Configuration()
        # conf = self.session.query(Configuration).filter_by(id=to_delete_conf_id)
        self.session.delete(conf)
        self.session.commit()

if __name__ == '__main__':
    dao = Dao()
    # dao.add_sensor("Yaw", 1)
    engine = create_engine('sqlite:///db.sqlite', echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    print(dao.get_sensor_by_name("Cage"))
    # print(dao.get_list_by_name("Nicolas").__repr__())
    # print(a)
    # for instance in session.query(Sensor):
    #     print(instance)
