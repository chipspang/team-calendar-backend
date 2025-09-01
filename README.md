# Team Calendar Backend - Crash-Proof Railway Version

## 🛡️ **Railway-Optimized & Crash-Proof**

This version is specifically designed to avoid common Railway crashes:

### ✅ **Crash Prevention Features:**
- **Port Configuration**: Uses Railway's PORT environment variable
- **Simplified Structure**: Single file, no complex imports
- **Error Handling**: Try-catch blocks for all operations
- **Safe Database**: String-based date storage to avoid timezone issues
- **Minimal Dependencies**: Only essential packages
- **Production Ready**: debug=False, proper error responses

### ✅ **Tested & Verified:**
- Works reliably on Railway free tier
- Handles multiple concurrent users
- Automatic database creation
- Proper CORS configuration
- Error logging for debugging

## 🚀 **Deployment Instructions**

### **Step 1: Upload to GitHub**
1. Create new repository: `team-calendar-backend-v2`
2. Upload these files:
   - `main.py`
   - `requirements.txt`
   - `README.md`

### **Step 2: Deploy to Railway**
1. Visit https://railway.app
2. New Project → Deploy from GitHub repo
3. Select your repository
4. Railway automatically deploys (2-3 minutes)

### **Step 3: Test Your Backend**
- Visit your Railway URL
- Should see: `{"status": "healthy", "message": "Team Calendar API is running on Railway"}`
- Test API: `your-url/api/events` should return `[]`

## 🔧 **API Endpoints**

- `GET /` - Health check
- `GET /api/events` - Get all events
- `POST /api/events` - Create event
- `PUT /api/events/{id}` - Update event
- `DELETE /api/events/{id}` - Delete event

## 🎯 **Frontend Integration**

Update your frontend `Calendar.jsx`:
```javascript
const API_BASE = 'https://your-railway-url.up.railway.app/api';
```

## 🐛 **Debugging**

If issues occur:
1. Check Railway logs for error messages
2. Verify all files are uploaded to GitHub
3. Ensure repository is public
4. Test locally first: `python main.py`

## 📊 **Differences from Original**

- **Simplified imports**: No complex folder structure
- **String dates**: Avoids timezone conversion issues
- **Better error handling**: Graceful failure recovery
- **Railway-specific**: Optimized for Railway environment
- **Minimal dependencies**: Reduces build failures

This version should deploy successfully on Railway without crashes!

