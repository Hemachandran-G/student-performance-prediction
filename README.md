# Student Performance Prediction Model

This project predicts students' exam scores based on various academic and personal factors using **Machine Learning**. The model is trained on student data and provides insights into performance trends. It uses **Linear Regression** for prediction and **MongoDB** for data storage.

## 🚀 Features
- Predicts student exam scores based on study habits, attendance, and motivation.
- Uses **Linear Regression** for performance prediction.
- **MongoDB integration** for storing student records and model predictions.
- Flask API for real-time predictions.
- Supports new student data input and dynamic recommendations.

## 📌 Tech Stack
- **Python** (pandas, numpy, scikit-learn)
- **MongoDB** (Database for storing student data)
- **Flask** (API for prediction service)
- **Joblib** (Model persistence)
- **Pymongo** (MongoDB interaction)

## 📂 Folder Structure
```
├── student_data.csv              # Dataset containing student records
├── app.py                        # Flask API for student prediction
├── model.py                      # Model training and prediction script
├── requirements.txt              # List of dependencies
├── README.md                     # Project documentation
├── student_performance_model.pkl  # Trained machine learning model
```

## 🛠 Installation
### **1. Clone the repository**
```bash
git clone https://github.com/Hemachandran-G/student-performance-prediction.git
cd student-performance-prediction
```

### **2. Install dependencies**
```bash
pip install -r requirements.txt
```

### **3. Set up MongoDB**
- Install MongoDB locally or use [MongoDB Atlas](https://www.mongodb.com/atlas).
- Update the **MongoDB connection string** in `app.py`.

### **4. Train the model**
```bash
python model.py
```
This will train the model and save it as `student_performance_model.pkl`.

### **5. Run the Flask API**
```bash
python app.py
```
API will be available at `http://127.0.0.1:5000/`.

## 📌 API Endpoints
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/predict` | POST | Predicts student exam score based on input data |
| `/add_student` | POST | Stores new student data in MongoDB |
| `/get_students` | GET | Retrieves stored student data |
| `/get_recommendations/<student_id>` | GET | Fetches personalized course recommendations |

## 🎯 Example API Usage

### **Predict Student Score**
Send a **POST request** to `/predict` with the following **input fields**:
```json
{
  "Hours_Studied": 23,
  "Attendance": 84,
  "Parental_Involvement": "Low",
  "Access_to_Resources": "High",
  "Extracurricular_Activities": "No",
  "Sleep_Hours": 7,
  "Previous_Scores": 73,
  "Motivation_Level": "Low",
  "Internet_Access": "Yes",
  "Tutoring_Sessions": 0,
  "Family_Income": "Low",
  "Teacher_Quality": "Medium",
  "School_Type": "Public",
  "Peer_Influence": "Positive",
  "Physical_Activity": 3,
  "Learning_Disabilities": "No",
  "Parental_Education_Level": "High School",
  "Distance_from_Home": "Near",
  "Gender": "Male"
}
```
#### **Response Example:**
```json
{
    "Predicted_Exam_Score": 78.5
}
```

## 🛠 Future Enhancements
- Improve accuracy using **deep learning models**.
- Integrate **frontend with Flask** for better user experience.
- Collect real-time student feedback to enhance recommendations.

## 🤝 Contributing
1. **Fork** the repository.
2. Create a **new branch**: `git checkout -b feature-branch`
3. Make your changes and **commit**: `git commit -m "Added new feature"`
4. **Push** to GitHub: `git push origin feature-branch`
5. Submit a **Pull Request**!

## 📝 License
This project is **open-source** under the [MIT License](LICENSE).

---
📢 **Feel free to contribute and improve this project!** 🚀  
For any questions, reach out to **[Hemachandran](https://github.com/Hemachandran-G/)**.

