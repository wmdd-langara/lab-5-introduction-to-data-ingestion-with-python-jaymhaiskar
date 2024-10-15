#!/usr/bin/python3

import os
import csv
import pandas as pd

file_path = 'prices.csv'
with open(file_path, 'r') as file:
    data = file.readlines()

# Function 1: Pure Python Method
def process_py(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    total_price, count = 0, 0
    for line in lines[1:]:
        parts = line.strip().split(',')
        try:
            price = float(parts[14])
            total_price += price
            count += 1
        except (ValueError, IndexError):
            continue  # Skip rows with missing or invalid price
    return total_price / count if count > 0 else 0

# Function 2: CSV Module Method
def process_csv(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        total_price, count = 0, 0
        for row in reader:
            try:
                price = float(row['PRODUCT_PRICE'])
                total_price += price
                count += 1
            except (ValueError, KeyError):
                continue  # Skip rows with missing or invalid price
    return total_price / count if count > 0 else 0

# Function 3: Pandas Method
def process_pandas(file_path):
    df = pd.read_csv(file_path)
    # Convert 'PRODUCT_PRICE' to numeric, forcing errors to NaN, and drop NaNs
    df['PRODUCT_PRICE'] = pd.to_numeric(df['PRODUCT_PRICE'], errors='coerce')
    return df['PRODUCT_PRICE'].mean()

def process_csv_dict(file_path):
    category_totals = {}
    category_counts = {}

    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            category = row['ITEM_CATEGORY_NAME']
            try:
                price = float(row['PRODUCT_PRICE'])

                # Initialize if category not yet in the dictionary
                if category not in category_totals:
                    category_totals[category] = 0
                    category_counts[category] = 0

                # Add the price and increase the count
                category_totals[category] += price
                category_counts[category] += 1
            except (ValueError, KeyError):
                continue  # Skip rows with missing or invalid price

    # Calculate average for each category
    category_averages = {category: category_totals[category] / category_counts[category] 
                         for category in category_totals if category_counts[category] > 0}

    return category_averages


def process_pandas_groupby(file_path):
    # Load the data into a DataFrame
    df = pd.read_csv(file_path)

    # Convert 'PRODUCT_PRICE' to numeric, forcing errors to NaN, and drop NaNs
    df['PRODUCT_PRICE'] = pd.to_numeric(df['PRODUCT_PRICE'], errors='coerce')

    # Group by 'ITEM_CATEGORY_NAME' and calculate the average price
    summary_df = df.groupby('ITEM_CATEGORY_NAME')['PRODUCT_PRICE'].mean().reset_index()

    # Rename the columns for clarity
    summary_df.columns = ['ITEM_CATEGORY_NAME', 'AVERAGE_PRICE']

    return summary_df
if __name__ == '__main__':
    file_path = 'prices.csv'
    print("Pure Python:", process_py(file_path))
    print("CSV Module:", process_csv(file_path))
    print("Pandas:", process_pandas(file_path))

    category_avg = process_csv_dict(file_path)
    print(category_avg)

    summary_stats = process_pandas_groupby(file_path)
    print(summary_stats)
