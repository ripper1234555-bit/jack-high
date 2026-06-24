# DateLink Installation Guide

## 📦 What's Included

The `DateLink_Dating_App.zip` contains a complete Streamlit dating application ready to deploy.

```
DateLink_Dating_App.zip
├── dating_app.py              # Main application (single file!)
├── requirements.txt           # Python dependencies
├── QUICK_START.md            # Quick start guide
├── DATING_APP_README.md      # Full documentation
├── setup.sh                  # Linux/Mac setup script
├── setup.bat                 # Windows setup script
└── .gitignore_dating         # Git ignore file
```

---

## 🚀 Installation Methods

### Method 1: Local Setup (Recommended for Testing)

#### On Windows:
1. Extract `DateLink_Dating_App.zip` to a folder
2. Double-click `setup.bat`
3. Wait for installation to complete
4. The terminal will show you how to run the app

#### On Mac/Linux:
```bash
# Extract the ZIP
unzip DateLink_Dating_App.zip
cd DateLink_Dating_App

# Run setup script
chmod +x setup.sh
./setup.sh

# Run the app (follows the on-screen instructions)
streamlit run dating_app.py
```

#### Manual Setup (All Platforms):
```bash
# Extract ZIP
unzip DateLink_Dating_App.zip
cd DateLink_Dating_App

# Install Python dependencies
pip install -r requirements.txt

# Run the app
streamlit run dating_app.py

# Access at: http://localhost:8501
```

---

### Method 2: GitHub Codespace (Best for Cloud)

#### Step 1: Prepare Repository
```bash
# In your local repository
cd your-repo
unzip DateLink_Dating_App.zip
# Copy all files to your repo
git add .
git commit -m "Add DateLink dating app"
git push
```

#### Step 2: Open Codespace
1. Go to your GitHub repository
2. Click **Code** button
3. Select **Codespaces**
4. Click **Create codespace on main**
5. Wait for Codespace to initialize

#### Step 3: Run in Codespace
```bash
pip install -r requirements.txt
streamlit run dating_app.py
```

6. Streamlit will provide a public URL in the terminal
7. Click the URL to access the app from anywhere

#### Make Codespace Default (Optional):
Add `.devcontainer/devcontainer.json` to your repo:
```json
{
  "name": "DateLink Dating App",
  "image": "mcr.microsoft.com/devcontainers/python:3.11",
  "postCreateCommand": "pip install -r requirements.txt",
  "customizations": {
    "codespaces": {
      "openFiles": ["dating_app.py"]
    }
  }
}
```

---

### Method 3: Docker Deployment

Create `Dockerfile`:
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY dating_app.py .
COPY data/ data/
COPY uploads/ uploads/

EXPOSE 8501

CMD ["streamlit", "run", "dating_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

Build and run:
```bash
docker build -t datelink .
docker run -p 8501:8501 datelink
```

---

### Method 4: Heroku Deployment

Create `Procfile`:
```
web: streamlit run dating_app.py --server.port=$PORT --server.address=0.0.0.0
```

Create `setup.sh`:
```bash
#!/bin/bash
pip install -r requirements.txt
mkdir -p data uploads
```

Deploy:
```bash
git push heroku main
```

---

## ✅ System Requirements

- **Python**: 3.8 or higher
- **RAM**: Minimum 512 MB
- **Storage**: 50 MB for app + user data
- **Internet**: Optional (works offline after initial setup)

---

## 🔧 Troubleshooting

### Python Not Found
```bash
# Install Python from python.org or use:
# macOS: brew install python3
# Ubuntu: sudo apt install python3 python3-pip
# Windows: Download from python.org
```

### Port 8501 Already in Use
```bash
streamlit run dating_app.py --server.port 8502
```

### Module Not Found Errors
```bash
# Reinstall dependencies
pip uninstall -r requirements.txt -y
pip install -r requirements.txt
```

### Permission Denied (Mac/Linux)
```bash
chmod +x setup.sh
./setup.sh
```

### Slow Performance in Codespace
- Stop other processes
- Close other browser tabs
- Check internet connection
- Try a different browser

---

## 📝 First Run

After successful installation:

1. **Create Test Account**
   - Email: user1@test.com
   - Password: password123

2. **Complete Profile**
   - Add location, bio, interests
   - Upload a profile photo

3. **Create Second Account**
   - Email: user2@test.com
   - This lets you test matching

4. **Test Features**
   - Like profiles as user1
   - Like user1 back as user2
   - View your match
   - Send messages

---

## 🚀 Deployment Options

| Platform | Setup Time | Cost | Best For |
|----------|-----------|------|----------|
| Local | 2 min | Free | Development |
| GitHub Codespace | 3 min | Free (60 hrs/mo) | Testing, Demo |
| Heroku | 5 min | Free/Paid | Small Projects |
| AWS/Azure | 10 min | Paid | Production |
| Digital Ocean | 5 min | $6+/month | Production |

---

## 🔒 Security Notes

**Development Only:** This app stores passwords in plain text. For production:
- Use proper password hashing (bcrypt, argon2)
- Add HTTPS
- Use a real database (PostgreSQL, MongoDB)
- Implement JWT tokens
- Add rate limiting
- Add input validation

---

## 📞 Support

- **Streamlit Docs**: https://docs.streamlit.io
- **Python Docs**: https://docs.python.org
- **GitHub Help**: https://docs.github.com

---

## 🎉 Next Steps

After successful installation:
1. Read `QUICK_START.md` for demo instructions
2. Read `DATING_APP_README.md` for complete features
3. Customize the app colors and branding
4. Deploy to production using your preferred platform
