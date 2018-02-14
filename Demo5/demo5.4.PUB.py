import paho.mqtt.client as mqtt

broker = "192.168.2.12"
topic = "testitopic"
message = "JERE OLI TAALA"

client = mqtt.Client()
client.connect(broker)
client.publish(topic, message)
client.disconnect()