import paho.mqtt.client as mqtt
import json
import time
import random

# MQTT Broker Config
broker = "localhost"  # or use IP like "192.168.1.100"
port = 1883
topic = "sensor/data"
username = "awais"
password = "Archu2025"

# Connect to MQTT
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, protocol=mqtt.MQTTv311)
client.username_pw_set(username, password)
client.connect(broker, port, 60)


def generate_sensor_data():
    return {
        "temperature": round(random.uniform(20.0, 30.0), 2),  # °C
        "humidity": round(random.uniform(40.0, 60.0), 2),  # %
        "pressure": round(random.uniform(950.0, 1050.0), 2),  # hPa
        "motion": round(random.uniform(0, 1)),  # hPa
        "smoke": round(random.uniform(0, 1)),  # hPa
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
    }


def check_col():
    data = generate_sensor_data()
    if data.smoke == 1 and data.temperature > 45:
        return "anamoly"
    else:
        return "Nominal"


# Infinite loop to send data every 2 seconds
try:
    while True:
        data = generate_sensor_data()
        payload = json.dumps(data)
        client.publish(topic, payload)
        print(f"📤 Sent: {payload}")
        time.sleep(2)
except KeyboardInterrupt:
    print("\n🚪 Exiting...")
    client.disconnect()
