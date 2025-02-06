import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

df = pd.read_csv("student_data.csv")

print(df.head())

categorical_columns = [
    "Parental_Involvement", "Access_to_Resources", "Extracurricular_Activities",
    "Motivation_Level", "Internet_Access", "Family_Income", "Teacher_Quality",
    "School_Type", "Peer_Influence", "Learning_Disabilities", "Parental_Education_Level",
    "Distance_from_Home", "Gender"
]

label_encoders = {}
for col in categorical_columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le 

X = df.drop(columns=["Exam_Score"]) 
y = df["Exam_Score"]  

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

joblib.dump(model, "student_performance_model.pkl")

y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Absolute Error (MAE): {mae:.2f}")
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"R-Squared (R²) Score: {r2:.2f}")

new_student = pd.DataFrame([{
    "Hours_Studied": 20, "Attendance": 75, "Parental_Involvement": "Low",
    "Access_to_Resources": "Medium", "Extracurricular_Activities": "No",
    "Sleep_Hours": 7, "Previous_Scores": 65, "Motivation_Level": "Medium",
    "Internet_Access": "Yes", "Tutoring_Sessions": 1, "Family_Income": "Medium",
    "Teacher_Quality": "High", "School_Type": "Public", "Peer_Influence": "Positive",
    "Physical_Activity": 3, "Learning_Disabilities": "No",
    "Parental_Education_Level": "College", "Distance_from_Home": "Moderate",
    "Gender": "Male"
}])

for col in categorical_columns:
    new_student[col] = label_encoders[col].transform(new_student[col])

predicted_score = model.predict(new_student)
print(f"Predicted Exam Score: {predicted_score[0]:.2f}")

joblib.dump(model, 'student_performance_model.pkl')
