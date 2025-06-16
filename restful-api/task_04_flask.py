from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory user database, stored as a dictionary
users = {}

@app.route('/', methods=['GET'])
def home():
    return 'Welcome to the Flask API!', 200

@app.route('/data', methods=['GET'])
def get_usernames():
    """
    Returns a list of all current usernames.
    """
    return jsonify(list(users.keys())), 200

@app.route('/status', methods=['GET'])
def status():
    return 'OK', 200

@app.route('/users/<username>', methods=['GET'])
def get_user(username):
    """
    Retrieve user info by username.
    """
    user_info = users.get(username)
    if not user_info:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(user_info), 200

@app.route('/add_user', methods=['POST'])
def add_user():
    if not request.is_json:
        return jsonify({'error': 'JSON body required'}), 400

    data = request.get_json()
    username = data.get('username')
    if not username:
        return jsonify({'error': 'Username is required'}), 400

    # Check for duplicate username
    if username in users:
        return jsonify({'error': 'User already exists'}), 400

    user_obj = {
        'username': username,
        'name': data.get('name'),
        'age': data.get('age'),
        'city': data.get('city')
    }
    users[username] = user_obj

    return jsonify({
        'message': 'User added',
        'user': user_obj
    }), 201

if __name__ == '__main__':
    app.run()
    