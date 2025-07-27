# 🎓 Should I Bunk? – A Smart Attendance Advisor


 A machine learning-powered Flask web app that helps students decide whether they can safely skip class without dropping below their required attendance percentage.

 **🔗 Live URL**: [https://should-i-bunk-o4ym.onrender.com/](https://should-i-bunk-o4ym.onrender.com/)



⚠️ *Please note: The application is deployed using Render's free plan, which may cause a delay (20–30 seconds) during the initial load due to server cold starts.*






---

## 🚀Overview
Should I Bunk? is a full-stack machine learning web application that helps students decide whether they can afford to miss a class without falling below the mandatory attendance threshold. Built using Logistic Regression, the app predicts based on personalized inputs like sleep hours, mood, upcoming tests, and subject priority.

🎯 Perfect for:

Students juggling between rest, academics, and attendance requirements

Showcasing full-stack ML + Flask deployment skills

Demonstrating real-world data analysis & predictive modeling in interviews


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

```
should-i-bunk/
│
├── backend/
│   ├── model.pkl          # Trained logistic regression model
│   └── predict.py         # Script to test new input
│
├── dataset.csv            # Sample dataset
├── requirements.txt       # All dependencies
├── image.png              # Screenshot for README
└── README.md              # Project documentation
```

---



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

```
### 🧪 2. Set Up Virtual Environment
```bash

python -m venv venv
venv\Scripts\activate  # Windows
# or
source venv/bin/activate  # macOS/Linux

```


### 📦 3. Install Required Packages

```bash
pip install -r requirements.txt
```

### 🚀 4. Run app.py

Edit the `app.py` file with your own input dictionary and run:

```bash
python /app.py
```

Example input inside `app.py`:
```python
new_student = {
    'mood': 'okay',
    'sleep_hours': 4,
    'test_soon': 'no',
    'topic_done': 'yes',
    'subject_importance': 'low',
    'total_classes': 35,
    'attended_classes': 28,
    'min_required_percent': 75
}
```

---



## 📷 Screenshots

| Model Prediction Output |
|--------------------------|
| ![Screenshot](https://github.com/EerthineniAnupama/should-i-bunk/blob/master/image.png) |

---

📈 Future Improvements
📊 Enhanced model with more features (e.g., assignment deadlines)

📱 Responsive mobile-friendly design

📚 Data visualization of attendance patterns

🔐 User login and history tracking


---

## 🙋‍♀️ Author

**Anupama Eerthineni**  
🔗 [GitHub Profile](https://github.com/EerthineniAnupama)

---

## 📄 License

This project is licensed under the MIT License. Feel free to use and adapt it.

---

## ⭐ Support

If you find this project helpful, please ⭐ star the repo and share with your friends!
