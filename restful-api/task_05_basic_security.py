#!/usr/bin/python3
""" Task 05: Secure API with Flask, JWT, and Basic Auth """

import json
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token,
    jwt_required, get_jwt_identity
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()

# Use a strong secret key
app.config["JWT_SECRET_KEY"] = "your_super_strong_secret_key_here"
jwt = JWTManager(app)

# Users with hashed passwords and roles
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

# Custom error handlers for JWT errors with 401 and specific messages
@jwt.unauthorized_loader
def handle_missing_token(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token(err):
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token(err):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_fresh_token(err):
    return jsonify({"error": "Fresh token required"}), 401

# Basic Auth error handler
@auth.error_handler
def handle_basic_auth_error():
    return jsonify({"error": "Unauthorized"}), 401

# Verify username/password for Basic Auth
@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return username
    return None

# Route protected by Basic Auth
@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    return jsonify({"message": "Basic Auth: Access Granted"}), 200

# Login route: returns JWT token
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    user = users.get(username)
    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401
    # Embed role info in JWT
    identity = {
        "username": username,
        "role": user["role"]
    }
    token = create_access_token(identity=json.dumps(identity))
    return jsonify({"access_token": token}), 200

# Protected route with JWT
@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    identity_str = get_jwt_identity()
    identity = json.loads(identity_str)
    return jsonify({"message": "JWT Auth: Access Granted"}), 200

# Admin-only route with role check
@app.route('/admin-only')
@jwt_required()
def admin_only():
    identity_str = get_jwt_identity()
    identity = json.loads(identity_str)
    if identity.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return jsonify({"message": "Admin Access: Granted"}), 200

# Run app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
