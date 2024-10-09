[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=16459645)
# Introduction

Be familiar with the techniques presented at 
https://github.com/env3d/python-data-ingestion-basics.

# Question 0

The BC government has made many datasets publicly available via its open data 
portal (https://www2.gov.bc.ca/gov/content/data/open-data).  For this exercise, 
download the BC liquor store produce price list from 
https://catalogue.data.gov.bc.ca/dataset/bc-liquor-store-product-price-list-historical-prices 
(you’ll have to get the direct csv link from the page and use wget or curl to download it to your working directory).
name this file `prices.csv`

# Question 1

Use the three techniques presented (pure python, python csv, and pandas) to calculate the average 
price of all products.  You will create a file called load_data.py in your working directory.  
This python file will contain 3 functions: 

process_py: use the pure python strategy
process_csv: use the csv module
process_pandas: use the pandas module

Below is a template for your load_data.py file:

```python
#!/usr/bin/python3

import pandas
import csv

def process_pandas():
  return 0

def process_csv():
  return 0

def process_py():
  return 0

if __name__ == "__main__":
    print("Average price using pure python: ", end='')    
    print(process_py())
    print("Average price using csv module: ", end='')    
    print(process_csv())
    print("Average price using pandas module: ", end='')    
    print(process_pands())
```

When you run the above program, all three lines should output the same number.

# Question 2 

Create a new functin called process_csv_dict() so it return a dictionary that contains the average for 
each item category, the output of this function must be a dictionary with each key being
the product type and the value being the average price.

```python
>>> process_csv_dict()
{'Wine': 231.77917462743028, 'Spirits': 1375.8744982699216, 'Refreshment Beverages': 15.805849056603703, 'Beer': 17.476013667425885, 'General Merchandise': 13.038000000000002}
```


# Question 3

Create a new function called process_pandas_groupby() so that it returns a dataframe
containing summary statistics of average price of each product using the `groupby` 
function of the Dataframe object.

Here's the documentation to the groupby function:
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html 

The expected output is a dataframe that contains the average price for each 
category of product, as below:

```python
>>> process_pandas_groupby()
                       PRODUCT_PRICE
ITEM_CATEGORY_NAME                  
Beer                       17.476014
General Merchandise        13.038000
Refreshment Beverages      15.805849
Spirits                  1375.874498
Wine                      231.779175
```

