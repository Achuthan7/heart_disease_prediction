A web-based application to predict the risk of heart disease using machine learning.  
Built with Flask (Python) on the backend and a Tailwind CSS + JavaScript frontend.  
Get instant predictions along with a  speedometer-style risk gauge.

| Tech Stack       | Tech used                      |
| ---------------- | ------------------------------ |
| Frontend         | HTML, Tailwind CSS, JavaScript |
| Backend          | Flask (Python), scikit-learn   | 
| Machine Learning |  Random Forest Classifier      |
| Hosting          | deployed the project in Render |

live site : https://heart-disease-prediction-6490.onrender.com/

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

<img width="683" height="754" alt="Screenshot 2025-07-10 181017" src="https://github.com/user-attachments/assets/3a648a4e-38ba-4186-addc-cd36b73a3142" />
<img width="684" height="877" alt="Screenshot 2025-07-10 181004" src="https://github.com/user-attachments/assets/faf5aef8-e9ac-42d5-ba51-f4e72e8aea70" />

<img width="692" height="892" alt="Screenshot 2025-07-10 181108" src="https://github.com/user-attachments/assets/096a537d-9fd0-4d8c-8e68-6a12e0f1115e" />
