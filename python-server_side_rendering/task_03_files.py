from flask import Flask, render_template, request
import json
import csv
import os

app = Flask(__name__)

def read_json_products():
    """Read products from JSON file"""
    try:
        with open('products.json', 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return None

def read_csv_products():
    """Read products from CSV file"""
    try:
        products = []
        with open('products.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Convert price to float and id to int
                row['price'] = float(row['price'])
                row['id'] = int(row['id'])
                products.append(row)
        return products
    except (FileNotFoundError, ValueError, KeyError):
        return None

@app.route('/products')
def display_products():
    source = request.args.get('source', '').lower()
    product_id = request.args.get('id')
    
    # Read products based on source
    if source == 'json':
        products = read_json_products()
    elif source == 'csv':
        products = read_csv_products()
    else:
        return render_template('product_display.html', 
                            error="Wrong source. Please use 'json' or 'csv'")
    
    if products is None:
        return render_template('product_display.html', 
                            error=f"Error reading {source} file")
    
    # Filter by ID if provided
    if product_id:
        try:
            product_id = int(product_id)
            filtered = [p for p in products if p['id'] == product_id]
            if not filtered:
                return render_template('product_display.html',
                                    error=f"Product with ID {product_id} not found")
            products = filtered
        except ValueError:
            return render_template('product_display.html',
                                error="Invalid product ID")
    
    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)