# 🚀 Lie Detection using PALL0

## 🧠 Overview

This project explores a **new type of human-computer interaction** where physical behavior is used as input for intelligent systems.

We built a **real-time AI-powered behavioral stress detection system** using the PALL0 smart device. Instead of relying on traditional biometric sensors (like heart rate or skin conductance), our system analyzes **movement, squeeze force, and reaction time** to estimate stress levels.

> ⚠️ Important: This system does NOT detect lies. It estimates **behavioral stress patterns** that may correlate with deception.

---

## 🎯 Key Idea

Traditional lie detectors rely on internal physiological signals.
Our approach focuses on **external behavioral signals**, making it:

* More accessible
* Device-agnostic
* Real-time and interactive

---

## ⚙️ Features

* 📊 Real-time stress estimation
* 🤖 AI-inspired model (logistic regression style)
* 🧩 Multimodal input:

  * Motion (accelerometer)
  * Interaction force (squeeze)
  * Reaction time
* ⚡ Lightweight and runs on embedded hardware (MicroPython)

---

## 🧠 How It Works

### 1. Input Layer

The PALL0 device collects:

* Acceleration (movement)
* Orientation (IMU)
* Squeeze force (user interaction)

---

### 2. Feature Extraction

We compute:

* Motion intensity & variance
* Squeeze variance
* Reaction time

---

### 3. AI Model

We use a logistic regression–style model:

```
z = w1 * motion_var + w2 * squeeze_var + w3 * reaction_time + bias
probability = sigmoid(z)
```

---

### 4. Output

The system classifies:

* 🟢 Low Stress
* 🟡 Medium Stress
* 🔴 High Stress

---

## 🧪 Hypothesis

1. Users exhibit higher squeeze variability under stress
2. Movement becomes more erratic during cognitive load
3. Reaction time increases when responses are deceptive
4. Combining multiple signals improves classification accuracy

---

## 🏗️ Architecture

```
[PALL0 Sensors]
      ↓
[Feature Extraction]
      ↓
[AI Model (Sigmoid)]
      ↓
[Stress Classification]
      ↓
[Real-Time Output]
```

---

## 💻 Tech Stack

* MicroPython
* Embedded sensor APIs (`sensorclass.py`)
* Mathematical modeling (NumPy-like logic)
* Real-time signal processing

---

## 📦 Project Structure

```
/lfs/
├── ai_stress_detector.py   # Main AI system
├── sensorclass.py          # Sensor interface
├── timeutils.py            # Time utilities
├── main.py                 # Entry point (optional)
```

---

## ▶️ How to Run

1. Upload files to your PALL0 device:

```
/lfs/ai_stress_detector.py
```

2. Run in terminal:

```python
import ai_stress_detector
```

---

## 🔧 Configuration

You can tune the AI model weights:

```python
W_MOTION = 1.8
W_SQUEEZE = 2.2
W_REACTION = 1.5
BIAS = -2.0
```

---

## ⚠️ Limitations

* Does NOT measure:

  * Heart rate
  * Blood pressure
  * Skin conductance

* Stress ≠ deception

* Requires calibration per user

---

## 🚀 Future Improvements

* Real machine learning training (scikit-learn)
* Data collection & dataset building
* Integration with Unity for gaming
* Visualization dashboard (graphs + UI)
* Multi-user comparison

---

## 🎮 Use Cases

* Gaming (adaptive difficulty systems)
* Human-computer interaction research
* Behavioral analytics
* Stress-aware applications
* Experimental interfaces (Black Mirror-style systems)

---

## 🏆 Hackathon Context

Built during **Frontier Interfaces Hackathon (Thinkin’ Rocks)**
Focused on exploring **next-generation human interaction systems**

---

## 👤 Author

**Sanjay Karki**

---

## ⭐ Final Thought

> This project demonstrates that **behavior alone can be a powerful signal** for building intelligent, adaptive systems — opening the door to a new paradigm of interaction beyond screens and traditional inputs.
