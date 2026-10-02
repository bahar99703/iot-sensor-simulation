import random
import time
import json

def fake_sensor_reading():
    temperature = round(random.uniform(18.0, 30.0), 2)   # °C
    humidity = round(random.uniform(30.0, 70.0), 2)      # %
    return {
        "temperature": temperature,
        "humidity": humidity,
        "timestamp": time.time()
    }

for i in range(30):
    reading = fake_sensor_reading()
    print(json.dumps(reading))   
    time.sleep(1)
