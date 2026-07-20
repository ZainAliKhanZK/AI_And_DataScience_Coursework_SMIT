# Adult Census Income Dataset — EDA

Exploratory data analysis of the **Adult (Census Income)** dataset, a classic benchmark for binary income classification based on U.S. Census demographic and employment data.

## Dataset Overview

- **Rows:** 48,842
- **Columns:** 15 (6 numeric, 9 categorical)
- **Target:** `income` — whether an individual earns `<=50K` or `>50K` annually
- **Class balance:** 76.1% `<=50K` vs. 23.9% `>50K` (moderately imbalanced)

| Column | Type | Description |
|---|---|---|
| `age` | numeric | Age in years |
| `workclass` | categorical | Type of employer |
| `fnlwgt` | numeric | Census sampling weight |
| `education` | categorical | Highest education level |
| `educational-num` | numeric | Education level, encoded numerically |
| `marital-status` | categorical | Marital status |
| `occupation` | categorical | Occupation |
| `relationship` | categorical | Relationship role in household |
| `race` | categorical | Race |
| `gender` | categorical | Gender |
| `capital-gain` / `capital-loss` | numeric | Investment income/loss |
| `hours-per-week` | numeric | Weekly working hours |
| `native-country` | categorical | Country of origin |
| `income` | categorical | Target: `<=50K` or `>50K` |

## Key Findings

- **Missing values are disguised as `"?"`**, not `NaN` — found in `workclass` (5.7%), `occupation` (5.8%), and `native-country` (1.8%).
- **`education` and `educational-num` are fully redundant** (1:1 mapping); one should be dropped before modeling.
- **`fnlwgt`** is a census sampling weight, not a personal attribute — weak correlation with all other features and typically excluded as a predictor.
- **Strongest predictors of income:** `marital-status`, `education`, `age` (non-linear, peaking mid-career), `hours-per-week`, and `capital-gain` (despite being ~92% zero, non-zero values strongly indicate higher income).
- **A gender income gap persists even within the same education tier** — worth noting as a fairness consideration for any downstream model.

## Data Cleaning Steps

1. Replace `"?"` with `NaN` and impute as `"Unknown"` (missingness is non-random, not safely filled with the mode).
2. Drop duplicate rows (52 found).
3. Drop one of `education` / `educational-num` to avoid redundancy.
4. Consider dropping `fnlwgt` for classification tasks.

## Repository Structure

```
├── data/
│   └── adult.csv
├── notebooks/
│   └── eda.ipynb
├── README.md
└── requirements.txt
```

## Source

UCI Machine Learning Repository — [Adult Data Set](https://archive.ics.uci.edu/dataset/2/adult)
