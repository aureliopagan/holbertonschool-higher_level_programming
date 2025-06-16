import requests

BASE_URL = 'http://127.0.0.1:5000'

def test_home():
    response = requests.get(BASE_URL + '/')
    assert response.status_code == 200
    assert response.text == 'Welcome to the Flask API!'

def test_data_empty():
    response = requests.get(BASE_URL + '/data')
    assert response.status_code == 200
    assert response.json() == []

def test_add_user():
    user = {
        "username": "john",
        "name": "John",
        "age": 30,
        "city": "New York"
    }
    response = requests.post(BASE_URL + '/add_user', json=user)
    assert response.status_code == 201
    data = response.json()
    assert data['message'] == 'User added'
    assert data['user']['username'] == 'john'

def test_data_after_add():
    response = requests.get(BASE_URL + '/data')
    assert response.status_code == 200
    assert 'john' in response.json()

def test_get_user():
    response = requests.get(BASE_URL + '/users/john')
    assert response.status_code == 200
    data = response.json()
    assert data['username'] == 'john'
    assert data['name'] == 'John'

def test_get_unknown_user():
    response = requests.get(BASE_URL + '/users/unknown')
    assert response.status_code == 404
    assert response.json()['error'] == 'User not found'

def test_status():
    response = requests.get(BASE_URL + '/status')
    assert response.status_code == 200
    assert response.text == 'OK'

def test_add_user_without_username():
    user = {
        "name": "Alice",
        "age": 25,
        "city": "San Francisco"
    }
    response = requests.post(BASE_URL + '/add_user', json=user)
    assert response.status_code == 400
    assert response.json()['error'] == 'Username is required'

def test_add_duplicate_user():
    user = {
        "username": "john",
        "name": "Johnny",
        "age": 35,
        "city": "Boston"
    }
    response = requests.post(BASE_URL + '/add_user', json=user)
    assert response.status_code == 400
    assert response.json()['error'] == 'User already exists'

def run_tests():
    test_home()
    print("Test home: OK")
    test_data_empty()
    print("Test data empty: OK")
    test_add_user()
    print("Test add user: OK")
    test_data_after_add()
    print("Test data after add: OK")
    test_get_user()
    print("Test get user: OK")
    test_get_unknown_user()
    print("Test get unknown user: OK")
    test_status()
    print("Test status: OK")
    test_add_user_without_username()
    print("Test add user without username: OK")
    test_add_duplicate_user()
    print("Test duplicate user: OK")
    print("All tests passed!")

if __name__ == '__main__':
    run_tests()
