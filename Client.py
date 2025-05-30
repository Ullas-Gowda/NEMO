import paho.mqtt.client as mqtt
import json
import time

BROKER = "192.168.103.124"
PORT = 1883
TOPIC = "test"
USERNAME = "awais"
PASSWORD = "Archu2025"

client = mqtt.Client()
client.username_pw_set(USERNAME, PASSWORD)
client.connect(BROKER, PORT, 60)

# Fake sensor data
sensor_data = {
    "temp": 24.5,
    "humidity": 55,
    "unit": "C"
}

# Publish as JSON string
client.publish(TOPIC, json.dumps(sensor_data))
print("📤 Published sensor data!")

client.disconnect()
