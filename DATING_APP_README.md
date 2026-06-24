# DateLink - Streamlit Dating App

A modern dating application built with Streamlit for discovering matches, messaging, and connecting with other users.

## Features

- **User Authentication**: Sign up and login with email/password
- **Profile Management**: Create and edit detailed profiles with photos
- **Discover**: Swipe through profiles and like users you're interested in
- **Matching System**: View mutual matches with other users
- **Messaging**: Real-time messaging with matched users
- **Search & Filter**: Find users by name, age, and location
- **Likes**: See who has liked your profile

## Installation & Setup

### 1. Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### 2. Installation

#### Option A: Local Setup
```bash
# Clone or download the project
cd dating_app

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run dating_app.py
```

#### Option B: GitHub Codespace
1. Upload this folder to your GitHub repository
2. Open the repository in a GitHub Codespace
3. Run the following commands:
```bash
pip install -r requirements.txt
streamlit run dating_app.py
```
4. Click the Streamlit URL that appears in the terminal (usually http://localhost:8501)

## Demo Accounts

The app comes with built-in demo functionality. You can:
1. Create a new account by entering details in the "Create Account" section
2. Build a profile with photos and bio
3. Start discovering other users

## File Structure

```
dating_app.py          # Main application file
requirements.txt       # Python dependencies
data/                  # Storage for user data (auto-created)
  ├── users.json       # User accounts
  ├── profiles.json    # User profiles
  ├── matches.json     # Match history
  └── messages.json    # Messages
uploads/               # User uploaded photos (auto-created)
```

## How to Use

### 1. Create an Account
- Click "Create Account"
- Enter your name, email, password, age, and gender
- Click "Sign Up"

### 2. Complete Your Profile
- Login with your credentials
- Go to "Profile" page
- Add your location, bio, interests, and upload a photo

### 3. Discover & Like Users
- Navigate to "Discover" page
- View profiles one at a time
- Click "Like" to express interest or "Pass" to skip

### 4. Check Your Matches
- Go to "Matches" to see mutual connections
- Click "Message" to start chatting

### 5. Send Messages
- Go to "Messages"
- Select a match from the list
- Type and send messages

### 6. Find Specific Users
- Use "Search" to filter by name, age, and location

## Technologies Used

- **Streamlit**: Web framework for building the UI
- **Python**: Backend logic
- **JSON**: Data storage
- **Pillow**: Image handling

## Data Storage

Data is stored locally in JSON files:
- User account info (including passwords in demo mode)
- Profile information
- Matches between users
- Messages

**Note**: This is a prototype app. In production, use proper databases and hash passwords!

## Customization

### Change App Colors
Edit the CSS section in `dating_app.py`:
```python
.main-header {
    color: #FF6B9D;  # Change this color
}
```

### Modify Features
- Add more profile fields in `create_profile()` function
- Customize the discovery algorithm in `discover_page()`
- Add premium features or subscriptions as needed

## Troubleshooting

### Port Already in Use
If port 8501 is already in use:
```bash
streamlit run dating_app.py --server.port 8502
```

### File Upload Issues
- Ensure the `uploads/` directory exists and is writable
- Check file permissions on the system

### Data Loss
- If you delete the `data/` folder, all users and matches will be reset
- Consider backing up JSON files before testing

## Future Enhancements

- Real-time notifications for matches and messages
- User verification system
- Photo gallery support
- Video profiles
- Advanced filtering and recommendations
- Subscription tiers
- Admin dashboard
- Analytics

## License

This project is open source and available for personal use and modification.

## Support

For issues or questions, please check the Streamlit documentation: https://docs.streamlit.io
