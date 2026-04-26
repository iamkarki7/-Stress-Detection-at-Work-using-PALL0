class StressAI:
    """
    Simple AI stress detection model (rule-based scoring system)
    Replaceable with ML model later.
    """

    def __init__(self):
        pass

    def predict(self, sensor_data):
        hr = sensor_data["heart_rate"]
        gsr = sensor_data["gsr"]
        motion = sensor_data["motion"]

        score = 0

        # Heart rate check
        if hr > 100:
            score += 3
        elif hr > 85:
            score += 2
        else:
            score += 0

        # GSR (stress sweat response)
        if gsr > 1.2:
            score += 3
        elif gsr > 0.8:
            score += 2

        # Movement (restlessness)
        if motion > 7:
            score += 2
        elif motion > 4:
            score += 1

        # Final classification
        if score >= 6:
            return "HIGH STRESS"
        elif score >= 3:
            return "MODERATE STRESS"
        else:
            return "LOW STRESS"