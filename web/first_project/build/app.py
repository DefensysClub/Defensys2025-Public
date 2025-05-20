import hashlib
from flask import Flask, render_template, request, redirect, session, render_template_string

app = Flask(__name__)
app.secret_key = "kncxd36)XW!=?#ys*ss+"  # Secret key for session management

# Read dmin_username_SHA512 and flag_structure from a file
with open("admin.txt", "r") as file:
    admin_username_SHA512 = file.readline().strip()  
    flag_structure = file.readline().strip()  
    informations_example = file.readline().strip()  
    flag_example = file.readline().strip()   

# Function to load user data from the file 
def load_users():
    users = []
    with open(USERS_FILE, "r") as file:
        for line in file:
            user_details = line.strip().split(":")  # Splitting the user details
            users.append(user_details)  # Storing user details in the list
    return users

# Function to check login credentials
def check_credentials(username, password):
    with open(USERS_FILE, "r") as file:
        for line in file:
            details = line.strip().split(":")  # Extracting user details
            if len(details) == 9 and details[7] == username and details[8] == password:
                return True  # Regular user credentials match
    return False  # No match found

# Function to add a new user to the file
def add_user_to_file(name, last_name, age, city, country, job, hobby, username, password):
    with open(USERS_FILE, "a") as file:
        file.write(f"{name}:{last_name}:{age}:{city}:{country}:{job}:{hobby}:{hashlib.sha256(username.encode()).hexdigest()}:{hashlib.sha256(password.encode()).hexdigest()}\n")  # Storing user data

USERS_FILE = "users.txt"

# Home page route
@app.route("/")
def index():
    return render_template("index.html")  # Rendering the home page template

# Register page route
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Collect user input from the form
        name = request.form["name"]
        last_name = request.form["last_name"]
        age = request.form["age"]
        city = request.form["city"]
        country = request.form["country"]
        job = request.form["job"]
        hobby = request.form["hobby"]
        username = request.form["username"]
        password = request.form["password"]

        # Save user data 
        add_user_to_file(name, last_name, age, city, country, job, hobby, username, password)

        return redirect("/login")  # Redirect to login page after registration

    return render_template("register.html")  # Rendering the registration page template

# Login page route
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if check_credentials(hashlib.sha256(username.encode()).hexdigest(), hashlib.sha256(password.encode()).hexdigest()):  # Checking login credentials
            session["username"] = username  # Storing username in session
            return redirect("/dashboard")  # Redirecting to dashboard
        else:
            return "Login failed!"  # Invalid credentials

    return render_template("login.html")  # Rendering the login page template

# Dashboard page route 
@app.route("/dashboard")
def dashboard():
    if "username" not in session:
        return redirect("/login")  # Redirect to login if not authenticated
    username = session["username"]
    if hashlib.sha512(username.encode()).hexdigest() == admin_username_SHA512:
        return f"<h2>Welcome, you are the site admin!</h2><p>{flag_structure}</p><p>{informations_example}</p><p>{flag_example}</p>" # Provide the flag structure if the registered user is the admin
    with open(USERS_FILE, "r") as file:
        for line in file:
            details = line.strip().split(":")  # Extracting user details
            if len(details) == 9 and details[7] == hashlib.sha256(username.encode()).hexdigest():
                return render_template_string(f"<h2>Good job, {details[0]}!</h2>") # Say "Good job" if the user is a regular user

# Running the application
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)  # Running Flask app on port 5000


