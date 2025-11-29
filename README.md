# Movie Recommender System

A content-based movie recommendation system built with Streamlit that suggests similar movies based on genres, keywords, cast, and crew.

## Features

- 4800+ movies database
- Content-based filtering algorithm
- Movie posters from TMDB API
- Clean and responsive UI

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Create `.streamlit/secrets.toml` and add your TMDB API key:
```toml
TMDB_API_KEY = "your_api_key_here"
```

3. Run the app:
```bash
streamlit run app.py
```

## Deployment

This app is deployed on Streamlit Cloud. To deploy your own:

1. Fork this repository
2. Go to [share.streamlit.io](https://share.streamlit.io/)
3. Deploy from your GitHub repo
4. Add your TMDB API key in app secrets

## Tech Stack

- Python
- Streamlit
- Pandas
- Scikit-learn
- TMDB API
