# 🏠 Housing Price Prediction

A machine learning regression project that predicts **housing prices** based on property characteristics such as area, number of bedrooms and bathrooms, stories, parking, furnishing status, and various amenities.

The project demonstrates an end-to-end machine learning workflow, from **data exploration and preprocessing to model training and evaluation**.

---

## 📌 Project Overview

The goal of this project is to develop a regression model capable of estimating the price of a house based on its available features.

The dataset contains **545 housing records** with information about property size, structure, amenities, and furnishing status.

The target variable is:

```text
price
```

---

## 🎯 Objectives

* Explore and understand the housing dataset
* Perform exploratory data analysis (EDA)
* Identify important factors affecting house prices
* Handle categorical and numerical features
* Encode categorical variables
* Preprocess the dataset for machine learning
* Train a regression model
* Evaluate model performance using standard regression metrics
* Analyze the model's predictive performance

---

## 📊 Dataset Features

The dataset contains the following features:

| Feature            | Description                                         |
| ------------------ | --------------------------------------------------- |
| `price`            | Price of the house — target variable                |
| `area`             | Total area of the property                          |
| `bedrooms`         | Number of bedrooms                                  |
| `bathrooms`        | Number of bathrooms                                 |
| `stories`          | Number of stories                                   |
| `mainroad`         | Whether the property is connected to the main road  |
| `guestroom`        | Whether the property has a guest room               |
| `basement`         | Whether the property has a basement                 |
| `hotwaterheating`  | Whether the property has hot water heating          |
| `airconditioning`  | Whether the property has air conditioning           |
| `parking`          | Number of parking spaces                            |
| `prefarea`         | Whether the property is located in a preferred area |
| `furnishingstatus` | Furnishing status of the property                   |

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
Categorical Encoding
   ↓
Feature Preparation
   ↓
Train/Test Split
   ↓
Model Training
   ↓
Prediction
   ↓
Model Evaluation
```

---

## 🧹 Data Preprocessing

The dataset contains both **numerical and categorical features**.

### Numerical Features

Numerical features such as:

* Area
* Bedrooms
* Bathrooms
* Stories
* Parking

are prepared for model training using appropriate preprocessing techniques.

### Binary Categorical Features

Features containing `yes`/`no` values are converted into numerical representations:

```text
yes → 1
no  → 0
```

### Multi-Class Categorical Features

The `furnishingstatus` feature contains multiple categories:

```text
furnished
semi-furnished
unfurnished
```

These categorical values are encoded using **One-Hot Encoding**.

---

## 📈 Model Evaluation

The model was evaluated using commonly used regression metrics.

### Results

| Metric       |                    Score |
| ------------ | -----------------------: |
| **R² Score** |                **65.2%** |
| **MAE**      |           **970,043.40** |
| **MSE**      | **1,754,318,687,330.66** |
| **RMSE**     |         **1,324,506.96** |

### Interpretation

The model achieved an **R² score of 65.2%**, meaning it explains approximately **65.2% of the variation in housing prices** based on the features provided.

The **MAE of approximately 970K** means that, on average, the model's predictions differ from the actual house prices by around 970,043 currency units.

The **RMSE of approximately 1.32M** indicates the typical magnitude of prediction error while giving greater weight to larger errors.

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

## 📁 Project Structure

```text
Housing-Price-Prediction/
│
├── data/
│   └── housing.csv
│
├── notebooks/
│   └── housing_price_prediction.ipynb
│
├── README.md
└── requirements.txt
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/housing-price-prediction.git
```

Navigate to the project directory:

```bash
cd housing-price-prediction
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
venv\Scripts\activate
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

1. Clone the repository.
2. Install the required dependencies.
3. Place the dataset in the `data/` directory.
4. Open the Jupyter Notebook.
5. Run the notebook cells sequentially.
6. Explore the data analysis, preprocessing, model training, and evaluation results.

---

## 📌 Key Concepts Demonstrated

This project demonstrates practical knowledge of:

* Regression
* Exploratory Data Analysis
* Data preprocessing
* Feature engineering
* Categorical encoding
* One-Hot Encoding
* Binary encoding
* Train/Test splitting
* Model evaluation
* MAE, MSE, RMSE, and R²
* Data visualization
* Machine learning workflow

---

## 🚀 Future Improvements

Potential improvements for this project include:

* Comparing multiple regression algorithms
* Hyperparameter tuning
* Cross-validation
* Feature selection
* Outlier treatment
* Advanced feature engineering
* Model explainability
* Building an interactive Streamlit application
* Deploying the trained model as an API

---

## 👨‍💻 Author

**Zain Ali Khan**

Bachelor of Artificial Intelligence (BSAI)

---

## ⭐ Conclusion

This project provides a practical implementation of a **housing price prediction system using machine learning regression**. With an R² score of **65.2%**, the current model provides a reasonable baseline for predicting house prices while leaving room for further optimization and feature engineering.

If you found this project useful, consider giving the repository a ⭐.
