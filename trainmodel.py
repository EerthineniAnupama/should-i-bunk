# train.py

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import pickle
import os

# Load the dataset
df = pd.read_csv('data/dataset_100.csv')  # Make sure path is correct

# Add attendance percentage as a feature
df['attendance_percent'] = (df['attended_classes'] / df['total_classes']) * 100

# Target and features
X = df.drop(columns=['should_bunk'])
y = df['should_bunk']

# Define categorical and numerical columns
categorical_cols = ['mood', 'test_soon', 'topic_done', 'subject_importance']
numerical_cols = ['sleep_hours', 'total_classes', 'attended_classes', 'min_required_percent', 'attendance_percent']

# Preprocessing
preprocessor = ColumnTransformer([
    ('cat', OneHotEncoder(drop='first'), categorical_cols),
    ('num', StandardScaler(), numerical_cols)
])

# Full pipeline with logistic regression model
model_pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', LogisticRegression(max_iter=1000))
])

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Fit model
model_pipeline.fit(X_train, y_train)

# Create backend directory if not exists
os.makedirs('backend', exist_ok=True)

# Save the trained model pipeline
with open('backend/bunk_model.pkl', 'wb') as f:
    pickle.dump(model_pipeline, f)

# Evaluate
accuracy = model_pipeline.score(X_test, y_test) * 100
print(f"Model accuracy: {accuracy:.2f}%")
