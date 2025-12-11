# QUICK START: Deployment Steps

## 🚀 Backend Deployment (Render)

### 1. Prepare for Deployment
```
✓ All files committed and pushed to GitHub
✓ requirements.txt has all dependencies
✓ settings.py configured for production
✓ render.yaml ready
```

### 2. Go to Render Dashboard
```
1. Visit https://render.com
2. Log in with your GitHub account
3. Click "New +" → "Web Service"
4. Select your backend repository
5. Choose "main" branch
6. Click "Connect"
```

### 3. Configure Service
```
Name:           peitel-backend
Environment:    Python
Build Command:  pip install -r requirements.txt
Start Command:  python manage.py runserver 0.0.0.0:$PORT
Region:         Choose closest to you
Branch:         main
```

### 4. Click "Create Web Service"
```
Wait 5-10 minutes for deployment
You'll get a URL like: https://peitel-backend.onrender.com
```

### 5. Add Environment Variables
```
Go to Settings → Environment
Add these variables:

SECRET_KEY = [from https://djecrety.ir/]
DEBUG = False
ALLOWED_HOSTS = peitel-backend.onrender.com
CSRF_TRUSTED_ORIGINS = https://peitel-backend.onrender.com
```

---

## 📱 Frontend Deployment (Snack.dev)

### 1. Create Snack.dev Account
```
Visit: https://snack.expo.dev
Sign in with: GitHub, Google, or Expo account
```

### 2. Import Frontend Repository
```
1. Click your profile icon → "My Snacks"
2. Click "Import GitHub Repository"
3. Paste your frontend repo URL
4. Wait for Snack to load
```

### 3. Update API URL
```
Find your backend URL definition:
OLD: const API_URL = "http://127.0.0.1:8000"
NEW: const API_URL = "https://peitel-backend.onrender.com"

Update ALL fetch/axios calls to use this URL
```

### 4. Test Integration
```
✓ Frontend loads in Snack.dev
✓ API calls succeed
✓ No CORS errors
✓ Data flows between frontend and backend
```

---

## 🔗 Important URLs After Deployment

| Purpose | URL |
|---------|-----|
| Backend API | `https://peitel-backend.onrender.com` |
| Django Admin | `https://peitel-backend.onrender.com/admin/` |
| Frontend (Snack) | `https://snack.expo.dev/@yourusername/projectname` |
| Render Dashboard | `https://dashboard.render.com` |
| Generate SECRET_KEY | `https://djecrety.ir/` |

---

## ⚠️ Common Issues & Fixes

### "Service failed to start"
- Check Render logs for errors
- Verify requirements.txt syntax
- Ensure all imports are available

### "CORS error: blocked by CORS policy"
- Update CSRF_TRUSTED_ORIGINS with your frontend URL
- Verify CORS_ALLOW_ALL_ORIGINS = True in settings.py
- Check django-cors-headers is installed

### "API returns 403 Forbidden"
- Make sure CSRF_TRUSTED_ORIGINS includes your frontend domain
- For development: add `http://localhost:3000`

### "Backend works locally but not on Render"
- Check environment variables are set
- Verify SECRET_KEY is strong
- Check DEBUG = False in production

---

## 📋 Files Created

- **requirements.txt** - All dependencies with versions
- **settings.py** - Production configuration
- **build.sh** - Build script for Render
- **render.yaml** - Render deployment config
- **.env.example** - Template for environment variables
- **.gitignore** - Protect sensitive files
- **DEPLOYMENT_GUIDE.md** - Detailed instructions
- **DEPLOYMENT_CHECKLIST.md** - Step-by-step checklist

---

**Ready to deploy? Start with the Render backend first! 🎉**
