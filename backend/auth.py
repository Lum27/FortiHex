from flask import request, jsonify
import bcrypt
from database import get_db_connection

def register():
    data = request.json
    username, password = data["username"], data["password"]
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
    conn.commit()
    return jsonify({"message": "Registration successful!"})

def login():
    data = request.json
    username, password = data["username"], data["password"]

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()

    if user and bcrypt.checkpw(password.encode(), user[0]):
        return jsonify ({"message": "Login successful!"})
    return jsonify({"message": "Invalid credentials."}), 401