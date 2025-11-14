# URGENT: Fix Exposed API Key

## ⚠️ Your API key was exposed on GitHub!

Don't panic - follow these steps to secure it:

---

## Step 1: Get a New API Key (IMPORTANT!)

1. Go to https://www.themoviedb.org/settings/api
2. Login to your TMDB account
3. Delete the old API key: `2171b9b5556bd2747edf8e75b027aafe`
4. Generate a new API key
5. Copy the new key

---

## Step 2: Update Local Secrets File

1. Open `.streamlit/secrets.toml`
2. Replace with your NEW API key:
```toml
TMDB_API_KEY = "YOUR_NEW_API_KEY_HERE"
```

---

## Step 3: Remove API Key from Git History

Run these commands:

```bash
# Remove the commit with the API key
git reset --soft HEAD~1

# Stage the fixed files
git add .

# Commit again with the fixed code
git commit -m "Secure API key using secrets"

# Force push to overwrite GitHub history
git push -f origin main
```

---

## Step 4: Add Secret to Streamlit Cloud

1. Go to https://share.streamlit.io/
2. Click on your app
3. Click "Settings" (⚙️ icon)
4. Go to "Secrets" section
5. Add this:
```toml
TMDB_API_KEY = "YOUR_NEW_API_KEY_HERE"
```
6. Click "Save"

---

## ✅ What I've Already Fixed:

1. ✅ Moved API key to `.streamlit/secrets.toml`
2. ✅ Updated `.gitignore` to exclude secrets file
3. ✅ Modified `app.py` to read from secrets
4. ✅ Added fallback for local development

---

## How It Works Now:

- **Local:** Reads from `.streamlit/secrets.toml` (not in git)
- **Streamlit Cloud:** Reads from app secrets settings
- **Secure:** API key never committed to GitHub again

---

## Prevention:

The `.gitignore` now includes:
```
.streamlit/secrets.toml
```

This ensures secrets are never committed!

---

## Need Help?

- TMDB API Docs: https://developers.themoviedb.org/
- Streamlit Secrets: https://docs.streamlit.io/streamlit-community-cloud/deploy-your-app/secrets-management
