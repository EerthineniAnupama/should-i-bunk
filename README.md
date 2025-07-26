# 🎓 Should I Bunk? – A Smart Attendance Advisor

> A machine learning-powered Flask web app that helps students decide whether they can safely skip class without dropping below their required attendance percentage.

---

## 🚀 Overview

This project uses logistic regression to analyze various factors such as your mood, sleep, test schedules, and subject importance to **predict whether you should attend or can afford to skip a class** — while still maintaining your attendance above the required limit.

💡 Useful for:
- Students who want to balance rest, priorities, and attendance.
- Learning how to build full-stack ML apps with Python and Flask.

---

## 📸 Screenshots

### 🏠 Home Page
![UI Screenshot](https://github.com/EerthineniAnupama/should-i-bunk/blob/master/image.png)


### 🔍 
![Prediction Screenshot](https://github.com/EerthineniAnupama/should-i-bunk/blob/master/Screenshot%202025-07-26%20204422.png)


---

## 🧠 Technologies Used

- 🐍 Python (Logistic Regression)
- 🧠 **joblib** (Model saving/loading)
- 🌐 Flask (Backend server)
- 🧾 HTML/CSS + JS (Frontend)
- 📦 Pandas, NumPy (Data handling)
- ☁️ Deployed via Render

---

## 📂 Project Structure



---

## ✨ Features

- ✅ Predicts if you can afford to miss class without hurting attendance
- 🧠 Uses logistic regression for classification
- 📊 Takes into account mood, sleep, test pressure, subject priority
- 🌍 Flask-based frontend for input & result display
- 💾 Model persisted using **joblib**
- 🔗 Fully deployable (e.g., Render)

---

## 🧪 Sample Inputs

The prediction model considers:
- Mood (`happy`, `okay`, `sad`, `tired`)
- Sleep hours (`0–12`)
- Upcoming test? (`yes`/`no`)
- Finished topic? (`yes`/`no`)
- Subject importance (`high`, `medium`, `low`)
- Total classes, attended classes, required attendance

---

## 🛠️ How to Run Locally

### 🔃 1. Clone this Repo

```bash
git clone https://github.com/EerthineniAnupama/should-i-bunk.git
cd should-i-bunk
🧪 2. Set Up Virtual Environment
python -m venv venv
venv\Scripts\activate  # Windows
# or
source venv/bin/activate  # macOS/Linux

📦 3. Install Dependencies
