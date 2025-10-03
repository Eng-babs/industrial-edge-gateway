import random
import time

while True:
    vibration = random.uniform(0.1, 0.9)
    temperature = random.uniform(22, 35)
    print(f"Simulated Vibration: {vibration:.2f}, Temp: {temperature:.2f}")
    time.sleep(1)
