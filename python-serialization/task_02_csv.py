#!/usr/bin/env python3
"""Convert CSV data to JSON format."""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Read a CSV file and write its contents to data.json."""
    try:
        with open(csv_filename, encoding="utf-8") as csv_file:
            rows = list(csv.DictReader(csv_file))
        with open("data.json", "w", encoding="utf-8") as json_file:
            json.dump(rows, json_file)
        return True
    except FileNotFoundError:
        return False
