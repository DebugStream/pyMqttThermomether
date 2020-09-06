import sys
import time
from random import randrange
import paho.mqtt.client as mqtt


client = mqtt.Client()
client.connect("localhost")
zone = sys.argv[1]

while True:
    temp = randrange(10, 35)
    print(f"Temperatura en {zone}: {temp}")
    client.publish(f"casa/{zone}/temperatura", temp)
    time.sleep(1)

