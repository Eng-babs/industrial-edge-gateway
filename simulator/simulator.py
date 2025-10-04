import time, json, random
import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect("mqtt", 1883, 60)

while True:
    data = {
        "temperature": round(random.uniform(20, 80), 2),
        "vibration": round(random.uniform(0.1, 1.5), 3),
        "pressure": round(random.uniform(1.0, 5.0), 2)
    }
    client.publish("plc/sensors", json.dumps(data))
    print("Published:", data)
    time.sleep(5)

