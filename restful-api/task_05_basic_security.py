#!/usr/bin/env python3
"""
API Security and Authentication Techniques.
Implements Basic Auth, JWT-based authentication, and role-based access control.
"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Configure JWT secret key
app.config['JWT_SECRET_KEY'] = 'your-secret-key-change-in-production'

# Initialize authentication components
auth = HTTPBasicAuth()
jwt = JWTManager(app)

# Users dictionary with hashed passwords
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


# ============================================================================
# BASIC AUTHENTICATION HANDLERS
# ============================================================================

@auth.verify_password
def verify_password(username, password):
    """
    Verify username and password for Basic Authentication.
    Args:
        username (str): The username
        password (str): The password
    Returns:
        str: The username if credentials are valid, None otherwise
    """
    if username in users and check_password_hash(users[username]["password"], password):
        return username
    return None


# ============================================================================
# JWT ERROR HANDLERS
# ============================================================================

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """
    Handle missing or invalid JWT token.
    Args:
        err: The error
    Returns:
        JSON: Error message with 401 status
    """
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """
    Handle invalid JWT token.
    Args:
        err: The error
    Returns:
        JSON: Error message with 401 status
    """
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    """
    Handle expired JWT token.
    Args:
        err: The error
    Returns:
        JSON: Error message with 401 status
    """
    return jsonify({"error": "Token has expired"}), 401


# ============================================================================
# BASIC AUTHENTICATION ROUTE
# ============================================================================

@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    """
    Protected route with Basic Authentication.
    Returns:
        str: Access granted message
    """
    return "Basic Auth: Access Granted"


# ============================================================================
# JWT AUTHENTICATION ROUTES
# ============================================================================

@app.route("/login", methods=["POST"])
def login():
    """
    Login endpoint that returns a JWT token.
    Expects JSON body with:
        - username (str, required): The username
        - password (str, required): The password
    Returns:
        JSON: JWT access token with 200 status,
              or error message with 401 status if credentials invalid
    """
    # Get JSON data from request
    data = request.get_json()

    # Check if data is provided
    if not data:
        return jsonify({"error": "Invalid JSON"}), 401

    username = data.get("username")
    password = data.get("password")

    # Check if username and password are provided
    if not username or not password:
        return jsonify({"error": "Missing credentials"}), 401

    # Check if user exists
    if username not in users:
        return jsonify({"error": "Invalid credentials"}), 401

    # Verify password
    if not check_password_hash(users[username]["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    # Create JWT token with username and role
    access_token = create_access_token(
        identity=username,
        additional_claims={"role": users[username]["role"]}
    )

    return jsonify({"access_token": access_token}), 200


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    """
    Protected route with JWT Authentication.
    Returns:
        str: Access granted message
    """
    return "JWT Auth: Access Granted"


@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    """
    Admin-only route with role-based access control.
    Returns:
        str: Admin access message if user is admin,
             or error message with 403 status otherwise
    """
    # Get JWT claims (includes identity and additional_claims)
    from flask_jwt_extended import get_jwt

    claims = get_jwt()
    role = claims.get("role")

    # Check if user has admin role
    if role != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted"


if __name__ == "__main__":
    app.run()
