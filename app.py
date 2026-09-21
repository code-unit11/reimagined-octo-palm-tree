 
from flask import Flask , render_template, request, redirect, url_for, jsonify  
from logic  import  get_response
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

USERNAME = "admin"
PASSWORD = "1234"

# LOGIN PAGE
@app.route("/", methods=["GET", "POST"])
def login():
    error = ""

    if request.method == "POST":
        user = request.form["username"]
        pwd = request.form["password"]

        if user == USERNAME and pwd == PASSWORD:
            return redirect(url_for("index"))
        else:
            error = "Invalid username or password"

    return render_template("login.html", error=error)


# index PAGe
@app.route("/index", methods=["GET", "POST"])
def index():

    response = ""

    if request.method == "POST":
        msg = request.form["msg"]
        response = get_response(msg)

    return render_template("index.html", response=response)


# signup page
@app.route("/signup")
def signup():
    return render_template("signup.html")


# API ROUTE
@app.route("/api/data")
def api_data():
    return jsonify({
        "message": "Hello from Flask API 🚀"
    })
    
# CHATBOT API ROUTE
@app.route("/get", methods=["POST"])
def get_bot_response():

    data = request.get_json()

    user_message = data["message"]

    reply = get_response(user_message)

    return jsonify({
        "response": reply
    })






# Chat API
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message")

    bot_response = get_response(user_message)

    return jsonify({
        "response": bot_response
    })





if __name__ == "__main__":
    app.run(debug=True)