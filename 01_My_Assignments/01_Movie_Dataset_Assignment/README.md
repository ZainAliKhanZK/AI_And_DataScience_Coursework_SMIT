# 🎬 IMDB Movies — Exploratory Data Analysis

An exploratory data analysis (EDA) assignment on the IMDB Top Movies dataset, covering data filtering, aggregation, and visualization using `pandas`, `matplotlib`, and `seaborn`.

## 📊 Dataset

The dataset (`movie.csv`) contains **1,000 movies** with the following columns:

| Column | Description |
|---|---|
| `Series_Title` | Movie name |
| `Released_Year` | Year of release |
| `Certificate` | Age/content certification |
| `Runtime` | Duration (minutes) |
| `Genre` | One or more genres (comma-separated) |
| `IMDB_Rating` | IMDB rating (0–10) |
| `Meta_score` | Metacritic score (0–100) |
| `Director` | Director's name |
| `Star1` | Lead actor |
| `No_of_Votes` | Number of IMDB votes |
| `Gross` | Box office earnings (USD) |

## 🔍 Analysis Covered

This notebook works through a series of data analysis tasks, including:

- Finding the movie with the longest runtime
- Correlation between `IMDB_Rating` and `Meta_score`
- Top 10 directors by number of movies
- Average `Gross` revenue grouped by `Certificate`
- Top 5 highest-voted movies
- Splitting and counting unique genres across the dataset
- Filtering actors who worked in Action/Sci-Fi genres with an IMDB rating ≥ 8.0
- Movies with `Meta_score` > 90 and `IMDB_Rating` < 8.5
- Comparing Drama vs Action genre gross revenue distributions
- Directors with movies exceeding 500,000 votes
- Pre-2000 movies grossing above the dataset's median
- Movies where the lead actor is also the director

## 📈 Visualizations

- Horizontal bar charts (top directors, top voted movies)
- Grouped/comparison bar charts (IMDB rating vs Meta score)
- Box plot comparing genre-wise gross revenue distributions (log scale)

## 🛠️ Tools Used

- Python
- Pandas
- Matplotlib
- Seaborn
- NumPy

## 📁 Files

- `movie_eda.ipynb` — main analysis notebook
- `movie.csv` — dataset used

## 🚀 How to Run

```bash
pip install pandas matplotlib seaborn numpy
jupyter notebook movie_eda.ipynb
```

## 👤 Author

**Zain Ali Khan**
Bachelor's in Artificial Intelligence, Sindh Madressatul Islam University (SMIU), Karachi

- GitHub: [@ZainAliKhanZK](https://github.com/ZainAliKhanZK)
