# DateLink - Quick Start Guide

## 🚀 Getting Started in 3 Steps

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Run the App
```bash
streamlit run dating_app.py
```

### Step 3: Open in Browser
Navigate to: **http://localhost:8501**

---

## 📝 Test Credentials

Since this is a demo app, create test accounts:

**Test User 1:**
- Name: Alice
- Email: alice@test.com
- Password: password123
- Age: 25

**Test User 2:**
- Name: Bob
- Email: bob@test.com
- Password: password123
- Age: 27

---

## 🎯 Quick Demo Flow

1. **Sign Up** with test account details
2. **Complete Profile** - Add bio, interests, location, and upload a photo
3. **Switch Users** - Create another test account with different credentials
4. **Like Profiles** - Use the Discover tab to like other users
5. **View Matches** - Check the Matches tab after both users like each other
6. **Send Messages** - Chat with your match in the Messages tab
7. **Search** - Find users by name, age, or location

---

## 🛠️ GitHub Codespace Setup

1. **Push to GitHub**
```bash
git add .
git commit -m "Add DateLink dating app"
git push origin main
```

2. **Open in Codespace**
   - Go to your GitHub repo
   - Click `Code` → `Codespaces` → `Create codespace on main`

3. **Inside Codespace, run:**
```bash
pip install -r requirements.txt
streamlit run dating_app.py
```

4. **Access the app** - Streamlit will provide a public URL

---

## 📱 Features Overview

| Feature | Description |
|---------|------------|
| **Discover** | Swipe through profiles one by one |
| **Likes** | See who has liked your profile |
| **Matches** | View mutual connections |
| **Messages** | Chat with your matches |
| **Profile** | Manage your profile and photos |
| **Search** | Find users by criteria |

---

## 💾 Data Storage

All data is stored locally in the `data/` folder:
- `users.json` - User accounts
- `profiles.json` - Profile information
- `matches.json` - Match history  
- `messages.json` - Messages between users
- `uploads/` - Profile photos

**Note**: Data persists between app restarts but will be lost if you delete these folders.

---

## ⚠️ Troubleshooting

**Port 8501 already in use?**
```bash
streamlit run dating_app.py --server.port 8502
```

**Changes not showing?**
- Restart the app with Ctrl+C and run again
- Clear Streamlit cache: `streamlit cache clear`

**Photos not uploading?**
- Ensure `uploads/` folder exists
- Check file permissions
- Try a different image format (jpg, jpeg, png)

---

## 📚 Full Documentation

See `DATING_APP_README.md` for complete documentation.
