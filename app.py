from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd
import sklearn
import os

print("Scikit-learn version:", sklearn.__version__)

app = Flask(__name__)

# Use absolute path to load model (Render-safe)
model_path = os.path.join(os.path.dirname(__file__), 'backend', 'model.joblib')
model_pipeline = joblib.load(model_path)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    try:
        # Extract input values from request JSON
        mood = data['mood']
        sleep_hours = int(data['sleep_hours'])
        test_soon = data['test_soon']
        topic_done = data['topic_done']
        subject_importance = data['subject_importance']
        total_classes = int(data['total_classes'])
        attended_classes = int(data['attended_classes'])
        min_required_percent = int(data['min_required_percent'])

        # Calculate attendance percentage
        attendance_percent = (attended_classes / total_classes) * 100

        # Create a DataFrame for prediction
        input_df = pd.DataFrame([{
            'mood': mood,
            'sleep_hours': sleep_hours,
            'test_soon': test_soon,
            'topic_done': topic_done,
            'subject_importance': subject_importance,
            'total_classes': total_classes,
            'attended_classes': attended_classes,
            'min_required_percent': min_required_percent,
            'attendance_percent': attendance_percent
        }])

        # Predict using the trained model
        prediction = model_pipeline.predict(input_df)[0]
        return jsonify({'should_bunk': int(prediction)})

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
