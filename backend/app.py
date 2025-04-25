from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import pandas as pd
import joblib
import os
import random
from sklearn.preprocessing import OrdinalEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from datetime import datetime

app = Flask(__name__, static_folder='../frontend', static_url_path='')
CORS(app)

MODEL_PATH = 'ids_model.joblib'
ALERT_TYPES_PATH = 'alert_types.csv'
ALERT_DB_PATH = 'full_alert_database.csv'

def train_and_save_model():
    if not os.path.exists(MODEL_PATH):
        df = pd.read_csv(ALERT_DB_PATH)
        preprocessor = ColumnTransformer(
            transformers=[
                ('cat', OrdinalEncoder(handle_unknown='use_encoded_value', unknown_value=-1), 
                 ['type', 'severity', 'source'])
            ],
            remainder='passthrough'
        )
        pipeline = Pipeline([
            ('preprocessor', preprocessor),
            ('classifier', RandomForestClassifier())
        ])
        X = df[['type', 'severity', 'source', 'packet_size', 'duration', 'flag_count']]
        y = df['is_attack']
        pipeline.fit(X, y)
        joblib.dump(pipeline, MODEL_PATH)

train_and_save_model()

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/api/alerts')
def get_random_alert():
    # Load alert types
    types_df = pd.read_csv(ALERT_TYPES_PATH)
    alert_types = types_df['type'].dropna().tolist()
    # Define possible severities and sources
    severities = ['Low', 'Medium', 'High', 'Critical']
    sources = [f'192.168.1.{i}' for i in range(100, 200)]

    # Pick random values
    alert_type = random.choice(alert_types)
    severity = random.choice(severities)
    source = random.choice(sources)
    packet_size = random.randint(100, 2000)
    duration = round(random.uniform(0.5, 10.0), 2)
    flag_count = random.randint(0, 15)

    # Predict using model
    model = joblib.load(MODEL_PATH)
    input_data = pd.DataFrame([[
        alert_type, severity, source, packet_size, duration, flag_count
    ]], columns=['type', 'severity', 'source', 'packet_size', 'duration', 'flag_count'])
    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)

    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")

    alert = {
        'time': current_time,
        'type': alert_type,
        'severity': severity,
        'source': source,
        'prediction': int(prediction[0]),
        'confidence': float(probability[0][1]),
        'is_attack': bool(prediction[0])
    }
    return jsonify([alert])  # Return as a list for table display

if __name__ == '__main__':
    app.run(debug=True)
