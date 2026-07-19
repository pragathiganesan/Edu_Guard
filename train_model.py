import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load dataset
data = pd.read_csv("dataset/students.csv")

# Input features
X = data[['Attendance', 'Marks', 'StudyHours', 'Engagement']]

# Output
y = data['Dropout']

# Create model
model = RandomForestClassifier(random_state=42)

# Train model
model.fit(X, y)

# Save model
joblib.dump(model, "model.pkl")

print("Model trained successfully!")