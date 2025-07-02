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

## 📊 EDA
- Number of movies per genre
- Sentiment polarity distribution
- Description length distribution

## ✅ Next steps
- Build NLP models to predict genres
- Topic modeling
- Build a small app to explore data
