# Heart Failure Clinical Records Prediction ❤️‍🩹

A Machine Learning classification project that predicts whether a patient will **survive or die (`DEATH_EVENT`)** from heart failure, based on their clinical records.

## 📌 Project Overview

This project follows a complete Machine Learning workflow — from raw data to a trained, evaluated model:

- Data Cleaning (missing values, duplicates)
- One Hot Encoding of categorical features
- Exploratory Data Analysis (EDA) with charts
- Feature Scaling
- Handling Class Imbalance (SMOTE)
- Training and comparing 2 classification models
- Model evaluation using Accuracy, Precision, Recall, F1-Score, Classification Report & Confusion Matrix

## 📂 Dataset

- **Source:** Heart Failure Clinical Records Dataset
- **Rows:** 299
- **Features:** 12 input features (age, anaemia, creatinine phosphokinase, diabetes, ejection fraction, high blood pressure, platelets, serum creatinine, serum sodium, sex, smoking, follow-up time)
- **Target column:** `DEATH_EVENT` → `0` = Survived, `1` = Died

## ⚙️ Tech Stack

- Python 3
- Pandas, NumPy – data handling
- Matplotlib, Seaborn – visualization
- Scikit-learn – ML models & metrics
- imbalanced-learn (SMOTE) – handling class imbalance

## 🧹 Data Preprocessing

1. **Missing Values:** Checked column by column — this dataset has none, but the code fills any with the median automatically if found
2. **Duplicates:** Checked and removed (none found in this dataset)
3. **Encoding:** All features here are already numeric (0/1 flags or continuous values), so the notebook checks for categorical columns automatically and one-hot encodes them if any exist
4. **Scaling:** All features scaled using `StandardScaler`
5. **Imbalance Handling:** Dataset is mildly imbalanced (~68% Survived vs ~32% Died) → balanced using **SMOTE** on the training set only

## 📊 Exploratory Data Analysis

The notebook includes visualizations for:
- Target class distribution
- Age distribution
- Ejection fraction vs death event
- Smoking vs death event
- Correlation heatmap
- Serum creatinine vs death event (boxplot)

## 🤖 Models Used

| Model | Accuracy | Precision | Recall | F1-Score |
|---|---|---|---|---|
| Logistic Regression | 0.800 | 0.733 | 0.579 | 0.647 |
| Random Forest | 0.800 | 0.684 | 0.684 | 0.684 |

> Note: Both models reached the same accuracy, but **Random Forest gives a more balanced Precision/Recall trade-off**, making it the better pick for this medical use case where missing a death event (false negative) is costly.

## 📈 Results

- Both models were evaluated with a full **Classification Report** and **Confusion Matrix**.
- A Random Forest **Feature Importance** chart is included to show which clinical factors matter most for predicting survival — `time` (follow-up period), `ejection_fraction`, and `serum_creatinine` tend to be the strongest predictors.

## 🚀 How to Run

1. Clone this repository
   ```bash
   git clone <repo-url>
   cd <repo-folder>
   ```
2. Install the required libraries
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn imbalanced-learn jupyter
   ```
3. Open the notebook
   ```bash
   jupyter notebook heart_failure_classification.ipynb
   ```
4. Run all cells from top to bottom.

## 📁 Repository Structure

```
├── heart_failure.csv                     # Dataset
├── heart_failure_classification.ipynb    # Full ML notebook (EDA + Models)
└── README.md                             # Project documentation
```

## 🔮 Future Improvements

- Hyperparameter tuning with `GridSearchCV` / `RandomizedSearchCV`
- Try additional models (XGBoost, SVM, KNN)
- Use ROC-AUC curve for further model comparison
- Deploy the best model as a simple web app (Streamlit/Flask)

## ✍️ Author

Zain Ali Khan
