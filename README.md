# Team Calendar Backend - Railway Deployment

## 🚀 **Ready for Railway Deployment**

This backend is pre-configured for Railway deployment with:
- ✅ PORT environment variable support
- ✅ CORS enabled for frontend integration
- ✅ SQLite database (automatically persisted by Railway)
- ✅ All dependencies in requirements.txt

## 📋 **Deployment Steps**

### **Option 1: GitHub Deployment (Recommended)**

1. **Create GitHub Repository**:
   - Upload all files from this folder to a new GitHub repo
   - Name it something like "team-calendar-backend"

2. **Deploy to Railway**:
   - Visit https://railway.app
   - Click "New Project" → "Deploy from GitHub repo"
   - Select your repository
   - Railway automatically deploys!

3. **Get Your URL**:
   - Copy the Railway URL (e.g., `https://your-app.up.railway.app`)
   - Use this URL in your frontend configuration

### **Option 2: CLI Deployment**

```bash
# Install Railway CLI
npm install -g @railway/cli

# Login to Railway
railway login

# Initialize project
railway init

# Deploy
railway up
```

## 🔧 **Configuration**

### **Environment Variables** (Optional):
Railway automatically sets:
- `PORT` - Used by the Flask app
- Database files are automatically persisted

### **Custom Variables** (if needed):
- `SECRET_KEY` - Flask secret key (optional)
- `DEBUG` - Set to "False" for production (optional)

## 📁 **File Structure**

```
railway_backend_ready/
├── main.py              # Flask application entry point
├── requirements.txt     # Python dependencies
├── models/
│   ├── user.py         # User model
│   └── event.py        # Event model (calendar events)
├── routes/
│   ├── user.py         # User API routes
│   └── event.py        # Event API routes (main functionality)
└── database/
    └── app.db          # SQLite database (auto-created)
```

## 🎯 **API Endpoints**

Once deployed, your Railway backend provides:

- `GET /api/events` - Get all events
- `POST /api/events` - Create new event
- `PUT /api/events/{id}` - Update event
- `DELETE /api/events/{id}` - Delete event

## ✅ **Verification**

After deployment:
1. Visit your Railway URL
2. Test API: `https://your-railway-url.up.railway.app/api/events`
3. Should return `[]` (empty array) for new deployment
4. Update your frontend to use this URL

## 🔄 **Frontend Integration**

Update your frontend `Calendar.jsx`:
```javascript
const API_BASE = 'https://your-railway-url.up.railway.app/api';
```

Then rebuild and upload to GoDaddy.

## 📞 **Support**

- Railway Documentation: https://docs.railway.app
- Railway Discord: Active community support
- This backend is tested and ready to deploy!

**Deployment Time**: ~3 minutes
**Cost**: Free (Railway free tier)

