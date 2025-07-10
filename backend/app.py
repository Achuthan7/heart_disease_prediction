from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import pandas as pd
import pickle

app = Flask(__name__)
CORS(app)


with open("heart_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("heart_scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

with open("heart_features.pkl", "rb") as f:
    feature_columns = pickle.load(f)

@app.route("/predict", methods=["POST"])
def predict():
    try:
        input_data = request.get_json()
        categorical_mappings = {
            "sex": {"male": "male", "female": "female"},
            "cp": {
                "typical angina": "typical angina",
                "atypical angina": "atypical angina",
                "non-anginal pain": "non-anginal pain",
                "asymptomatic": "asymptomatic",
            },
            "fbs": {"yes": "yes", "no": "no"},
            "restecg": {
                "normal": "normal",
                "st-t abnormality": "st-t abnormality",
                "left ventricular hypertrophy": "lv hypertrophy",
                "lv hypertrophy": "lv hypertrophy",
            },
            "exang": {"yes": "yes", "no": "no"},
            "slope": {
                "upsloping": "upsloping",
                "flat": "flat",
                "downsloping": "downsloping",
            },
            "thal": {
                "normal": "normal",
                "fixed defect": "fixed defect",
                "reversible defect": "reversible defect",
            },
        }
        for key in categorical_mappings:
            if key in input_data:
                val = input_data[key].strip().lower()
                input_data[key] = categorical_mappings[key].get(val, val)

        input_df = pd.DataFrame([input_data])
        input_df_encoded = pd.get_dummies(input_df)
        input_df_encoded = input_df_encoded.reindex(columns=feature_columns, fill_value=0)

        numeric_cols = ["age", "trestbps", "chol", "thalach", "oldpeak", "ca"]
        for col in numeric_cols:
            if col in input_df_encoded.columns:
                input_df_encoded[col] = pd.to_numeric(input_df_encoded[col], errors='coerce')

 
        if input_df_encoded.isnull().values.any():
            raise ValueError("One or more input values are invalid or missing.")

        input_scaled = scaler.transform(input_df_encoded)

 
        prediction = model.predict(input_scaled)[0]
        probability = model.predict_proba(input_scaled)[0][1]
        percent = round(probability * 100, 2)

        result = "Heart Disease" if prediction == 1 else "No Heart Disease"
        risk = "Low Risk" if percent < 30 else "Moderate Risk" if percent < 70 else "High Risk"

        return jsonify({
            "prediction": int(prediction),
            "result": result,
            "probability": percent,
            "risk_level": risk
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
