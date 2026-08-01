# Alternative Data-Enhanced Credit Risk Scoring using UPI Behavioral Analytics

## Overview

Traditional credit scoring systems primarily rely on financial history and bureau information, making it difficult to accurately assess applicants with limited or no formal credit records. This project proposes an **Alternative Data-Enhanced Credit Risk Scoring Framework** that incorporates **UPI transaction behavior** into conventional credit risk assessment.

The framework combines traditional credit features with engineered behavioral indicators derived from UPI transactions to improve creditworthiness prediction. A **Random Forest** model is used as the baseline, while an **XGBoost** classifier serves as the enhanced model. The project also includes an interactive **Power BI dashboard** for exploratory analysis and business insights.

---

## Objectives

- Develop a robust credit risk prediction framework using alternative financial data.
- Engineer behavioral features from UPI transaction patterns.
- Compare a baseline Random Forest model with an enhanced XGBoost model.
- Visualize borrower characteristics and behavioral insights using Power BI.
- Improve credit assessment for users with limited credit history.

---

## Key Features

- Alternative data-driven credit scoring
- UPI behavioral feature engineering
- Random Forest baseline model
- Enhanced XGBoost classifier
- Feature importance analysis
- Interactive Power BI dashboard
- Comprehensive model evaluation

---

## System Architecture

<p align="center">
<img src="docs/architecture.png" width="850">
</p>

---

## Dashboard Preview

### Executive Summary

*(Add screenshot here)*

### Credit Risk Drivers

*(Add screenshot here)*

### UPI Behavioral Analytics

*(Add screenshot here)*

---

## Machine Learning Models

| Model | Algorithm |
|-------|-----------|
| Baseline | Random Forest Classifier |
| Enhanced | XGBoost Classifier |

---

## Model Performance

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

## Confusion Matrix

<p align="center">
<img src="results/confusion_matrix.png" width="500">
</p>

The enhanced XGBoost model correctly classified **155 out of 160** evaluation samples while maintaining high precision and recall for identifying high-risk borrowers.

---

## Feature Importance

The enhanced model provides feature importance scores to identify the variables contributing most significantly to credit risk prediction.

The feature importance output is available in:

```
results/feature_importance.csv
```

---

## Repository Structure

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

## Technologies Used

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

## Installation

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

## Future Enhancements

- Deep learning-based credit scoring models
- Explainable AI using SHAP and LIME
- Real-time UPI transaction scoring
- API deployment using FastAPI
- Cloud-based dashboard deployment

---

## Contributors

- **Dipyaman Chakraborty** — Data Analytics, Power BI Dashboard, Feature Engineering, Repository Management
- **Arkajit Chaudhuri** — Machine Learning Model Development and Optimization

---

## License

This project is released under the MIT License.
