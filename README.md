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

## ⚙️ How It Works

1. **ML Model** — A `RandomForestClassifier` inside a `scikit-learn Pipeline` classifies network events as normal or malicious
2. **Class Balancing** — SMOTE used to handle imbalanced data, boosting attack recall from ~6% → 85–95%
3. **REST API** — Flask serves predictions via `/api/alerts`
4. **Dashboard** — Live alert table, color-coded by severity (Low / Medium / High / Critical)

---

## 🛠️ Stack

| Layer | Tools |
|-------|-------|
| ML | `scikit-learn`, `RandomForestClassifier`, `joblib` |
| Data | `Pandas`, `OrdinalEncoder`, `ColumnTransformer` |
| Backend | `Flask`, `Flask-CORS` |
| Frontend | `HTML`, `CSS`, `JavaScript` |

---

## 📊 Results

| Metric | Before SMOTE | After SMOTE |
|--------|-------------|-------------|
| Accuracy | 99.1% | 99.9% |
| Attack Recall | 4–12% | 85–95% |
| F1-Score | 5–12% | 90–93% |
| ROC-AUC | 0.87–0.91 | 0.98–0.99 |

---

## 🚀 Run Locally

```bash
# Backend
cd backend
pip install -r requirements.txt
python app.py

# Frontend
# Open frontend/index.html in your browser
```

---

## 👤 Author

**Shrey Rao** — [LinkedIn](https://linkedin.com/in/YOUR_LINKEDIN) · [shreyrao2004@gmail.com](mailto:shreyrao2004@gmail.com)
