#!/usr/bin/env python3
"""Flask application that displays product data from JSON or CSV files."""
import json
import csv
from flask import Flask, render_template, request

app = Flask(__name__)


def read_json():
    """Read and return products from products.json."""
    with open('products.json', 'r') as f:
        return json.load(f)


def read_csv():
    """Read and return products from products.csv."""
    products = []
    with open('products.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            products.append({
                'id': int(row['id']),
                'name': row['name'],
                'category': row['category'],
                'price': float(row['price'])
            })
    return products


@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')


@app.route('/products')
def products():
    """Render products from JSON or CSV based on source query parameter."""
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source == 'json':
        data = read_json()
    elif source == 'csv':
        data = read_csv()
    else:
        return render_template('product_display.html', error='Wrong source')

    if product_id is not None:
        try:
            product_id = int(product_id)
        except ValueError:
            return render_template(
                'product_display.html', error='Product not found'
            )
        data = [p for p in data if p['id'] == product_id]
        if not data:
            return render_template(
                'product_display.html', error='Product not found'
            )

    return render_template('product_display.html', products=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
