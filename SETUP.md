# Setup Guide

## ⚠️ IMPORTANT: API Key Security

Your API key has been removed from the code and git history.

### Get a New TMDB API Key

1. Go to https://www.themoviedb.org/settings/api
2. **Delete the old exposed key**
3. **Generate a new API key**
4. Copy the new key

---

## Local Development Setup

1. Create `.streamlit/secrets.toml` file:
```toml
TMDB_API_KEY = "your_new_api_key_here"
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the app:
```bash
streamlit run app.py
```

---

## Deploy to Streamlit Cloud

1. Go to https://share.streamlit.io/
2. Sign in with GitHub
3. Click "New app"
4. Select repository: `Asadp3406/Movie-Recommender`
5. Branch: `main`
6. File: `app.py`
7. Click "Deploy"

### Add API Key to Streamlit Cloud

**IMPORTANT:** After deployment:

1. Click on your app
2. Click "⚙️ Settings"
3. Go to "Secrets" tab
4. Add:
```toml
TMDB_API_KEY = "your_new_api_key_here"
```
5. Click "Save"

---

## What's Fixed

✅ API key removed from code
✅ API key removed from git history
✅ `.gitignore` updated to exclude secrets
✅ App now reads API key from secrets only

---

## Files Structure

```
movie_recommender/
├── app.py                      # Main application
├── requirements.txt            # Dependencies
├── movie_list.pkl             # Movie data
├── similarity_compressed.pkl  # Similarity matrix
├── README.md                  # Documentation
├── .gitignore                 # Git exclusions
└── .streamlit/
    └── secrets.toml          # API key (NOT in git)
```

---

## Security Notes

- Never commit `.streamlit/secrets.toml` to git
- Always use secrets management for API keys
- Rotate API keys if exposed
- The `.gitignore` now prevents secrets from being committed
