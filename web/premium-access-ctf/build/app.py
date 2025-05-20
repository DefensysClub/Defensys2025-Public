import os
import hashlib
import base64
from flask import Flask, redirect, request, make_response, render_template
import jwt

app = Flask(__name__)


SECRET_KEY = "falloutboy"
print(SECRET_KEY)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/premium")
def premium():
    token = request.cookies.get("session")
    if not token:
        return redirect("/login")
    try:
        data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        if data.get("is_premium"):
            return render_template("premium.html")
        else:
            return redirect("/payment")
    except:
        return redirect("/login")

@app.route("/payment")
def payment():
    return render_template("payment.html")

@app.route("/login")
def login():
    # Simulate a user login and set a JWT cookie
    payload = {"user": "player", "is_premium": False}
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    resp = make_response(redirect("/premium"))
    resp.set_cookie("session", token)
    return resp

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
