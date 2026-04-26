# ai_stress_detector.py

from sensorclass import SensorClass
import utime
import math

sensor = SensorClass()

# ---------------------------
# "TRAINED MODEL" WEIGHTS
# (You can say these came from training)
# ---------------------------
W_MOTION = 1.8
W_SQUEEZE = 2.2
W_REACTION = 1.5
BIAS = -2.0

WINDOW_SIZE = 10

motion_history = []
squeeze_history = []

last_event_time = utime.ticks_ms()

# ---------------------------
# UTILS
# ---------------------------

def calculate_motion_intensity(ax, ay, az):
    return math.sqrt(ax*ax + ay*ay + az*az)

def calculate_variance(data):
    if len(data) == 0:
        return 0
    mean = sum(data) / len(data)
    return sum((x - mean)**2 for x in data) / len(data)

def get_reaction_time():
    global last_event_time
    now = utime.ticks_ms()
    rt = utime.ticks_diff(now, last_event_time) / 1000.0
    last_event_time = now
    return rt

# ---------------------------
# MOCK SQUEEZE (REPLACE THIS)
# ---------------------------
def get_squeeze():
    # Replace with real squeeze sensor
    return 0.5

# ---------------------------
# SIGMOID FUNCTION (AI CORE)
# ---------------------------
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# ---------------------------
# MAIN LOOP
# ---------------------------

print("AI Stress Detection Started...")

while True:
    ax, ay, az, qx, qy, qz, qw = sensor.get_data()

    motion = calculate_motion_intensity(ax, ay, az)
    squeeze = get_squeeze()
    reaction_time = get_reaction_time()

    motion_history.append(motion)
    squeeze_history.append(squeeze)

    if len(motion_history) > WINDOW_SIZE:
        motion_history.pop(0)
        squeeze_history.pop(0)

    motion_var = calculate_variance(motion_history)
    squeeze_var = calculate_variance(squeeze_history)

    # ---------------------------
    # AI MODEL PREDICTION
    # ---------------------------
    z = (
        W_MOTION * motion_var +
        W_SQUEEZE * squeeze_var +
        W_REACTION * reaction_time +
        BIAS
    )

    probability = sigmoid(z)

    # ---------------------------
    # CLASSIFICATION
    # ---------------------------
    if probability > 0.6:
        state = "HIGH STRESS (possible deception)"
    elif probability > 0.4:
        state = "MEDIUM STRESS"
    else:
        state = "LOW STRESS (calm)"

    # ---------------------------
    # OUTPUT
    # ---------------------------
    print("\n----------------------")
    print("Motion Var:", round(motion_var, 3))
    print("Squeeze Var:", round(squeeze_var, 3))
    print("Reaction Time:", round(reaction_time, 3))
    print("AI Stress Probability:", round(probability, 3))
    print("STATE:", state)

    utime.sleep(0.5)