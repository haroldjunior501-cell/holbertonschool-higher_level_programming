#!/usr/bin/env python3
"""Flask application with JSON, CSV, and SQLite data sources."""
import json
import csv
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)


def create_database():
    """Create and populate the products.db SQLite database."""
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
    cursor.execute("SELECT COUNT(*) FROM Products")
    if cursor.fetchone()[0] == 0:
        cursor.execute('''
            INSERT INTO Products (id, name, category, price)
            VALUES
            (1, 'Laptop', 'Electronics', 799.99),
            (2, 'Coffee Mug', 'Home Goods', 15.99)
        ''')
    conn.commit()
    conn.close()


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


def read_sql():
    """Read and return products from the SQLite database."""
    conn = sqlite3.connect('products.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, category, price FROM Products')
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]


@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')


@app.route('/products')
def products():
    """Render products from JSON, CSV, or SQL based on source query param."""
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source == 'json':
        data = read_json()
    elif source == 'csv':
        data = read_csv()
    elif source == 'sql':
        data = read_sql()
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
    create_database()
    app.run(debug=True, port=5000)
