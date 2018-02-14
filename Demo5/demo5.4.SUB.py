import paho.mqtt.client as mqtt
import time

broker = "192.168.2.12"
topic = "testitopic"

def on_message(client1, userdata, message):
    print("Viesti saatu", str(message.payload.decode("utf-8")))


def on_connect(client, userdata, flags, rc):
    client.subscribe(topic)


client = mqtt.Client()
client.on_message = on_message
time.sleep(1)

client.connect(broker)
client.loop_start()
client.subscribe(topic)

time.sleep(20)
client.disconnect()
client.loop_stop()