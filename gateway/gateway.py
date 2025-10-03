import time
import random
import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect("mqtt", 1883, 60)

while True:
    payload = {
        "temperature": round(20 + random.random()*10, 2),
        "vibration": round(random.random(), 2)
    }
    client.publish("plc/data", str(payload))
    print("Published:", payload)
    time.sleep(2)
