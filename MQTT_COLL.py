import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    print("Connected with code:", rc)
    client.subscribe("home/sensor/#")  # subscribe to all home/sensor topics


def on_message(client, userdata, msg):
    print(f"Received from {msg.topic}: {msg.payload.decode()}")


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)
client.loop_forever()
