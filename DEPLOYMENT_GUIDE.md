# Streamlit Cloud Deployment - Step by Step

## Prerequisites
- GitHub account (free)
- Your code ready to deploy

---

## Step 1: Create GitHub Repository

1. Go to https://github.com/
2. Click the **"+"** icon (top right corner)
3. Select **"New repository"**
4. Fill in:
   - Repository name: `movie-recommender`
   - Description: `Movie recommendation system with Streamlit`
   - Make it **PUBLIC** (required for free Streamlit Cloud)
   - **DO NOT** check "Add a README file"
5. Click **"Create repository"**

---

## Step 2: Push Code to GitHub

Open your terminal in the movie_recommender folder and run:

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/movie-recommender.git
git push -u origin main
```

**Replace `YOUR_USERNAME`** with your actual GitHub username!

Example: If your username is `john123`:
```bash
git remote add origin https://github.com/john123/movie-recommender.git
```

---

## Step 3: Verify Files on GitHub

Go to your repository on GitHub and make sure these files are there:
- ✅ app.py
- ✅ requirements.txt
- ✅ movie_list.pkl
- ✅ similarity_compressed.pkl
- ✅ .gitignore
- ✅ README.md

---

## Step 4: Deploy on Streamlit Cloud

1. Go to https://share.streamlit.io/

2. Click **"Sign in with GitHub"**

3. Authorize Streamlit Cloud to access your GitHub

4. Click **"New app"** button (top right)

5. Fill in the form:
   - **Repository:** Select `YOUR_USERNAME/movie-recommender`
   - **Branch:** `main`
   - **Main file path:** `app.py`

6. Click **"Deploy!"**

7. Wait 2-5 minutes for deployment

8. Your app will be live! 🎉

---

## Step 5: Get Your App URL

Your app will be available at:
```
https://YOUR_USERNAME-movie-recommender.streamlit.app
```

You can share this URL with anyone!

---

## Updating Your App

Whenever you make changes to your code:

```bash
git add .
git commit -m "Updated features"
git push
```

Streamlit Cloud will automatically redeploy your app!

---

## Troubleshooting

### Problem: Git not recognized
**Solution:** Install Git from https://git-scm.com/downloads

### Problem: Permission denied when pushing
**Solution:** Set up Git credentials:
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### Problem: App not loading on Streamlit Cloud
**Solution:** 
- Check the logs in Streamlit Cloud dashboard
- Verify all files are in GitHub
- Make sure requirements.txt is correct

### Problem: Files too large
**Solution:** Already handled! We compressed similarity.pkl from 176MB to 44MB

---

## Alternative: Use GitHub Desktop (Easier)

If you prefer a GUI:

1. Download GitHub Desktop: https://desktop.github.com/
2. Install and sign in
3. Click "Add" → "Create New Repository"
4. Choose the movie_recommender folder
5. Click "Publish repository"
6. Make it public
7. Then follow Step 4 above

---

## Need Help?

- Streamlit Docs: https://docs.streamlit.io/
- Streamlit Forum: https://discuss.streamlit.io/
- GitHub Docs: https://docs.github.com/

---

## Summary

1. Create GitHub repo (public)
2. Push code: `git init` → `git add .` → `git commit` → `git push`
3. Go to share.streamlit.io
4. Deploy your repo
5. Done! 🚀
