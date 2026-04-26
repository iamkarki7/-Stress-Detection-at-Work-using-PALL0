import time
from sensorclass import Sensor
from ai_stress_detector import StressAI
from timeutils import get_timestamp

def run():
    sensor = Sensor()
    ai = StressAI()

    print("🧠 AI Stress Detector Running...\n")

    while True:
        data = sensor.get_data()
        result = ai.predict(data)
        timestamp = get_timestamp()

        print(f"[{timestamp}] Sensor Data: {data}")
        print(f"👉 Stress Level: {result}\n")

        time.sleep(2)

if __name__ == "__main__":
    run()