from flask import Flask, jsonify, request

app = Flask(__name__)

# Data store for users, keyed by username
users = {}

@app.route('/', methods=['GET'])
def home():
    return 'Welcome to the Flask API!', 200

@app.route('/data', methods=['GET'])
def get_usernames():
    """
    Return a list of all usernames in the system.
    """
    return jsonify(list(users.keys())), 200

@app.route('/status', methods=['GET'])
def status():
    return 'OK', 200

@app.route('/users/<username>', methods=['GET'])
def get_user(username):
    """
    Retrieve user info by username.
    If user doesn't exist, return error message.
    """
    user_info = users.get(username)
    if not user_info:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(user_info), 200

@app.route('/add_user', methods=['POST'])
def add_user():
    """
    Add a new user based on JSON payload.
    Must include 'username'.
    """
    if not request.is_json:
        return jsonify({'error': 'JSON body required'}), 400

    data_received = request.get_json()

    # Extract username
    username_value = data_received.get('username')
    if not username_value:
        return jsonify({'error': 'Username is required'}), 400

    # Prevent duplicate usernames
    if username_value in users:
        return jsonify({'error': 'User already exists'}), 400

    # Build user object
    user_obj = {
        'username': username_value,
        'name': data_received.get('name'),
        'age': data_received.get('age'),
        'city': data_received.get('city')
    }

    # Store the user
    users[username_value] = user_obj

    # Return success message with user data
    return jsonify({
        'message': 'User added',
        'user': user_obj
    }), 201

if __name__ == '__main__':
    app.run()
