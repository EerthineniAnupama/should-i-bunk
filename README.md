🎓 Should I Bunk?
A machine learning web application that helps students decide whether to attend or skip class based on real-life factors like sleep, tests, and mood.


📌 Live App: should-i-bunk-o4ym.onrender.com

📌 Overview
"Should I Bunk?" is a student-focused ML web app that predicts whether it's safe to skip a class based on personal and academic context. Built with a trained Logistic Regression model and deployed on Render using Flask and Gunicorn.

🧠 Features
✅ Predicts whether a student can bunk class or not

🧠 Trained ML model with 95%+ accuracy (Logistic Regression)

📦 Flask backend with a simple and responsive frontend

📝 Takes inputs like:

Mood

Sleep hours

Upcoming test

Topic covered

Subject importance

Attendance data

📸 Screenshots
Home Page	Prediction Result

⚙️ Tech Stack
Layer	Tools Used
ML Model	Python, scikit-learn, Pandas
Backend	Flask, Gunicorn, joblib
Frontend	HTML5, CSS3, JavaScript
Hosting	Render (free-tier deployment)
Version Control	Git + GitHub
should-i-bunk/
├── backend/
│   └── model.joblib           # Trained ML model
├── templates/
│   └── index.html             # Frontend page
├── static/
│   └── style.css              # Styling
├── app.py                     # Flask backend
├── predict.py                 # Model training script
├── requirements.txt
└── README.md

📈 Model Details
Algorithm: Logistic Regression

Libraries: scikit-learn, pandas

Accuracy: ~95.8% on validation data

Input Features: mood, sleep_hours, test_soon, topic_done, subject_importance, total/attended_classes, min attendance %

🧪 Sample Input

{
  "mood": "tired",
  "sleep_hours": 4,
  "test_soon": "no",
  "topic_done": "yes",
  "subject_importance": "low",
  "total_classes": 30,
  "attended_classes": 24,
  "min_required_percent": 75
}


🌐 Deployment
Deployed on Render with Gunicorn:

# render.yaml or start command
gunicorn app:app


📝 Future Improvements
Add login & user history tracking

Use advanced models like Random Forest or XGBoost

Improve UI/UX with animations & validations

Mobile responsive version

🙋‍♀️ Author
Anupama Eerthineni
BMS College of Engineering | AI & ML
LinkedIn • GitHub


