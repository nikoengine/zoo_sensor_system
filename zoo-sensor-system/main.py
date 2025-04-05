import random
import time

security_channel = []
cage_quality_channel = []
animal_condition_channel = []
general_channel = []


class Event:
    def __init__(self, name, payload):
        self.name = name
        self.payload = payload  


class Sensor:
    def __init__(self, id_number, sensor_type, cage):
        self.id_number = id_number
        self.sensor_type = sensor_type
        self.cage = cage

    def emit_event(self):
        timestamp = time.strftime("%H:%M:%S %d.%m.%Y")
        event_name = f"{self.sensor_type} sensor triggered"
        event = Event(event_name, {'sensor': self, 'timestamp': timestamp})
        security_channel.append(event)


class Employee:
    def __init__(self, id_number, name, role):
        self.id_number = id_number 
        self.name = name
        self.role = role

    def handle_sensor_event(self, event):
        sensor_type = event.payload['sensor'].sensor_type
        cage = event.payload['sensor'].cage

        if self.is_responsible_for(sensor_type):
            print(f"\nEvent received: {event.name}")
            print(f"My name is {self.name} and my role is {self.role}")
            print(f"{self.name} is going to check the cage: {cage}")

    def is_responsible_for(self, sensor_type):
        role_sensor_map = {
            'motion': 'guard',
            'humidity': 'zookeeper',
            'temperature': 'cleaner'
        }
        return role_sensor_map.get(sensor_type) == self.role


employees = [
    Employee(1, 'Piotr', 'zookeeper'),
    Employee(2, 'Kraiven', 'cleaner'),
    Employee(3, 'John', 'guard'),
    Employee(4, 'Mable', 'vet'),
    Employee(5, 'Jane', 'manager'),
    Employee(6, 'Serhat', 'zookeeper2'),
    Employee(7, 'Tom', 'cleaner2'),
    Employee(8, 'Serhat', 'guard2'),
    Employee(9, 'Piotr', 'admin')
]


sensors = [
    Sensor(1, 'humidity', 'elephants 1'),
    Sensor(2, 'humidity', 'tigers 1'),
    Sensor(3, 'humidity', 'elephants 2'),
    Sensor(4, 'temperature', 'elephants 1'),
    Sensor(5, 'temperature', 'tigers 1'),
    Sensor(6, 'motion', 'elephants 1'),
    Sensor(7, 'motion', 'tigers 1'),
    Sensor(8, 'motion', 'tigers 2')
]


def randomly_trigger_sensors():
    chosen_sensors = random.sample(sensors, random.randint(1, len(sensors)))
    for sensor in chosen_sensors:
        sensor.emit_event()


def handle_all_events():
    for event in security_channel:
        for employee in employees:
            employee.handle_sensor_event(event)


randomly_trigger_sensors()
handle_all_events()
