# Alternative Data-Enhanced Credit Risk Scoring Framework using UPI Behavioral Analytics

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10-blue)
![XGBoost](https://img.shields.io/badge/XGBoost-ML-green)
![Power BI](https://img.shields.io/badge/PowerBI-Dashboard-yellow)
![License](https://img.shields.io/badge/License-MIT-red)

</p>

## 📌 Project Overview
Traditional credit scoring systems primarily rely on financial history and bureau information, making it difficult to accurately assess applicants with limited or no formal credit records. This project proposes an **Alternative Data-Enhanced Credit Risk Scoring Framework** that incorporates **UPI transaction behavior** into conventional credit risk assessment.

The framework combines traditional credit features with engineered behavioral indicators derived from UPI transactions to improve creditworthiness prediction. A **Random Forest** model is used as the baseline, while an **XGBoost** classifier serves as the enhanced model. The project also includes an interactive **Power BI dashboard** for exploratory analysis and business insights.

---
## 🚀 Project Highlights

- Developed an alternative data-enhanced credit risk prediction framework.
- Engineered behavioral features from UPI transaction data.
- Compared Random Forest and XGBoost models for credit risk prediction.
- Achieved a ROC-AUC improvement from **0.7183** to **0.7457**.
- Built an interactive Power BI dashboard for business insights.
## Table of Contents

- Overview
- Objectives
- Key Features
- System Architecture
- Dashboard Preview
- Machine Learning Models
- Model Performance
- Confusion Matrix
- Repository Structure
- Technologies Used
- Installation
- Future Work
- Contributors

## 🎯 Objectives

- Develop a robust credit risk prediction framework using alternative financial data.
- Engineer behavioral features from UPI transaction patterns.
- Compare a baseline Random Forest model with an enhanced XGBoost model.
- Visualize borrower characteristics and behavioral insights using Power BI.
- Improve credit assessment for users with limited credit history.

---

## ✨ Key Features

- Alternative data-driven credit scoring
- UPI behavioral feature engineering
- Random Forest baseline model
- Enhanced XGBoost classifier
- Feature importance analysis
- Interactive Power BI dashboard
- Comprehensive model evaluation

---

## 🏗️ System Architecture

<p align="center">
<img width="359" height="970" alt="architecture" src="https://github.com/user-attachments/assets/7582e5ad-d506-4206-b22e-db441faaa24b" />
</p>

---

## 📊 Dashboard Preview

### Executive Summary

<img width="1197" height="666" alt="dashboard_d1" src="https://github.com/user-attachments/assets/712e5f19-806f-4962-b393-b4871fe45472" />


### Credit Risk Drivers

<img width="1205" height="665" alt="dashboard_d2" src="https://github.com/user-attachments/assets/da12e861-e17a-456a-8173-25378efc11d0" />

### UPI Behavioral Analytics

<img width="1197" height="670" alt="dashboard_d3" src="https://github.com/user-attachments/assets/19e56548-dd36-41f4-a692-4481e0129e75" />

---

## 🤖 Machine Learning Models

| Model | Algorithm |
|-------|-----------|
| Baseline | Random Forest Classifier |
| Enhanced | XGBoost Classifier |

---

## 📈 Model Performance

### ROC-AUC Comparison

| Model | ROC-AUC |
|--------|--------:|
| Random Forest | **0.7183** |
| XGBoost | **0.7457** |
| Improvement | **+0.0274** |

### Enhanced XGBoost Performance

| Metric | Value |
|--------|-------:|
| Accuracy | **96.88%** |
| Precision | **94.03%** |
| Recall | **98.44%** |
| F1-Score | **96.18%** |
| Specificity | **95.83%** |

---

## 📌 Confusion Matrix

<p align="center">
<img width="550" height="547" alt="confusion_matrix" src="https://github.com/user-attachments/assets/fc415b1c-62ba-4c0d-93e4-83b0a91ea5e4" />
</p>

The enhanced XGBoost model correctly classified **155 out of 160** evaluation samples while maintaining high precision and recall for identifying high-risk borrowers.

---

## ⭐ Feature Importance

The enhanced model provides feature importance scores to identify the variables contributing most significantly to credit risk prediction.

The feature importance output is available in:

```
results/feature_importance.csv
```

---

## 📂 Repository Structure

```text
Alternative-Data-Credit-Risk-Scoring
│
├── src/
├── models/
├── results/
├── dashboard/
│   └── screenshots/
├── docs/
├── README.md
├── requirements.txt
├── LICENSE
└── .gitignore
```

---

## 🛠️ Technologies Used

### Programming

- Python

### Machine Learning

- Scikit-learn
- XGBoost

### Data Processing

- Pandas
- NumPy

### Visualization

- Power BI
- Matplotlib

### Model Serialization

- Joblib

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Alternative-Data-Credit-Risk-Scoring.git
```

Install the required libraries

```bash
pip install -r requirements.txt
```

Run

```bash
python src/model_training.py
```

---

## 🔮 Future Enhancements

- Deep learning-based credit scoring models
- Explainable AI using SHAP and LIME
- Real-time UPI transaction scoring
- API deployment using FastAPI
- Cloud-based dashboard deployment

---

## 👥 Contributors

- **Dipyaman Chakraborty** — Data Analytics, Power BI Dashboard, Feature Engineering, Repository Management
- **Arkajit Chaudhuri** — Machine Learning Model Development and Optimization

---

## 📜 License
This project is released under the MIT License.
