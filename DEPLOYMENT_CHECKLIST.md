# Deployment Checklist

## Pre-Deployment Checklist ✓

### Backend (Django)
- [x] All dependencies added to `requirements.txt`
- [x] `settings.py` configured for production
- [x] CSRF settings configured
- [x] CORS headers configured
- [x] Static files configuration set up
- [x] Environment variables configured
- [x] `.env.example` created with template
- [x] `.gitignore` configured to protect sensitive files
- [x] Build script (`build.sh`) created
- [x] Render configuration (`render.yaml`) created

### Before Going Live
- [ ] Generate a strong SECRET_KEY from https://djecrety.ir/
- [ ] Create a Render account at https://render.com
- [ ] Connect your GitHub repository to Render
- [ ] Set environment variables on Render dashboard:
  - [ ] SECRET_KEY
  - [ ] DEBUG = False
  - [ ] ALLOWED_HOSTS
  - [ ] CSRF_TRUSTED_ORIGINS

## Deployment Steps

### Step 1: Backend Deployment on Render
- [ ] Log in to https://render.com
- [ ] Click "New +" → "Web Service"
- [ ] Select your backend repository
- [ ] Configure with these settings:
  - [ ] Name: peitel-backend
  - [ ] Environment: Python
  - [ ] Build Command: `pip install -r requirements.txt`
  - [ ] Start Command: `python manage.py runserver 0.0.0.0:$PORT`
  - [ ] Region: Closest to you
  - [ ] Branch: main
- [ ] Click "Create Web Service"
- [ ] Wait for deployment (5-10 minutes)
- [ ] Copy your Live URL: `https://peitel-backend.onrender.com`

### Step 2: Update Environment Variables on Render
- [ ] Go to Settings → Environment
- [ ] Add SECRET_KEY environment variable
- [ ] Add ALLOWED_HOSTS environment variable
- [ ] Add CSRF_TRUSTED_ORIGINS environment variable
- [ ] Redeploy service if needed

### Step 3: Test Backend
- [ ] Visit `https://peitel-backend.onrender.com/` in browser
- [ ] Check if API endpoints are accessible
- [ ] Test with curl or Postman

### Step 4: Frontend Deployment on Snack.dev
- [ ] Create account at https://snack.expo.dev
- [ ] Click "Import GitHub Repository"
- [ ] Paste your frontend repository URL
- [ ] Wait for Snack to load your project

### Step 5: Configure Frontend API URL
- [ ] Find API configuration in your frontend code
- [ ] Replace local URL with: `https://peitel-backend.onrender.com`
- [ ] Update all fetch/axios calls to use the new URL
- [ ] Test API calls from the frontend

### Step 6: Test Integration
- [ ] Frontend can fetch from backend
- [ ] POST requests work without CORS errors
- [ ] User registration/login works
- [ ] All API endpoints respond correctly

## Important Environment Variables

### Render Dashboard Environment Variables
```
SECRET_KEY=your-generated-secret-key
DEBUG=False
ALLOWED_HOSTS=peitel-backend.onrender.com
CSRF_TRUSTED_ORIGINS=https://peitel-backend.onrender.com,https://your-frontend-url.com
```

## Useful Links

- Render Dashboard: https://dashboard.render.com
- Snack.dev: https://snack.expo.dev
- Generate SECRET_KEY: https://djecrety.ir/
- Django Deployment Checklist: https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

## Troubleshooting

### Backend won't start
- Check Render logs (Dashboard → Logs tab)
- Verify requirements.txt has all dependencies
- Check for Python syntax errors

### CORS errors
- Verify ALLOWED_HOSTS is configured
- Check CSRF_TRUSTED_ORIGINS includes your frontend URL
- Ensure django-cors-headers is installed

### Frontend can't connect to backend
- Verify API_URL points to your Render URL
- Check browser console for detailed error messages
- Test endpoint with curl first

---

**Date Started:** _______________
**Backend Deployed:** _______________
**Frontend Deployed:** _______________
**Deployment Complete:** _______________
