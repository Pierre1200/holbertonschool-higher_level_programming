#!/usr/bin/env python3
"""
Simple Flask API with user management endpoints.
"""
from flask import Flask, jsonify, request
app = Flask(__name__)
# Users dictionary to store user data in memory
users = {}


@app.route("/", methods=["GET"])
def home():
    """
    Root endpoint that returns a welcome message.
    Returns:
        str: Welcome message
    """
    return "Welcome to the Flask API!"


@app.route("/data", methods=["GET"])
def get_data():
    """
    Returns a list of all usernames stored in the API.
    Returns:
        JSON: List of usernames
    """
    return jsonify(list(users.keys()))


@app.route("/status", methods=["GET"])
def get_status():
    """
    Returns the status of the API.
    Returns:
        str: Status message
    """
    return "OK"


@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    """
    Returns the full object corresponding to the provided username.
    Args:
        username (str): The username to retrieve
    Returns:
        JSON: User object if found, or error message with 404 if not found
    """
    if username not in users:
        return jsonify({"error": "User not found"}), 404

    user = users[username].copy()
    user["username"] = username
    return jsonify(user)


@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Adds a new user to the API.
    Expects JSON body with:
        - username (str, required): The username
        - name (str): The user's full name
        - age (int): The user's age
        - city (str): The user's city
    Returns:
        JSON: Confirmation message with user data and 201 status,
              or error message with appropriate status code
    """
    # Check if request body is valid JSON
    try:
        data = request.get_json()
    except Exception:
        return jsonify({"error": "Invalid JSON"}), 400

    # Check if data is None (no JSON provided)
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    # Check if username is provided
    if "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]

    # Check if username already exists
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Add the new user
    users[username] = {
        "name": data.get("name", ""),
        "age": data.get("age", None),
        "city": data.get("city", "")
    }

    # Prepare the response
    response_user = users[username].copy()
    response_user["username"] = username

    return jsonify({
        "message": "User added",
        "user": response_user
    }), 201


if __name__ == "__main__":
    app.run()
