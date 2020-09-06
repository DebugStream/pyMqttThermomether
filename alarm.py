import paho.mqtt.client as mqtt
from playsound import playsound


def on_message(client, userdata, message):
    temp = int(message.payload)
    if temp > 33:
        print(f"La Temperatura en {message.topic} es de {temp}")
        playsound("./beep.mp3")


client = mqtt.Client()
client.connect("localhost")
client.subscribe("casa/#")
client.on_message = on_message

print("Alarma Lista!!")
client.loop_forever()
