from flask import Flask, request, render_template, redirect, make_response, get_flashed_messages
import base64
import json
import subprocess

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Set a secret key for sessions
# Hardcoded credentials
USERNAME = "admin"
PASSWORD = "admin"

# Flag is stored in this file
FLAG_PATH = "/app/flag"

def encode_session(data):
    """Encode session data as a Base64 string."""
    # Convert the data to a JSON string
    json_data = json.dumps(data)
    # Encode the JSON string as Base64
    return base64.b64encode(json_data.encode()).decode()

def decode_session(cookie):
    """Decode session data from a Base64 string."""
    try:
        # Decode the Base64 string
        json_data = base64.b64decode(cookie).decode()
        # Parse the JSON string back into a Python dictionary
        return json.loads(json_data)
    except (base64.binascii.Error, json.JSONDecodeError):
        return None

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Check credentials
        if username == USERNAME and password == PASSWORD:
            # Set session cookie with role=user
            session_data = {"role": "user"}
            session_cookie = encode_session(session_data)
            resp = make_response(redirect("/gallery"))
            resp.set_cookie("session", session_cookie)
            return resp
        else:
            return "Invalid credentials!", 401
    return render_template("login.html")

@app.route("/gallery", methods=["GET", "POST"])
def gallery():
    # Decode the session cookie
    session_cookie = request.cookies.get("session")
    session_data = decode_session(session_cookie)

    # Check if the user is admin
    if not session_data or session_data.get("role") != "admin":
        return "Access denied! You are not an admin.", 403

    if request.method == "POST":
        filename = request.form.get("filename", "")
        print(f"Filename: {filename}")  # Debug print
        # Simulate a file viewer feature (vulnerable to command injection)
        try:
            # Use subprocess to execute the command
            command = f"cat {filename}"  # Debug print
            print(f"Command: {command}")  # Debug print
            result = subprocess.run(
                command,  # Command to execute
                shell=True,         # Run in a shell
                capture_output=True, # Capture output
                text=True           # Return output as a string
            )
            print(f"Command Output: {result.stdout}")  # Debug print
            output = result.stdout  # Get the command output
        except Exception as e:
            output = f"Error: {str(e)}\nHint: The treasure might be closer than you think. Look within the app."
        return render_template("gallery.html", output=output)
    return render_template("gallery.html", output="")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)