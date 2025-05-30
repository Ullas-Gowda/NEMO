import paho.mqtt.client as mqtt

BROKER = (
    "192.168.137.1"  # Use the IP address that successfully pings your Windows server
)
PORT = 1883
TOPIC = "test"  # Use the test topic for connectivity check

import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker!")
        client.subscribe(TOPIC)
    else:
        print(f"Failed to connect, return code {rc}")


def on_message(client, userdata, msg):
    print(f"Received command for {TOPIC}: {msg.payload.decode()}")


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT, 60)
client.loop_forever()
