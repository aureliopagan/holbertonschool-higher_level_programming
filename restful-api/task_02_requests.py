import requests
import csv

def fetch_and_print_posts():
    """
    Retrieve all posts from JSONPlaceholder and display the response status
    along with the titles of each post.
    """
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)
    # Print exactly as the test expects
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        all_posts = response.json()
        for post_item in all_posts:
            title_text = post_item.get('title')
            if title_text:
                print(title_text)
    else:
        print(f"Error fetching data: status code {response.status_code}")

def fetch_and_save_posts():
    """
    Fetch all posts and store selected details (id, title, body) into
    a CSV file named 'posts.csv'.
    """
    api_url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(api_url)
    print(f"Response status: {response.status_code}")
    if response.status_code == 200:
        posts_data = response.json()
        post_list = [
            {
                'id': post.get('id'),
                'title': post.get('title'),
                'body': post.get('body')
            }
            for post in posts_data
        ]
        with open('posts.csv', mode='w', encoding='utf-8', newline='') as csv_file:
            headers = ['id', 'title', 'body']
            writer = csv.DictWriter(csv_file, fieldnames=headers)
            writer.writeheader()
            for post_entry in post_list:
                writer.writerow(post_entry)
    else:
        print(f"Error retrieving posts: status code {response.status_code}")
