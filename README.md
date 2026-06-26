# 🛡️ Intrusion Detection System (IDS-Guard)

A real-time, ML-powered network intrusion detection system with a live alert dashboard.

---

## 🗂️ Project Structure

```
intusion_detection_system/
├── backend/        # Flask REST API + ML model (RandomForest)
└── frontend/       # HTML/CSS/JS alert dashboard
```
---
## 🗃️ Dataset
 
This project uses a **predefined CSV dataset** (`full_alert_database.csv`) to train the model. No live network capture is required.
 
| Column | Description |
|--------|-------------|
| `time` | Timestamp of the event |
| `type` | Attack category |
| `severity` | Risk level |
| `source` | Source IP address |
| `packet_size` | Size of the network packet (bytes) |
| `duration` | Connection duration (seconds) |
| `flag_count` | Number of TCP flags set |
| `is_attack` | Label — `1` = attack, `0` = normal |
 
**Sample rows:**
 
```
time,type,severity,source,packet_size,duration,flag_count,is_attack
2025-04-22 15:00:00,DDoS,High,192.168.1.100,1500,5.0,10,1
2025-04-22 15:01:00,SQL Injection,Medium,192.168.1.101,500,2.5,5,1
2025-04-22 15:02:00,Port Scan,Low,192.168.1.102,300,1.0,3,1
2025-04-22 15:03:00,Normal Traffic,Low,192.168.1.103,100,0.5,0,0
2025-04-22 15:04:00,Brute Force,High,192.168.1.104,800,3.2,7,1
2025-04-22 15:05:00,XSS,Medium,192.168.1.105,450,1.8,4,1
2025-04-22 15:06:00,Data Exfiltration,Critical,192.168.1.106,2000,4.5,9,1
2025-04-22 15:07:00,Ransomware,Critical,192.168.1.107,1700,5.0,8,1
```
 
---
 
## 🛠️ Technologies Used
 
**Backend**
- `Python 3.x` — core language
- `Flask` — REST API server
- `Flask-CORS` — cross-origin request handling
- `scikit-learn` — ML pipeline (RandomForestClassifier, OrdinalEncoder, ColumnTransformer)
- `Pandas` — data loading and preprocessing
- `joblib` — model serialization and loading
**Frontend**
- `HTML5` — dashboard structure
- `CSS3` — dark neon theme, severity color-coding
- `JavaScript (Vanilla)` — async fetch, DOM rendering
---
 
## ✨ Features
 
- 🤖 **ML-based detection** — RandomForest trained on predefined network traffic data
- ⚖️ **Class balancing** — handles imbalanced attack vs. normal traffic
- 🔁 **Model persistence** — trains once, saves with `joblib`, reloads on restart
- 📡 **REST API** — `/api/alerts` returns live predictions as JSON
- 🖥️ **Live dashboard** — alerts rendered in real time without page reload
- 🎨 **Severity color-coding**:
  - 🟢 `Low` — green
  - 🟠 `Medium` — orange
  - 🔴 `High` / `Critical` — red bold
---
 
## 👤 What Users Can Do
 
- Click **"Check Alerts"** to fetch the latest predicted network event
- View alert details: timestamp, attack type, severity, and source IP
- Instantly identify critical threats by color — no reading required
- Refresh as many times as needed; each click generates a new prediction
---
 
## ⌨️ Keyboard Shortcuts
 
| Shortcut | Action |
|----------|--------|
| `Enter` | Trigger "Check Alerts" (when button is focused) |
| `Tab` | Navigate to the Check Alerts button |
| `F5` | Refresh the page / reset the dashboard |
 
---
 
## ⚙️ How I Built It
 
### 1. Dataset Preparation
Created a structured CSV (`full_alert_database.csv`) with labeled network events covering attack types like DDoS, SQL Injection, Port Scan, Ransomware, and normal traffic.
 
### 2. ML Pipeline
Built a `scikit-learn` Pipeline combining:
- `ColumnTransformer` with `OrdinalEncoder` for categorical columns (`type`, `severity`, `source`)
- `RandomForestClassifier` for binary classification (`is_attack`: 0 or 1)
Model trained on first run and persisted to `ids_model.joblib` — skipped on subsequent runs.
 
### 3. Flask API
Exposed a `/api/alerts` endpoint that:
- Randomly samples an alert type and source IP
- Runs it through the loaded model
- Returns the prediction + confidence score as JSON
### 4. Frontend Dashboard
Built a minimal dark-themed HTML/CSS/JS page:
- Button triggers a `fetch()` call to the Flask API
- Response populates an alert table dynamically
- Severity class applied per row for instant visual triage
---
 
## 📚 What I Learnt
 
- Building end-to-end ML pipelines with `scikit-learn` (preprocessing → training → saving → serving)
- How to expose a trained model as a REST API using Flask
- Handling class imbalance in real-world network datasets
- Connecting a vanilla JS frontend to a Python backend via async `fetch()`
- Structuring a full-stack project cleanly across `backend/` and `frontend/` folders
---
 
## 📊 Model Performance
 
| Metric | Before Balancing | After Balancing |
|--------|-----------------|-----------------|
| Accuracy | 99.1% | 99.9% |
| Attack Recall | 4–12% | 85–95% |
| F1-Score | 5–12% | 90–93% |
| ROC-AUC | 0.87–0.91 | 0.98–0.99 |
 
---
 
## 🔮 Future Improvements
 
- [ ] Integrate **SMOTE** directly into the pipeline for automated class balancing
- [ ] Replace predefined dataset with **live packet capture** (using Scapy or pyshark)
- [ ] Add **deep learning model** (LSTM/DNN) for sequential pattern detection
- [ ] Build a **severity trend chart** on the dashboard using Chart.js
- [ ] Add **IP blocking simulation** when Critical alerts are detected
- [ ] Export alert logs as downloadable CSV from the dashboard
- [ ] Add **authentication** to the dashboard for production use
---
 
## 🚀 Running the Project
 
### Prerequisites
```bash
pip install flask flask-cors scikit-learn pandas joblib
```
 
### Step 1 — Start the Backend
```bash
cd backend
python app.py
```
> Flask runs on `http://127.0.0.1:5000`  
> Model trains automatically on first run and saves as `ids_model.joblib`
 
### Step 2 — Open the Frontend
```bash
# Just open this file in your browser
frontend/index.html
```
 
### Step 3 — Use the Dashboard
- Click **"Check Alerts"** to fetch a live prediction
- Each click runs the ML model and returns a new alert
> ⚠️ Make sure the Flask backend is running before opening the dashboard, or the fetch will fail.
 
---
