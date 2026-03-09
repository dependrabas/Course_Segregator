# Render Deployment Guide - STEP BY STEP

## The Problem You Encountered

Your error was: **"Publish directory build does not exist!"**

This happens when you select the **wrong service type** in Render. You likely selected "Static Site" instead of "Web Service".

## ✅ CORRECT Way to Deploy on Render

### Step 1: Go to Render Dashboard
- Visit https://render.com
- Log in with your GitHub account
- Click "Dashboard" (top right)

### Step 2: Create New Web Service
1. Click **"New +"** button (top left)
2. Select **"Web Service"** (NOT "Static Site")
3. Authorize Render to access GitHub
4. Search for and select: **`Course_Segregator`**
5. Click "Connect"

### Step 3: Configure Build Settings
Fill in the form with these EXACT values:

| Field | Value |
|-------|-------|
| **Name** | `clcs-programme-separator` |
| **Environment** | `Python 3` |
| **Region** | Select closest to you |
| **Branch** | `main` |
| **Build Command** | `pip install -r requirements.txt && mkdir -p uploads output` |
| **Start Command** | `gunicorn app:app` |
| **Plan** | Free (or Starter if you need better performance) |

⚠️ **IMPORTANT**: 
- DO NOT use "Publish Directory" option
- DO NOT select "Static Site"
- This MUST be a "Web Service"

### Step 4: Environment Variables (Optional)
1. Scroll down to "Environment"
2. Add these if needed:
   - Key: `PYTHON_VERSION` → Value: `3.14.3`
   - Key: `FLASK_ENV` → Value: `production`

### Step 5: Deploy
1. Click "Create Web Service" button
2. Wait for build (usually 2-3 minutes)
3. You'll see "Live" status when complete
4. Your app will be available at: `https://clcs-programme-separator.onrender.com`

## ✅ Verify Deployment Success

1. Click on your service in Render dashboard
2. Check "Events" tab for deployment status
3. Click "Logs" to see console output
4. Visit your app URL to test

## 🐛 If It Still Fails

Check these in order:

1. **Wrong Service Type?**
   - Delete the failed deployment
   - Start over, selecting "Web Service"

2. **Check Build Log**
   - Go to Events tab
   - Look for error messages
   - Common issue: Missing dependencies in requirements.txt

3. **Check Runtime Log**
   - Go to Logs tab
   - Look for Flask startup messages
   - Should see: "Running on http://0.0.0.0:10000"

4. **App Not Loading?**
   - Wait 30-60 seconds after "Live" status
   - Clear browser cache (Ctrl+Shift+Delete)
   - Try incognito/private mode

## 📋 Checklist Before Deploying

- [ ] All files pushed to GitHub (`git push origin main`)
- [ ] `Procfile` exists with: `web: gunicorn app:app`
- [ ] `requirements.txt` has: pandas, Flask, gunicorn
- [ ] `app.py` runs on `0.0.0.0` (not 127.0.0.1)
- [ ] `templates/` folder exists with HTML files
- [ ] `static/` folder exists with CSS/JS files
- [ ] `processor.py` is in root directory

## 🎉 Success Indicators

When deployed correctly, you'll see:

```
✓ Build successful
✓ Service live
✓ Python 3.14.3 running
✓ Gunicorn server active
✓ Web app accessible at: https://your-app.onrender.com
```

---

**Still having issues?** 
1. Take a screenshot of your Render dashboard
2. Check the Logs tab for error details
3. Verify all files are in GitHub with `git push`
