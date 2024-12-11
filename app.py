from flask import Flask, render_template, redirect, url_for, request, flash, jsonify
from flask import request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
from datetime import datetime
from pymongo import MongoClient
import redis
import json
import jwt
import pyttsx3
import speech_recognition as sr
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import os
from dotenv import load_dotenv
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
from datetime import timezone
from flask_babel import Babel, refresh

# Load environment variables from the .env file
load_dotenv()

# Initialize Sentry with DSN from environment variables
sentry_sdk.init(
    dsn=os.getenv('SENTRY_DSN'),  # Get the DSN from the .env file
    integrations=[FlaskIntegration()],
    traces_sample_rate=1.0
)

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'fallback_secret_key_if_env_var_fails')  # Use a real secret key here, preferably from environment variable


# Configure supported languages and default locale
babel = Babel(app)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_SUPPORTED_LOCALES'] = ['en', 'hi', 'te']


# MongoDB configuration using environment variables
mongo_uri = os.getenv('MONGODB_URI', 'mongodb://localhost:27017/')  # Get the MongoDB URI
client = MongoClient(mongo_uri)
db = client["medisearch"]  # Your database
users_collection = db.users  # Users collection
medicines_collection = db.medicines  # Medicines collection
search_history_collection = db.search_history  # Search history collection
chat_history_collection = db.chat_history  # Chat history collection
# Ensure all users have a 'full_name' field
users_collection.update_many(
    {"full_name": {"$exists": False}},
    {"$set": {"full_name": "Anonymous User"}}
)

# Assume you have a function to determine the user's preferred language
def get_user_locale():
    # Just as an example, returning English
    return 'en'

@app.before_request
def before_request():
    # Manually set the locale for each request
    user_locale = get_user_locale()
    request.babel_locale = user_locale
    refresh()



# Ensure an index is created on the 'name' field of medicines for faster search
medicines_collection.create_index([("name", 1)])

# Redis configuration
cache = redis.StrictRedis(host='localhost', port=6379, db=0)

# JWT configuration
SECRET_KEY = "your_secret_key"  # Replace with your secret key

# Helper function to get cached medicine data
def get_cached_medicine(query):
    cached_data = cache.get(query)
    if cached_data:
        return json.loads(cached_data)  # Return cached result if available
    return None

# Helper function to cache medicine data
def cache_medicine(query, data):
    cache.set(query, json.dumps(data))  # Cache the result for future queries

# Function to recommend medicines based on the user's search history
def recommend_medicines(user_id, current_medicine_name):
    user_search_history = search_history_collection.find_one({"user_id": ObjectId(user_id)})
    
    if not user_search_history or 'medicines' not in user_search_history:
        return []
    
    history = user_search_history['medicines']
    
    # Append current medicine to history
    history.append(current_medicine_name)
    
    # Calculate similarity using TF-IDF and cosine similarity
    vectorizer = TfidfVectorizer().fit_transform(history)
    vectors = vectorizer.toarray()
    
    # Calculate cosine similarity
    cosine_sim = cosine_similarity(vectors)
    
    # Find the most similar medicines
    similar_indices = cosine_sim[-1].argsort()[:-2:-1]
    similar_medicines = [history[i] for i in similar_indices if i != len(history) - 1]
    
    return similar_medicines

# Initialize the login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# User class for login management
class User(UserMixin):
    def __init__(self, user_id, username, password, role, full_name):
        self.id = user_id
        self.username = username
        self.password = password
        self.role = role
        self.full_name = full_name

    @property
    def initials(self):
        # Generate initials from full name
        return ''.join([name[0].upper() for name in self.full_name.split()[:2]])

    @property
    def display_name(self):
        # Extract the portion before the "@" symbol
        return self.username.split('@')[0]



# Load user by ID
@login_manager.user_loader
def load_user(user_id):
    try:
        if ObjectId.is_valid(user_id):
            user = users_collection.find_one({"_id": ObjectId(user_id)})
            if user:
                # Ensure 'full_name' exists in the user document, or provide a default value
                full_name = user.get('full_name', 'Unknown User')
                return User(
                    user_id=str(user['_id']),
                    username=user['username'],
                    password=user['password'],
                    role=user['role'],
                    full_name=full_name
                )
    except Exception as e:
        print(f"Error loading user: {e}")
    return None

# JWT token generation
def create_token(user_id):
    payload = {
        'exp': datetime.datetime.now(timezone.utc) + datetime.timedelta(hours=24),
        'iat': datetime.datetime.now(timezone.utc),
        'sub': user_id
    }
    return jwt.encode(payload, SECRET_KEY, algorithm='HS256')


# Function for speech recognition
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    
    try:
        query = recognizer.recognize_google(audio)
        print(f"Recognized Speech: {query}")
        return query.lower().strip()
    except sr.UnknownValueError:
        return "Sorry, I couldn't understand your speech."

# Define engine globally
engine = pyttsx3.init()

# Function for text-to-speech
def speak_text(text):
    engine.say(text)
    engine.runAndWait()

@app.route('/set_language/<lang_code>')
def set_language(lang_code):
    response = redirect(request.referrer)
    response.set_cookie('language', lang_code)
    return response

# Home route
@app.route('/')
def home():
    return render_template('home.html')

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()

        # Log the attempted username for debugging purposes
        print(f"Login attempt by username: {username}")

        # Check if the username exists in the database
        user = users_collection.find_one({"username": username})
        if user:
            # Check if the provided password matches the hashed password in the database
            if check_password_hash(user['password'], password):
                full_name = user.get('full_name', 'Unknown User')  # Ensure full_name has a default value
                user_obj = User(
                    str(user['_id']),
                    user['username'],
                    user['password'],
                    user['role'],
                    full_name
                )
                login_user(user_obj)

                # Generate JWT token for session or API use
                token = create_token(str(user['_id']))
                flash(f'Logged in successfully. Token: {token}')

                # Redirect based on the user's role
                if user['role'] == 'admin':
                    return redirect(url_for('admin_dashboard'))
                elif user['role'] == 'user':
                    return redirect(url_for('chatbot_view'))
                else:
                    flash('Role not recognized. Please contact support.')
                    return redirect(url_for('login'))
            else:
                # Password mismatch
                flash('Invalid password. Please try again.')
        else:
            # Username not found
            flash('Username not found. Please check your credentials.')

    return render_template('login.html')


# Logout route
@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('home'))

#about route
@app.route('/about')
def about():
    return render_template('about.html')

#contact route
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # Add logic to process the form (e.g., save to DB or send email)
        flash("Thank you for contacting us! We'll respond shortly.", "success")
        return redirect(url_for('contact'))
    return render_template('contact.html')
path: "{{ url_for('static', filename='animations/contact.json') }}"


# Admin Dashboard route
@app.route('/admin_dashboard')
@login_required
def admin_dashboard():
    if current_user.role == 'admin':
        users = users_collection.find()  # Fetch all users from the database
        medicines = medicines_collection.find()  # Fetch all medicines from the database
        return render_template('admin_dashboard.html', users=users, medicines=medicines)
    flash('Unauthorized access!')
    return redirect(url_for('login'))

# Admin Fix Full Name route
@app.route('/admin/fix_full_name', methods=['POST'])
@login_required
def fix_full_name():
    if current_user.role == 'admin':
        users_collection.update_many(
            {"full_name": {"$exists": False}},
            {"$set": {"full_name": "Anonymous User"}}
        )
        flash('Missing full_name fields have been updated.')
        return redirect(url_for('admin_dashboard'))
    flash('Unauthorized access!')
    return redirect(url_for('login'))

# User Management route
@app.route('/admin/users')
@login_required
def manage_users():
    if current_user.role == 'admin':
        users = users_collection.find()
        return render_template('manage_users.html', users=users)
    flash('Unauthorized access!')
    return redirect(url_for('login'))

# Medicine Management route
@app.route('/admin/medicines')
@login_required
def manage_medicines():
    if current_user.role == 'admin':
        medicines = medicines_collection.find()
        return render_template('manage_medicines.html', medicines=medicines)
    flash('Unauthorized access!')
    return redirect(url_for('login'))

# Edit user route
@app.route('/admin/edit_user/<user_id>', methods=['GET', 'POST'])
@login_required
def edit_user(user_id):
    if current_user.role == 'admin':
        user = users_collection.find_one({"_id": ObjectId(user_id)})
        if request.method == 'POST':
            users_collection.update_one(
                {"_id": ObjectId(user_id)},
                {"$set": {
                    "username": request.form['username'],
                    "email": request.form['email'],
                    "role": request.form['role']
                }}
            )
            flash('User updated successfully!')
            return redirect(url_for('manage_users'))
        return render_template('edit_user.html', user=user)
    flash('Unauthorized access!')
    return redirect(url_for('login'))

# Delete user route
@app.route('/admin/delete_user/<user_id>', methods=['POST'])
@login_required
def delete_user(user_id):
    if current_user.role == 'admin':
        users_collection.delete_one({'_id': ObjectId(user_id)})
        flash('User deleted successfully.')
        return redirect(url_for('manage_users'))
    flash('Unauthorized access!')
    return redirect(url_for('admin_dashboard'))

# Edit medicine route
@app.route('/admin/edit_medicine/<medicine_id>', methods=['GET', 'POST'])
@login_required
def edit_medicine(medicine_id):
    if current_user.role == 'admin':
        medicine = medicines_collection.find_one({"_id": ObjectId(medicine_id)})
        if not medicine:
            flash('Medicine not found.')
            return redirect(url_for('manage_medicines'))
        if request.method == 'POST':
            medicines_collection.update_one(
                {"_id": ObjectId(medicine_id)},
                {"$set": {
                    "name": request.form['name'],
                    "description": {
                        "usage": {
                            "short": request.form['usage_short'],
                            "detailed": request.form['usage_detailed']
                        },
                        "why_to_use": {
                            "short": request.form['why_short'],
                            "detailed": request.form['why_detailed']
                        },
                        "advantages": {
                            "short": request.form['advantages_short'],
                            "detailed": request.form['advantages_detailed']
                        },
                        "disadvantages": {
                            "short": request.form['disadvantages_short'],
                            "detailed": request.form['disadvantages_detailed']
                        },
                        "side_effects": {
                            "short": request.form['side_effects_short'],
                            "detailed": request.form['side_effects_detailed']
                        }
                    }
                }}
            )
            flash('Medicine updated successfully!')
            return redirect(url_for('manage_medicines'))
        return render_template('edit_medicine.html', medicine=medicine)
    flash('Unauthorized access!')
    return redirect(url_for('login'))

# Delete medicine route
@app.route('/admin/delete_medicine/<medicine_id>', methods=['POST'])
@login_required
def delete_medicine(medicine_id):
    if current_user.role == 'admin':
        medicines_collection.delete_one({"_id": ObjectId(medicine_id)})
        flash('Medicine deleted successfully!')
        return redirect(url_for('manage_medicines'))
    flash('Unauthorized access!')
    return redirect(url_for('login'))

# Ensure this runs at application start or as part of the database setup script
medicines_collection.create_index([('name', 'text'), ('description', 'text')])

################admin manage chat history#####
from datetime import datetime
from bson.objectid import ObjectId

# ChatHistory Class
class ChatHistory:
    def __init__(self, collection):
        self.collection = collection

    def add_chat(self, user_id, messages):
        """Insert a new chat entry."""
        chat = {
            "user_id": ObjectId(user_id),  # Ensure user_id is an ObjectId
            "messages": messages,
            "date_created": datetime.utcnow()
        }
        return self.collection.insert_one(chat)

    def get_all_chats(self):
        """Retrieve all chats."""
        return self.collection.find()

    def delete_chat(self, chat_id):
        """Delete a chat by its ObjectId."""
        return self.collection.delete_one({"_id": ObjectId(chat_id)})

# Initialize ChatHistory manager
chat_history_manager = ChatHistory(chat_history_collection)

# Admin route to view all chat histories
@app.route('/admin/chat-history')
@login_required
def chat_history():
    """Admin route to view all chat histories."""
    if current_user.role != "admin":
        flash("Unauthorized access", "danger")
        return redirect(url_for('dashboard'))

    # Retrieve all user chat histories
    chats = []
    for chat in chat_history_manager.get_all_chats():
        user = users_collection.find_one({"_id": ObjectId(chat["user_id"])})
        chats.append({
            "id": str(chat["_id"]),
            "user": user.get("username", "Unknown User") if user else "Deleted User",
            "messages": chat["messages"],
            "date_created": chat["date_created"].strftime("%Y-%m-%d %H:%M:%S")
        })

    return render_template('admin_chat_history.html', chats=chats)

# Admin route to delete a chat
@app.route('/admin/delete-chat/<chat_id>', methods=['POST'])
@login_required
def delete_chat(chat_id):
    """Admin route to delete a chat."""
    if current_user.role != "admin":
        flash("Unauthorized access", "danger")
        return redirect(url_for('dashboard'))

    # Delete chat by its ObjectId
    result = chat_history_manager.delete_chat(chat_id)
    if result.deleted_count > 0:
        flash("Chat deleted successfully", "success")
    else:
        flash("Chat not found", "danger")

    return redirect(url_for('chat_history'))


###chatbot inside user chat history

@app.route('/history', methods=['GET'])
@login_required
def get_history():
    user_id = current_user.id
    history = search_history_collection.find({"user_id": user_id}).sort("timestamp", -1)
    history_list = [{"query": h["query"], "response": h["response"], "timestamp": h["timestamp"].strftime('%Y-%m-%d %H:%M:%S')} for h in history]
    return jsonify(history_list)
# Save the chat history
    chat_history_manager.add_chat(
        current_user._id,  # Current user's ID
        f"Query: {user_input}\nResponse: {response}"  # Combine query and response
    )

    return jsonify({"response": response})

######upload page pdf like docx files
from flask import request, redirect, url_for, flash
import pytesseract
from pdf2image import convert_from_path
from docx import Document
import os
from PIL import Image

# Configure pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Function to extract text from image
def extract_text_from_image(image_path):
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        print(f"Extracted Text from Image:\n{text}")
        return text
    except Exception as e:
        print(f"Error processing image: {e}")
        return None

# Function to process different file types
def extract_text_from_file(file_path):
    extracted_text = ""
    try:
        if file_path.endswith(('.png', '.jpg', '.jpeg')):
            extracted_text = extract_text_from_image(file_path)
        elif file_path.endswith('.pdf'):
            pages = convert_from_path(file_path)
            for page in pages:
                extracted_text += pytesseract.image_to_string(page)
        elif file_path.endswith('.docx'):
            doc = Document(file_path)
            for para in doc.paragraphs:
                extracted_text += para.text
        elif file_path.endswith('.txt'):
            with open(file_path, 'r') as f:
                extracted_text = f.read()
    except Exception as e:
        print(f"Error processing file: {e}")
    return extracted_text

@app.route('/process_file', methods=['POST'])
@login_required
def process_file():
    if 'uploaded_file' not in request.files:
        flash('No file uploaded.')
        return redirect(url_for('chatbot_view'))

    file = request.files['uploaded_file']
    if file.filename == '':
        flash('No file selected.')
        return redirect(url_for('chatbot_view'))

    # Save uploaded file
    file_path = os.path.join('uploads', file.filename)
    file.save(file_path)

    # Extract text
    extracted_text = extract_text_from_file(file_path)

    # Clean up the uploaded file
    os.remove(file_path)

    # Flash extracted text
    if extracted_text:
        flash(f'Extracted Text: {extracted_text}')
    else:
        flash('Failed to extract text from the file.')

    return redirect(url_for('chatbot_view'))

# Test section for OCR functionality
if __name__ == "__main__":
    # Testing OCR with a local image
    test_image_path = "M:\\MediSearch-Chatbot\\static\\images\\test_image.jpg"
    print(f"Testing OCR on image: {test_image_path}")
    test_text = extract_text_from_image(test_image_path)
    if test_text:
        print(f"Extracted Text:\n{test_text}")
    else:
        print("Failed to process the image.")

## chatbot view  routes


from flask import Flask, request, render_template, flash, redirect, url_for, jsonify
from flask_login import login_required, current_user
import re  # Importing regular expressions
import datetime  # For timestamping user history

@app.route('/chatbot', methods=['GET', 'POST'])
@login_required
def chatbot_view():
    if current_user.role == 'user':
        # Extract the username before '@'
        user_display_name = current_user.username.split('@')[0]
        
        response = set()  # Using a set to avoid duplicate responses
        
        # Pre-fill the robot greeting
        robot_greeting = f"Hi {user_display_name}, how can I assist you today?"

        if request.method == 'POST':
            # Get the user query from the form or through speech recognition
            user_query = request.form.get('message', '').lower().strip() if 'message' in request.form else recognize_speech()

            if not user_query:
                flash("Please enter a query.")
                return render_template('chatbot.html', user_display_name=user_display_name, robot_greeting=robot_greeting)

            # Print the user query for debugging purposes
            print(f"Query received: {user_query}")

            # Check if there are any documents matching the text search in the database
            result_count = medicines_collection.count_documents({"$text": {"$search": user_query}})
            if result_count > 0:
                search_result = medicines_collection.find({"$text": {"$search": user_query}})
                for medicine in search_result:
                    description = medicine.get('description', {})

                    # Using regular expressions to ensure accurate keyword matching
                    if re.search(r'\bwhy to use\b', user_query):
                        response_text = f"Reason to use {medicine['name']}: {description['why_to_use']['detailed']}"
                        response.add(response_text)
                    elif re.search(r'\busage\b', user_query):
                        response_text = f"Usage of {medicine['name']}: {description['usage']['detailed']}"
                        response.add(response_text)
                    elif re.search(r'\badvantages\b', user_query):
                        response_text = f"Advantages of {medicine['name']}: {description['advantages']['detailed']}"
                        response.add(response_text)
                    elif re.search(r'\bdisadvantages\b', user_query):
                        response_text = f"Disadvantages of {medicine['name']}: {description['disadvantages']['detailed']}"
                        response.add(response_text)
                    elif re.search(r'\bside effects\b', user_query):
                        response_text = f"Side effects of {medicine['name']}: {description['side_effects']['detailed']}"
                        response.add(response_text)
                    else:
                        response_text = f"Here is a summary for {medicine['name']}: {description['usage']['detailed']}"
                        response.add(response_text)

                    # Save each query and response to the user's history
                    search_history_collection.insert_one({
                        "user_id": current_user.id,
                        "query": user_query,
                        "response": response_text,
                        "timestamp": datetime.datetime.now()
                    })

                if response:
                    for res in response:
                        flash(res)
                else:
                    flash("Sorry, no specific information found for your query.")
            else:
                # If no results are found, save the query with a default response
                flash("Sorry, no information found for your query.")
                search_history_collection.insert_one({
                    "user_id": current_user.id,
                    "query": user_query,
                    "response": "No results found.",
                    "timestamp": datetime.datetime.now()
                })

            return render_template('chatbot.html', user_display_name=user_display_name, robot_greeting=robot_greeting, response="\n".join(response))
        
        # Render the chatbot page for GET requests with the robot greeting
        return render_template('chatbot.html', user_display_name=user_display_name, robot_greeting=robot_greeting)

    # Flash a message and redirect for unauthorized access
    flash('Unauthorized access!')
    return redirect(url_for('login'))


# Signup route
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        surname = request.form['surname']
        middle_name = request.form['middle_name']
        last_name = request.form['last_name']
        username = request.form['username']
        email = request.form['email']
        mobile_number = request.form['mobile_number']
        password = request.form['password']
        role = request.form['role']

        existing_user = users_collection.find_one({"username": username})
        if existing_user:
            flash('Username already exists.')
            return redirect(url_for('signup'))

        existing_email = users_collection.find_one({"email": email})
        if existing_email:
            flash('Email already registered.')
            return redirect(url_for('signup'))

        hashed_password = generate_password_hash(password, method='sha256')
        users_collection.insert_one({
            "surname": surname,
            "middle_name": middle_name,
            "last_name": last_name,
            "username": username,
            "email": email,
            "mobile_number": mobile_number,
            "password": hashed_password,
            "role": role
        })
        flash('Registration successful! Please log in.')
        return redirect(url_for('login'))

    return render_template('register.html')

# Error handler for 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
# For cloud deployment, dynamic port binding
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
