# Backend & Frontend Deployment Guide

## PART I – BACKEND DEPLOYMENT ON RENDER

### Step 1 — Create a Render Account
1. Go to https://render.com
2. Click "Sign Up" and register using your **GitHub account**
   - You need a GitHub account to link your backend repository

### Step 2 — Link Your GitHub Repository
1. After logging in, click the **"New +"** button on the Render dashboard
2. Choose **"Web Service"**
3. Select your **backend repository** from GitHub (ZoePascua/backend)
4. Choose the **main** branch
5. Click **"Connect"**

### Step 3 — Configure Your Service

Fill in the deployment form with these settings:

| Field | Value |
|-------|-------|
| **Name** | peitel-backend (or your preferred name) |
| **Environment** | Python |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `python manage.py runserver 0.0.0.0:$PORT` |
| **Region** | Select closest to you (e.g., Singapore, US) |
| **Branch** | main |

### Step 4 — Wait for Deployment

1. Render will automatically:
   - Install all dependencies from `requirements.txt`
   - Run database migrations
   - Collect static files
   - Start your Django server

2. Once successful, you'll see a **Live URL** like:
   ```
   https://peitel-backend.onrender.com
   ```
   
3. **Copy and save this URL** — you'll need it for your frontend!

### Step 5 — Set Environment Variables on Render

1. Go to your service settings on Render dashboard
2. Navigate to **"Environment"** tab
3. Add these environment variables:

```
SECRET_KEY = [Generate a strong secret key from https://djecrety.ir/]
DEBUG = False
ALLOWED_HOSTS = peitel-backend.onrender.com,yourdomain.com
CSRF_TRUSTED_ORIGINS = https://peitel-backend.onrender.com,https://your-frontend-url.expo.dev
```

---

## PART II – FRONTEND DEPLOYMENT ON SNACK.DEV

### Step 1 — Create a Snack.dev Account

1. Visit https://snack.expo.dev
2. Sign in with your **GitHub**, **Google**, or **Expo** account

### Step 2 — Link Your Frontend Repository

1. In Snack, click on your **profile icon** → choose **"My Snacks"**
2. Click **"Import GitHub Repository"**
3. Paste the URL of your **frontend repository**
   - Example: `https://github.com/yourusername/frontend-repo`
4. Snack will load your project code directly into the editor

### Step 3 — Configure Backend API URL

1. In your frontend code, find where your **API URL** is defined
   - Look for files like: `config.js`, `api.js`, `constants.js`, or `.env`
   - Or search for fetch calls with `http://127.0.0.1:8000` or `http://localhost:8000`

2. **Replace the local URL** with your Render backend URL:
   ```javascript
   // OLD (local development)
   const API_URL = "http://127.0.0.1:8000";
   const API_URL = "http://localhost:8000";
   
   // NEW (Render production)
   const API_URL = "https://peitel-backend.onrender.com";
   ```

3. Update all API endpoints to use this new URL:
   ```javascript
   // Example for a user registration endpoint
   const response = await fetch(`${API_URL}/api/register/`, {
     method: 'POST',
     headers: {
       'Content-Type': 'application/json',
     },
     body: JSON.stringify(userData)
   });
   ```

### Step 4 — Update Backend CSRF Settings

Your backend is now configured to accept requests from:
- The Snack.dev frontend URL (automatically included in CSRF_TRUSTED_ORIGINS)
- Any frontend URL you specify

**If you deploy your frontend to a different URL**, update the environment variable on Render:

```
CSRF_TRUSTED_ORIGINS = https://peitel-backend.onrender.com,https://your-frontend-url.com
```

---

## Important Notes

### 🔒 Security

- **Never commit `.env` file** to GitHub (already in `.gitignore`)
- Generate a strong `SECRET_KEY` at https://djecrety.ir/
- Keep `DEBUG = False` in production
- Use HTTPS only for all API calls

### 🚀 Testing Your Deployment

After deployment, test your endpoints:

```bash
# Test if backend is running
curl https://peitel-backend.onrender.com/

# Test your API endpoints
curl https://peitel-backend.onrender.com/api/users/
curl -X POST https://peitel-backend.onrender.com/api/register/ \
  -H "Content-Type: application/json" \
  -d '{"username":"test","email":"test@example.com","password":"password123"}'
```

### 📝 Troubleshooting

**Backend not starting?**
- Check Render logs for error messages
- Verify all environment variables are set
- Check that `requirements.txt` has all dependencies

**Frontend can't connect to backend?**
- Verify the API_URL is correct (use your Render domain)
- Check CSRF_TRUSTED_ORIGINS in settings.py includes your frontend URL
- Check browser console for CORS errors

**CORS errors?**
- Make sure `django-cors-headers` is installed (✓ already in requirements.txt)
- Verify `CORS_ALLOW_ALL_ORIGINS = True` in settings.py

---

## Quick Reference

| Component | URL |
|-----------|-----|
| Backend (Render) | https://peitel-backend.onrender.com |
| Frontend (Snack.dev) | https://snack.expo.dev/@yourusername/project-name |
| Admin Panel | https://peitel-backend.onrender.com/admin/ |

---

**Good luck with your deployment! 🎉**
