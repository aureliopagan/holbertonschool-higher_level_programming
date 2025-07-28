#!/usr/bin/python3
"""Module for converting CSV data to JSON format."""

import csv
import json

def convert_csv_to_json(csv_filename):
    """Convert CSV file to JSON format.
    
    Args:
        csv_filename: Path to the input CSV file
        
    Returns:
        bool: True if conversion succeeded, False otherwise
    """
    try:
        # Read CSV data
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = [row for row in csv_reader]
        
        # Write JSON data
        with open('data.json', mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)
            
        return True
        
    except (FileNotFoundError, csv.Error, json.JSONEncodeError):
        return False
