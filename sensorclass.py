import random

class Sensor:
    """
    Simulates wearable sensors:
    - heart rate
    - skin conductance (GSR)
    - movement level
    """

    def __init__(self):
        self.base_hr = 70
        self.base_gsr = 0.5

    def read_heart_rate(self):
        # normal 60–90, stress increases it
        return self.base_hr + random.randint(-5, 35)

    def read_gsr(self):
        # skin conductance increases with stress
        return round(self.base_gsr + random.uniform(0, 1.5), 2)

    def read_motion(self):
        # jitter / restlessness
        return random.randint(0, 10)

    def get_data(self):
        return {
            "heart_rate": self.read_heart_rate(),
            "gsr": self.read_gsr(),
            "motion": self.read_motion()
        }