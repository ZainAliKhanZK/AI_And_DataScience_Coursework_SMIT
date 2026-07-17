# 🏦 Loan Approval Dataset - Data Cleaning & Exploratory Data Analysis (EDA)

This project demonstrates the complete data preprocessing and exploratory data analysis (EDA) workflow on the **Loan Approval Dataset** using **Python, Pandas, Matplotlib, and Seaborn**.

The objective of this project is to clean the dataset, handle missing values, detect and remove outliers, visualize important relationships, and prepare the dataset for future machine learning models.

---

## 📌 Project Objectives

- Load and inspect the dataset
- Explore dataset structure and data types
- Handle missing values using appropriate techniques
- Detect and remove outliers using the IQR method
- Perform exploratory data analysis (EDA)
- Visualize key insights affecting loan approval
- Export the cleaned dataset for further analysis

---

## 📊 Exploratory Data Analysis Performed

### Dataset Exploration
- Dataset overview (`head()`, `tail()`)
- Dataset information (`info()`)
- Missing value analysis
- Duplicate record check

### Data Cleaning
- Filled missing categorical values using **Mode**
- Filled missing numerical values using **Median**
- Removed outliers from the `LoanAmount` column using the **Interquartile Range (IQR)** method

### Visualizations
- Loan Approval Distribution
- Credit History vs Loan Approval
- Boxplot for Loan Amount

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn

---

## 📂 Project Workflow

1. Load the dataset
2. Explore the dataset
3. Handle missing values
4. Check for duplicate records
5. Detect and remove outliers
6. Perform exploratory data analysis
7. Visualize important features
8. Save the cleaned dataset

---

## 📁 Output

- Cleaned Loan Dataset (`Cleaned_Loan_Dataset.csv`)
- EDA visualizations
- Preprocessed dataset ready for machine learning

---

## 📈 Key Insights

- Applicants with a positive **Credit History** have a significantly higher loan approval rate.
- Missing values were successfully handled using statistical imputation techniques.
- Outliers in the **LoanAmount** feature were identified and removed using the IQR method.
- The cleaned dataset is suitable for predictive modeling and further machine learning tasks.

---

## 🚀 Future Improvements

- Feature Engineering
- Label Encoding & One-Hot Encoding
- Feature Scaling
- Machine Learning Model Training
- Hyperparameter Tuning
- Model Evaluation and Performance Comparison

---

## 📜 License

This project is created for learning and educational purposes.
