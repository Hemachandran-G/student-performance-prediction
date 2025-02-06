from flask import Flask, request, jsonify
from sklearn.impute import SimpleImputer
import joblib
import pandas as pd

app = Flask(__name__)

model = joblib.load('student_performance_model.pkl')

columns = [
    "Hours_Studied", "Attendance", "Parental_Involvement", "Access_to_Resources",
    "Extracurricular_Activities", "Sleep_Hours", "Previous_Scores", "Motivation_Level",
    "Internet_Access", "Tutoring_Sessions", "Family_Income", "Teacher_Quality",
    "School_Type", "Peer_Influence", "Physical_Activity", "Learning_Disabilities",
    "Parental_Education_Level", "Distance_from_Home", "Gender"
]

@app.route('/')
def home():
    return "Student Performance Prediction API"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    df = pd.DataFrame([data])  
    df = preprocess_input(df)  
    
    prediction = model.predict(df)
    return jsonify({'Predicted Exam Score': prediction[0]})

def preprocess_input(df):
    """Convert categorical variables to numerical encoding and handle NaN values."""
    
    encoding_dict = {
        "Low": 0, "Medium": 1, "High": 2,
        "Yes": 1, "No": 0,
        "Male": 0, "Female": 1,
        "Public": 0, "Private": 1,
        "Positive": 1, "Negative": 0,
        "Near": 0, "Moderate": 1, "Far": 2
    }

    for col in df.columns:
        if df[col].dtype == "object": 
            df[col] = df[col].map(encoding_dict)
    
    df.fillna(-1, inplace=True)

    imputer = SimpleImputer(strategy='median')  
    df[df.columns] = imputer.fit_transform(df)

    return df

if __name__ == '__main__':
    app.run(debug=True)
