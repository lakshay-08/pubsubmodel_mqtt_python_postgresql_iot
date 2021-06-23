import paho.mqtt.publish as publish
from random import uniform
import time


def generate_sensor_data():
    """
      Generates sensor data
     :return: prints the generated data
    """
    while True:
        msgs = [{'topic': "sensor/test/room_temp", 'payload': float("{0:.2f}".format(uniform(20.0, 25.0)))},
                ("sensor/test/flow_status", "OK", 0, False)]
        print(msgs)
        publish.multiple(msgs, hostname="localhost")
        # Publishes after every 5 seconds
        time.sleep(5)


def main():
    generate_sensor_data()