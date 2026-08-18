# 📊 Exam Score Prediction

A machine learning project that predicts students' **exam scores** based on factors such as study time and other academic or demographic features.

The project demonstrates a complete machine learning workflow, including **data exploration, preprocessing, feature engineering, visualization, model training, and evaluation**.

---

## 📌 Project Overview

Student performance can be influenced by several factors, including study habits, attendance, previous academic performance, and other personal or academic characteristics.

This project uses student-related data to build a **regression model** capable of predicting an individual's exam score.

The primary objective is to understand which features have the strongest relationship with exam performance and develop a machine learning model that can make accurate predictions.

---

## 🎯 Objectives

* Explore and understand the dataset
* Perform exploratory data analysis (EDA)
* Identify relationships between features and exam scores
* Handle missing and inconsistent data
* Encode categorical variables
* Standardize numerical features where appropriate
* Separate features and the target variable
* Train regression models
* Evaluate model performance
* Analyze prediction results

---

## 🛠️ Technologies & Libraries

* **Python**
* **Pandas** — Data manipulation and analysis
* **NumPy** — Numerical computing
* **Matplotlib** — Data visualization
* **Seaborn** — Statistical visualization
* **Scikit-learn** — Machine learning and preprocessing
* **Jupyter Notebook** — Development and experimentation

---

## 🔄 Machine Learning Workflow

```text
Dataset
   ↓
Data Loading
   ↓
Data Exploration
   ↓
Data Cleaning
   ↓
Exploratory Data Analysis
   ↓
Feature Engineering
   ↓
Categorical Encoding
   ↓
Numerical Feature Scaling
   ↓
Train/Test Split
   ↓
Model Training
   ↓
Model Evaluation
   ↓
Exam Score Prediction
```

---

## 📊 Exploratory Data Analysis

Several visualizations are used to understand the dataset and identify important patterns.

For example, the relationship between **Study Time** and **Exam Score** can help determine whether students who spend more time studying tend to achieve higher scores.

Other EDA techniques include:

* Distribution analysis
* Correlation analysis
* Feature comparison
* Outlier detection
* Categorical feature analysis

---

## 🧹 Data Preprocessing

The preprocessing stage includes:

### Numerical Features

Numerical features are standardized when required by the selected machine learning algorithm.

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_numeric_scaled = scaler.fit_transform(X[numeric_cols])
```

The target variable, **Exam Score**, is kept separate from feature scaling because it is the prediction target.

### Categorical Features

Categorical variables are converted into numerical representations using appropriate encoding techniques such as:

* One-Hot Encoding
* Label Encoding

---

## 🤖 Machine Learning

The project is designed as a **regression problem**, where the target variable is:

```text
Exam Score
```

The model learns patterns from the input features and predicts a continuous exam score for new students.

Possible regression algorithms include:

* Linear Regression
* Ridge Regression
* Lasso Regression
* Decision Tree Regressor
* Random Forest Regressor
* Gradient Boosting Regressor

---

## 📈 Model Evaluation Results

The trained model can be evaluated using common regression metrics:

### Mean Absolute Error (MAE)

Measures the average absolute difference between actual and predicted scores.

### Mean Squared Error (MSE)

Penalizes larger prediction errors more heavily.

### Root Mean Squared Error (RMSE)

Provides the prediction error in the same unit as the target variable.

### R² Score

Measures how well the model explains the variation in exam scores.

## Evaluation Results:

- **R2 score : 89.6%**
- **MAE : 4.18**
- **MSE : 26.5**
- **RMSE : 5.15**

```python
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = mse ** 0.5
r2 = r2_score(y_test, y_pred)

print("MAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)
print("R² Score:", r2)
```

---

## 📁 Project Structure

```text
Exam-Score-Prediction/
│
├── data/
│   └── dataset.csv
│
├── notebooks/
│   └── exam_score_prediction.ipynb
│
├── README.md
└── requirements.txt
```

> The project structure may vary depending on the final implementation.

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/exam-score-prediction.git
```

Navigate to the project directory:

```bash
cd exam-score-prediction
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment on Windows:

```powershell
venv\Scripts\activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

1. Clone the repository.
2. Install the required dependencies.
3. Place the dataset inside the `data/` directory.
4. Open the Jupyter Notebook.
5. Run the cells sequentially.
6. Explore the analysis and model results.

---

## 📌 Key Concepts Demonstrated

This project demonstrates practical understanding of:

* Data preprocessing
* Exploratory Data Analysis
* Feature selection
* Categorical encoding
* Feature scaling
* Train-test splitting
* Regression
* Model evaluation
* Data visualization
* Machine learning workflow

---

## 🚀 Future Improvements

Potential improvements include:

* Hyperparameter tuning
* Cross-validation
* Feature selection
* Comparing multiple regression algorithms
* Model explainability
* Interactive prediction interface using Streamlit
* Model deployment through an API
* Saving the trained model for production use

---

## 👨‍💻 Author

**Zain Ali Khan**

Bachelor of Artificial Intelligence (BSAI)

---

## ⭐ Acknowledgements

This project was developed as part of practical learning in **Machine Learning, Data Science, and Artificial Intelligence**.

If you find this project useful, consider giving the repository a ⭐.
