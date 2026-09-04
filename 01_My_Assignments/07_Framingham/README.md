# Framingham Heart Disease Prediction 🫀

A Machine Learning classification project that predicts whether a patient will develop **Coronary Heart Disease (CHD) within 10 years**, using the Framingham Heart Study dataset.

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

- **Source:** Framingham Heart Study
- **Rows:** 4238
- **Features:** 15 input features (age, sex, smoking habits, cholesterol, blood pressure, glucose, BMI, etc.)
- **Target column:** `TenYearCHD` → `0` = No CHD in 10 years, `1` = CHD in 10 years

## ⚙️ Tech Stack

- Python 3
- Pandas, NumPy – data handling
- Matplotlib, Seaborn – visualization
- Scikit-learn – ML models & metrics
- imbalanced-learn (SMOTE) – handling class imbalance

## 🧹 Data Preprocessing

1. **Missing Values:** Filled using the median of each column (`education`, `cigsPerDay`, `BPMeds`, `totChol`, `BMI`, `heartRate`, `glucose`)
2. **Duplicates:** Checked and removed
3. **Encoding:** `education` column (categorical: 1–4) one-hot encoded
4. **Scaling:** All features scaled using `StandardScaler`
5. **Imbalance Handling:** Dataset is imbalanced (~85% No CHD vs ~15% CHD) → balanced using **SMOTE** on the training set only

## 📊 Exploratory Data Analysis

The notebook includes visualizations for:
- Target class distribution
- Age distribution
- Gender vs CHD
- Smoking vs CHD
- Correlation heatmap
- Systolic BP vs CHD (boxplot)

## 🤖 Models Used

| Model | Accuracy | Precision | Recall | F1-Score |
|---|---|---|---|---|
| Logistic Regression | 0.665 | 0.249 | 0.597 | 0.352 |
| Random Forest | 0.724 | 0.244 | 0.388 | 0.299 |

> Note: Since the dataset is heavily imbalanced, **Recall and F1-Score matter more than raw Accuracy** for this medical use case — missing an actual CHD case (false negative) is more costly than a false alarm.

## 📈 Results

- Both models were evaluated with a full **Classification Report** and **Confusion Matrix**.
- Random Forest gave higher overall accuracy, while Logistic Regression achieved better recall on the minority (CHD) class after balancing with SMOTE.
- A Random Forest **Feature Importance** chart is included to show which health factors matter most for CHD prediction.

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
   jupyter notebook framingham_classification.ipynb
   ```
4. Run all cells from top to bottom.

## 📁 Repository Structure

```
├── framingham.csv                     # Dataset
├── framingham_classification.ipynb    # Full ML notebook (EDA + Models)
└── README.md                          # Project documentation
```

## 🔮 Future Improvements

- Hyperparameter tuning with `GridSearchCV` / `RandomizedSearchCV`
- Try additional models (XGBoost, SVM, KNN)
- Use ROC-AUC curve for further model comparison
- Deploy the best model as a simple web app (Streamlit/Flask)

## ✍️ Author

Zain Ali Khan
