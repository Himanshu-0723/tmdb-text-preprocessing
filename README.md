# 🎬 TMDB Movie Dataset: Text Preprocessing & EDA

In this project, I built my own dataset by fetching ≈10,000 popular movies from the TMDB API.  
Then I applied standard text preprocessing and performed exploratory data analysis (EDA).

## 📦 Project structure
- `fetch_data.py`: Script to fetch data from TMDB API and save as CSV
- `data.ipynb`: Jupyter notebook with text preprocessing and EDA
- `movies.csv`: Raw dataset (title, description, genres)

## 🧹 Preprocessing steps
- Lowercasing
- Removing punctuation
- Stopword removal
- Lemmatization


## 📊 Exploratory Data Analysis (EDA)

To better understand the dataset and guide further cleaning or modeling, I explored:

- **Number of movies per genre**: shows which genres are most common in the dataset.
- **Sentiment polarity distribution**: checks if descriptions are generally positive, negative, or neutral.
- **Description length distribution**: helps see if descriptions are usually short or long.
- **Presence of URLs and HTML tags**: detects potential noise in the text that might need extra cleaning.


## ✅ Next steps
- Build NLP models to predict genres
- Topic modeling
- Build a small app to explore data
