A web-based application to predict the risk of heart disease using machine learning.  
Built with Flask (Python) on the backend and a Tailwind CSS + JavaScript frontend.  
Get instant predictions along with a  speedometer-style risk gauge.

Frontend: HTML, Tailwind CSS, JavaScript
Backend: Flask (Python), scikit-learn
Machine Learning: Random Forest Classifier

# WORKING
# User Input (Frontend)

* The user enters medical and lifestyle data in a web form:
  * Age, gender
  * Chest pain type, blood pressure, cholesterol
  * Fasting blood sugar, resting ECG results
  * Max heart rate (thalach), exercise-induced angina
  * ST depression (oldpeak), slope of the ST segment
  * Number of major vessels, thalassemia condition
All fields are user-friendly, with dropdowns and validations to avoid errors.

# Form Submission (Frontend JS)

* Once submitted, the input data is:
  * Collected using JavaScript
  * Cleaned and converted (numeric fields are parsed properly)
  * Sent via a POST request to a Flask backend API (/predict)

# Data Preprocessing (Backend)

* The Flask backend:
  * Loads the trained ML model (RandomForestClassifier)
  * Loads the scaler and feature schema used during model training
  * Applies the same preprocessing steps (one-hot encoding, feature reindexing, scaling)

# Prediction (ML Model)

* The model:
  * Predicts whether the person is at risk (0 = No Disease, 1 = Heart Disease)
  * Calculates the probability/confidence score
  * Categorizes the result into one of three risk levels:

  Low Risk (< 30%)
  Moderate Risk (30–69%)
  High Risk (≥ 70%)

# Data Consistency: 
The model and frontend use the same feature names and value formats.
# Reusable ML Assets: 
Model, scaler, and feature schema are saved as .pkl files and reused by the backend.

