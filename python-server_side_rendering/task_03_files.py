from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json_products():
    """Read and parse products from JSON file"""
    try:
        with open('products.json') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error reading JSON file: {e}")
        return None

def read_csv_products():
    """Read and parse products from CSV file"""
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
        print(f"Error reading CSV file: {e}")
        return None

@app.route('/products')
def display_products():
    """
    Display products from JSON or CSV source
    Query parameters:
    - source: 'json' or 'csv' (required)
    - id: product ID to filter (optional)
    """
    source = request.args.get('source', '').lower()
    product_id = request.args.get('id', type=int)
    
    # Validate source parameter
    if source not in ['json', 'csv']:
        return render_template('product_display.html', 
                            error='Wrong source. Please use "json" or "csv"')
    
    # Read products based on source
    products = read_json_products() if source == 'json' else read_csv_products()
    
    if products is None:
        return render_template('product_display.html',
                            error=f'Error reading {source} file')
    
    # Filter by ID if provided
    if product_id is not None:
        filtered_products = [p for p in products if p['id'] == product_id]
        if not filtered_products:
            return render_template('product_display.html',
                                error='Product not found')
        products = filtered_products
    
    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)