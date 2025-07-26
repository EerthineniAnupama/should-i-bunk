# train.py

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import joblib
import os

# Load dataset
df = pd.read_csv('data/dataset_100.csv')  # Ensure this path is correct

# Add attendance percentage feature
df['attendance_percent'] = (df['attended_classes'] / df['total_classes']) * 100

# Define features and target
X = df.drop(columns=['should_bunk'])
y = df['should_bunk']

# Column types
categorical_cols = ['mood', 'test_soon', 'topic_done', 'subject_importance']
numerical_cols = ['sleep_hours', 'total_classes', 'attended_classes', 'min_required_percent', 'attendance_percent']

# Preprocessing pipeline
preprocessor = ColumnTransformer([
    ('cat', OneHotEncoder(drop='first'), categorical_cols),
    ('num', StandardScaler(), numerical_cols)
])

# Full model pipeline
model_pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', LogisticRegression(max_iter=1000))
])

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model_pipeline.fit(X_train, y_train)

# Save model to backend folder
os.makedirs('backend', exist_ok=True)
joblib.dump(model_pipeline, 'backend/bunk_model.joblib')

# Evaluate
accuracy = model_pipeline.score(X_test, y_test) * 100
print(f"Model accuracy: {accuracy:.2f}%")
