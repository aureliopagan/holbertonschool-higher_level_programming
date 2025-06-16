#!/usr/bin/python3
""" Task 05: API Security with Flask """

import json
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required,
    get_jwt_identity
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()

# Secret key for JWT
app.config["JWT_SECRET_KEY"] = "your_strong_secret_key_here"
jwt = JWTManager(app)

# Users stored in memory with hashed passwords and roles
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

# Custom error handler for unauthorized access (Basic Auth)
@auth.error_handler
def handle_unauthorized():
    return jsonify({"error": "Unauthorized access"}), 401

# Verify username and password for Basic Auth
@auth.verify_password
def verify_user(username, password):
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return username
    return None

# Basic Auth protected route
@app.route('/basic-protected')
@auth.login_required
def basic_secured():
    return jsonify({"message": "Basic Auth: Access Granted"}), 200

# Login route to generate JWT token
@app.route('/login', methods=['POST'])
def login():
    login_data = request.get_json()
    username = login_data.get("username")
    password = login_data.get("password")

    user_record = users.get(username)
    if not user_record or not check_password_hash(user_record["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    # Embed role info in JWT
    token_payload = {
        "username": username,
        "role": user_record["role"]
    }
    token = create_access_token(identity=json.dumps(token_payload))
    return jsonify({"access_token": token}), 200

# JWT-protected route
@app.route('/jwt-protected')
@jwt_required()
def jwt_secured():
    identity_str = get_jwt_identity()
    identity = json.loads(identity_str)
    return jsonify({"message": "JWT Auth: Access Granted"}), 200

# Admin-only route
@app.route('/admin-only')
@jwt_required()
def admin_route():
    identity_str = get_jwt_identity()
    identity = json.loads(identity_str)
    if identity.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return jsonify({"message": "Admin Access: Granted"}), 200

# Custom handlers for JWT errors
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
def handle_fresh_token_required(err):
    return jsonify({"error": "Fresh token required"}), 401

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
