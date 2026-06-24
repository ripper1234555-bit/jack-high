import streamlit as st
import json
import os
from datetime import datetime
from pathlib import Path
import uuid

# Page config
st.set_page_config(page_title="DateLink", layout="wide", initial_sidebar_state="expanded")

# Initialize session state
if "user" not in st.session_state:
    st.session_state.user = None
if "page" not in st.session_state:
    st.session_state.page = "login"

# Data file paths
DATA_DIR = "data"
USERS_FILE = f"{DATA_DIR}/users.json"
PROFILES_FILE = f"{DATA_DIR}/profiles.json"
MATCHES_FILE = f"{DATA_DIR}/matches.json"
MESSAGES_FILE = f"{DATA_DIR}/messages.json"
UPLOADS_DIR = "uploads"

# Create necessary directories
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(UPLOADS_DIR, exist_ok=True)

# Load/Save functions
def load_json(filepath):
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            return json.load(f)
    return {}

def save_json(filepath, data):
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)

# Data loading functions
def load_users():
    return load_json(USERS_FILE)

def save_users(users):
    save_json(USERS_FILE, users)

def load_profiles():
    return load_json(PROFILES_FILE)

def save_profiles(profiles):
    save_json(PROFILES_FILE, profiles)

def load_matches():
    return load_json(MATCHES_FILE)

def save_matches(matches):
    save_json(MATCHES_FILE, matches)

def load_messages():
    return load_json(MESSAGES_FILE)

def save_messages(messages):
    save_json(MESSAGES_FILE, messages)

# Authentication functions
def handle_login(email, password):
    users = load_users()
    for user_id, user in users.items():
        if user['email'] == email and user['password'] == password:
            return {'id': user_id, 'name': user['name'], 'email': user['email'], 'age': user['age']}
    return None

def handle_signup(name, email, password, age, gender):
    users = load_users()
    
    for user in users.values():
        if user['email'] == email:
            return False, "Email already registered"
    
    user_id = str(uuid.uuid4())
    users[user_id] = {
        'id': user_id,
        'name': name,
        'email': email,
        'password': password,
        'age': age,
        'gender': gender
    }
    save_users(users)
    return True, "Account created! Please log in"

# Profile functions
def create_profile(user_id, location, bio, interests, photo_path):
    profiles = load_profiles()
    profiles[user_id] = {
        'location': location,
        'bio': bio,
        'interests': interests,
        'photo_path': photo_path
    }
    save_profiles(profiles)

def get_user_profile(user_id):
    profiles = load_profiles()
    return profiles.get(user_id)

def edit_profile(user_id, location, bio, interests, photo_path):
    create_profile(user_id, location, bio, interests, photo_path)

# Matching functions
def like_user(liker_id, liked_id):
    matches = load_matches()
    key = f"{liker_id}_{liked_id}"
    matches[key] = {'liker': liker_id, 'liked': liked_id, 'timestamp': str(datetime.now())}
    save_matches(matches)

def get_matches(user_id):
    matches = load_matches()
    users = load_users()
    profiles = load_profiles()
    
    match_ids = set()
    for key, match in matches.items():
        if match['liker'] == user_id and match['liked'] in matches:
            reverse_key = f"{match['liked']}_{user_id}"
            if reverse_key in matches and matches[reverse_key]['liker'] == match['liked']:
                match_ids.add(match['liked'])
        elif match['liked'] == user_id and match['liker'] in matches:
            reverse_key = f"{user_id}_{match['liker']}"
            if reverse_key in matches and matches[reverse_key]['liker'] == user_id:
                match_ids.add(match['liker'])
    
    result = []
    for match_id in match_ids:
        if match_id in users:
            user = users[match_id]
            profile = profiles.get(match_id, {})
            result.append({
                'id': match_id,
                'name': user['name'],
                'age': user['age'],
                **profile
            })
    return result

def get_likes(user_id):
    matches = load_matches()
    users = load_users()
    profiles = load_profiles()
    
    likers = []
    for key, match in matches.items():
        if match['liked'] == user_id:
            reverse_key = f"{user_id}_{match['liker']}"
            if reverse_key not in matches:
                if match['liker'] in users:
                    user = users[match['liker']]
                    profile = profiles.get(match['liker'], {})
                    likers.append({
                        'id': match['liker'],
                        'name': user['name'],
                        'age': user['age'],
                        **profile
                    })
    
    return likers

# Messaging functions
def send_message(sender_id, receiver_id, message):
    messages = load_messages()
    msg_id = str(uuid.uuid4())
    messages[msg_id] = {
        'sender_id': sender_id,
        'receiver_id': receiver_id,
        'message': message,
        'timestamp': str(datetime.now())
    }
    save_messages(messages)

def get_conversation(user_id, other_user_id):
    messages = load_messages()
    conversation = []
    
    for msg in messages.values():
        if (msg['sender_id'] == user_id and msg['receiver_id'] == other_user_id) or \
           (msg['sender_id'] == other_user_id and msg['receiver_id'] == user_id):
            conversation.append(msg)
    
    return sorted(conversation, key=lambda x: x['timestamp'])

def get_all_conversations(user_id):
    messages = load_messages()
    users = load_users()
    conversations = {}
    
    for msg in messages.values():
        if msg['sender_id'] == user_id:
            other_id = msg['receiver_id']
        elif msg['receiver_id'] == user_id:
            other_id = msg['sender_id']
        else:
            continue
        
        if other_id not in conversations and other_id in users:
            conversations[other_id] = users[other_id]['name']
    
    result = []
    for other_id, name in conversations.items():
        result.append({'other_user_id': other_id, 'other_user_name': name})
    
    return result

# Search functions
def search_users(name_query, age_range, location_query):
    users = load_users()
    profiles = load_profiles()
    results = []
    
    for user_id, user in users.items():
        profile = profiles.get(user_id, {})
        
        name_match = not name_query or name_query.lower() in user['name'].lower()
        age_match = age_range[0] <= user['age'] <= age_range[1]
        location_match = not location_query or location_query.lower() in profile.get('location', '').lower()
        
        if name_match and age_match and location_match:
            results.append({
                'id': user_id,
                'name': user['name'],
                'age': user['age'],
                **profile
            })
    
    return results

# Custom CSS
st.markdown("""
    <style>
    .main-header {
        text-align: center;
        color: #FF6B9D;
        font-size: 2.5em;
        font-weight: bold;
        margin-bottom: 1em;
    }
    .profile-card {
        border: 2px solid #FF6B9D;
        border-radius: 10px;
        padding: 20px;
        margin: 10px 0;
        background: linear-gradient(135deg, #fff 0%, #f5f5f5 100%);
    }
    .match-card {
        border: 1px solid #FFB3D9;
        border-radius: 8px;
        padding: 15px;
        margin: 10px 0;
    }
    </style>
""", unsafe_allow_html=True)

# Page functions
def discover_page():
    st.header("Discover Profiles")
    
    users = load_users()
    profiles = load_profiles()
    current_user_id = st.session_state.user['id']
    
    available_users = [u for u in users.values() if u['id'] != current_user_id]
    
    if not available_users:
        st.info("No users available at this time")
        return
    
    if "current_user_index" not in st.session_state:
        st.session_state.current_user_index = 0
    
    idx = st.session_state.current_user_index
    if idx >= len(available_users):
        st.info("You've viewed all available profiles! Come back later for more.")
        st.session_state.current_user_index = 0
        return
    
    user = available_users[idx]
    profile = profiles.get(user['id'], {})
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown('<div class="profile-card">', unsafe_allow_html=True)
        
        if profile.get('photo_path') and os.path.exists(profile['photo_path']):
            st.image(profile['photo_path'], use_column_width=True, caption=f"{user['name']}, {user['age']}")
        else:
            st.write(f"**{user['name']}, {user['age']}** from {profile.get('location', 'Unknown')}")
        
        st.write(f"**Bio:** {profile.get('bio', 'No bio yet')}")
        st.write(f"**Interests:** {profile.get('interests', 'Not specified')}")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.write("")
        col_pass, col_like = st.columns(2)
        
        with col_pass:
            if st.button("Pass", key="pass_btn"):
                st.session_state.current_user_index += 1
                st.rerun()
        
        with col_like:
            if st.button("Like", key="like_btn"):
                like_user(current_user_id, user['id'])
                st.success("You liked this profile!")
                st.session_state.current_user_index += 1
                st.rerun()

def matches_page():
    st.header("Your Matches")
    
    current_user_id = st.session_state.user['id']
    matches = get_matches(current_user_id)
    
    if not matches:
        st.info("No matches yet. Keep swiping!")
        return
    
    for match in matches:
        col1, col2 = st.columns([3, 1])
        
        with col1:
            st.markdown('<div class="match-card">', unsafe_allow_html=True)
            
            if match.get('photo_path') and os.path.exists(match['photo_path']):
                st.image(match['photo_path'], width=150, caption=f"{match['name']}, {match['age']}")
            else:
                st.write(f"**{match['name']}, {match['age']}**")
            
            st.write(f"📍 {match.get('location', 'Unknown')}")
            st.write(f"{match.get('bio', 'No bio')}")
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col2:
            if st.button("Message", key=f"msg_{match['id']}"):
                st.session_state.chat_user_id = match['id']
                st.rerun()

def likes_page():
    st.header("People Who Liked You")
    
    current_user_id = st.session_state.user['id']
    likers = get_likes(current_user_id)
    
    if not likers:
        st.info("No likes yet. Check back soon!")
        return
    
    for liker in likers:
        col1, col2 = st.columns([3, 1])
        
        with col1:
            st.markdown('<div class="match-card">', unsafe_allow_html=True)
            
            if liker.get('photo_path') and os.path.exists(liker['photo_path']):
                st.image(liker['photo_path'], width=150, caption=f"{liker['name']}, {liker['age']}")
            else:
                st.write(f"**{liker['name']}, {liker['age']}**")
            
            st.write(f"{liker.get('bio', 'No bio')}")
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col2:
            if st.button("Like Back", key=f"like_back_{liker['id']}"):
                like_user(current_user_id, liker['id'])
                st.success("It's a match!")
                st.rerun()

def messages_page():
    st.header("Messages")
    
    current_user_id = st.session_state.user['id']
    conversations = get_all_conversations(current_user_id)
    
    if not conversations:
        st.info("No conversations yet")
        return
    
    conv_options = [f"{c['other_user_name']}" for c in conversations]
    selected = st.selectbox("Select a conversation:", conv_options)
    
    if selected:
        selected_idx = conv_options.index(selected)
        other_user_id = conversations[selected_idx]['other_user_id']
        
        messages = get_conversation(current_user_id, other_user_id)
        
        st.subheader(f"Chat with {conversations[selected_idx]['other_user_name']}")
        
        for msg in messages:
            if msg['sender_id'] == current_user_id:
                st.write(f"**You:** {msg['message']}")
            else:
                st.write(f"**{conversations[selected_idx]['other_user_name']}:** {msg['message']}")
        
        new_msg = st.text_input("Type your message:")
        if st.button("Send"):
            if new_msg:
                send_message(current_user_id, other_user_id, new_msg)
                st.success("Message sent!")
                st.rerun()

def profile_page():
    st.header("My Profile")
    
    current_user_id = st.session_state.user['id']
    profile = get_user_profile(current_user_id)
    
    if not profile:
        st.info("Create your profile to get started!")
        
        with st.form("create_profile"):
            st.subheader("Complete Your Profile")
            
            location = st.text_input("Location")
            bio = st.text_area("Bio (tell us about yourself)")
            interests = st.text_input("Interests (comma separated)")
            photo = st.file_uploader("Upload Profile Photo", type=["jpg", "jpeg", "png"])
            
            if st.form_submit_button("Create Profile"):
                photo_path = None
                if photo:
                    photo_path = f"{UPLOADS_DIR}/{current_user_id}_{photo.name}"
                    with open(photo_path, "wb") as f:
                        f.write(photo.getbuffer())
                
                create_profile(current_user_id, location, bio, interests, photo_path)
                st.success("Profile created!")
                st.rerun()
    else:
        col1, col2 = st.columns([1, 2])
        
        with col1:
            if profile.get('photo_path') and os.path.exists(profile['photo_path']):
                st.image(profile['photo_path'], use_column_width=True)
            else:
                st.write("No photo yet")
        
        with col2:
            st.write(f"**Name:** {st.session_state.user['name']}")
            st.write(f"**Age:** {st.session_state.user['age']}")
            st.write(f"**Location:** {profile.get('location', 'Not set')}")
            st.write(f"**Bio:** {profile.get('bio', 'Not set')}")
            st.write(f"**Interests:** {profile.get('interests', 'Not set')}")
        
        if st.button("Edit Profile"):
            st.session_state.editing_profile = True
        
        if st.session_state.get("editing_profile"):
            with st.form("edit_profile"):
                location = st.text_input("Location", value=profile.get('location', ''))
                bio = st.text_area("Bio", value=profile.get('bio', ''))
                interests = st.text_input("Interests", value=profile.get('interests', ''))
                photo = st.file_uploader("Update Photo", type=["jpg", "jpeg", "png"])
                
                if st.form_submit_button("Save Changes"):
                    photo_path = profile.get('photo_path')
                    if photo:
                        photo_path = f"{UPLOADS_DIR}/{current_user_id}_{photo.name}"
                        with open(photo_path, "wb") as f:
                            f.write(photo.getbuffer())
                    
                    edit_profile(current_user_id, location, bio, interests, photo_path)
                    st.success("Profile updated!")
                    st.session_state.editing_profile = False
                    st.rerun()

def search_page():
    st.header("Search Users")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        name = st.text_input("Search by name")
    
    with col2:
        age_range = st.slider("Age range", 18, 100, (18, 100))
    
    with col3:
        location = st.text_input("Location")
    
    if st.button("Search"):
        results = search_users(name, age_range, location)
        current_user_id = st.session_state.user['id']
        results = [u for u in results if u['id'] != current_user_id]
        
        if results:
            st.subheader(f"Found {len(results)} users")
            for user in results:
                col1, col2 = st.columns([3, 1])
                
                with col1:
                    st.markdown('<div class="match-card">', unsafe_allow_html=True)
                    
                    if user.get('photo_path') and os.path.exists(user['photo_path']):
                        st.image(user['photo_path'], width=150, caption=f"{user['name']}, {user['age']}")
                    else:
                        st.write(f"**{user['name']}, {user['age']}**")
                    
                    st.write(f"📍 {user.get('location', 'Unknown')}")
                    st.markdown('</div>', unsafe_allow_html=True)
                
                with col2:
                    if st.button("Like", key=f"search_like_{user['id']}"):
                        like_user(current_user_id, user['id'])
                        st.success("Liked!")
                        st.rerun()
        else:
            st.info("No users found matching your criteria")

# Main function
def main():
    if st.session_state.user:
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.markdown('<div class="main-header">DateLink ❤️</div>', unsafe_allow_html=True)
        
        with st.sidebar:
            st.title("Navigation")
            page = st.radio("Go to:", 
                ["Discover", "Matches", "Likes", "Messages", "Profile", "Search", "Logout"],
                key="nav")
            
            st.session_state.page = page
        
        if page == "Discover":
            discover_page()
        elif page == "Matches":
            matches_page()
        elif page == "Likes":
            likes_page()
        elif page == "Messages":
            messages_page()
        elif page == "Profile":
            profile_page()
        elif page == "Search":
            search_page()
        elif page == "Logout":
            st.session_state.user = None
            st.session_state.page = "login"
            st.rerun()
    else:
        st.markdown('<div class="main-header">DateLink ❤️</div>', unsafe_allow_html=True)
        st.markdown("### Find your perfect match!")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Login")
            email = st.text_input("Email", key="login_email")
            password = st.text_input("Password", type="password", key="login_password")
            
            if st.button("Sign In", key="login_btn"):
                user = handle_login(email, password)
                if user:
                    st.session_state.user = user
                    st.success(f"Welcome back, {user['name']}!")
                    st.rerun()
                else:
                    st.error("Invalid email or password")
        
        with col2:
            st.subheader("Create Account")
            name = st.text_input("Full Name", key="signup_name")
            email = st.text_input("Email", key="signup_email")
            password = st.text_input("Password", type="password", key="signup_password")
            age = st.number_input("Age", min_value=18, max_value=100, key="signup_age")
            gender = st.selectbox("Gender", ["Male", "Female", "Other"], key="signup_gender")
            
            if st.button("Sign Up", key="signup_btn"):
                if name and email and password and age:
                    success, message = handle_signup(name, email, password, age, gender)
                    if success:
                        st.success(message)
                        st.info("Now please log in with your credentials")
                    else:
                        st.error(message)
                else:
                    st.warning("Please fill in all fields")

if __name__ == "__main__":
    main()
