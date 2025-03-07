from flask import request, jsonify

challenges = [
    {"id": 1, "name": "SQL Injection", "difficulty": "Hard"},
    {"id": 2, "name": "Brute Force", "difficulty": "Medium"},
    {"id": 3, "name": "Networking Scanning", "difficulty": "Hard"},
    {"id": 4, "name": "Basic Password Cracking", "difficulty": "Easy", "hint": "It's a common password!"}
]

def get_challenges():
    return jsonify(challenges)

def basic_password_cracking():
    correct_password = "password123"
    user_input = request.json.get("password", "")

    if user_input == correct_password:
        return jsonify({"message": "Correct! You cracked the password!"})
    else:
        return jsonify({"message": "Incorrect. Try again!"})
