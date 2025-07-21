from flask import Flask, render_template, request
import json
import csv
import sqlite3
import os

app = Flask(__name__)

def read_json_products():
    """Read products from JSON file"""
    try:
        with open('products.json') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"JSON Error: {e}")
        return None

def read_csv_products():
    """Read products from CSV file"""
    try:
        products = []
        with open('products.csv', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                products.append({
                    'id': int(row['id']),
                    'name': row['name'],
                    'category': row['category'],
                    'price': float(row['price'])
                })
        return products
    except (FileNotFoundError, ValueError, KeyError) as e:
        print(f"CSV Error: {e}")
        return None

def read_sql_products():
    """Read products from SQLite database"""
    try:
        conn = sqlite3.connect('products.db')
        conn.row_factory = sqlite3.Row  # Return rows as dictionaries
        cursor = conn.cursor()
        
        cursor.execute("SELECT id, name, category, price FROM Products")
        products = [dict(row) for row in cursor.fetchall()]
        
        conn.close()
        return products
    except sqlite3.Error as e:
        print(f"SQL Error: {e}")
        return None

@app.route('/products')
def display_products():
    """
    Display products from JSON, CSV, or SQL source
    Query parameters:
    - source: 'json', 'csv', or 'sql' (required)
    - id: product ID to filter (optional)
    """
    source = request.args.get('source', '').lower()
    product_id = request.args.get('id', type=int)
    
    # Validate source parameter
    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', 
                            error='Wrong source. Please use "json", "csv", or "sql"')
    
    # Read products based on source
    if source == 'json':
        products = read_json_products()
    elif source == 'csv':
        products = read_csv_products()
    else:  # sql
        products = read_sql_products()
    
    if products is None:
        return render_template('product_display.html',
                            error=f'Error reading {source} data source')
    
    # Filter by ID if provided
    if product_id is not None:
        filtered_products = [p for p in products if p['id'] == product_id]
        if not filtered_products:
            return render_template('product_display.html',
                                error='Product not found')
        products = filtered_products
    
    return render_template('product_display.html', products=products)

def create_database():
    """Initialize the SQLite database with sample data"""
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Products (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                category TEXT NOT NULL,
                price REAL NOT NULL
            )
        ''')
        
        # Insert sample data if table is empty
        cursor.execute("SELECT COUNT(*) FROM Products")
        if cursor.fetchone()[0] == 0:
            cursor.executemany('''
                INSERT INTO Products (id, name, category, price)
                VALUES (?, ?, ?, ?)
            ''', [
                (1, 'Laptop', 'Electronics', 799.99),
                (2, 'Coffee Mug', 'Home Goods', 15.99),
                (3, 'Wireless Headphones', 'Electronics', 149.99)
            ])
        
        conn.commit()
        conn.close()
        print("Database initialized successfully")
    except sqlite3.Error as e:
        print(f"Database initialization failed: {e}")

if __name__ == '__main__':
    # Create database if it doesn't exist
    if not os.path.exists('products.db'):
        create_database()
    
    app.run(debug=True, port=5000)