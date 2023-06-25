#!/usr/bin/env python

import sys

# The input will be in the form of key-value pairs
# It is sorted according to the key
# Each key value pair will be in a new line
# The key and the value are seperated by a tab (\t)
# The key is the payment type and the value is the sales

# Example input data (Key=Payment, Value=Sales)
# Input is ordered by the key
# Visa  205.96
# Cash  11.32
# Cash  444.19

# We want to sum all values with the same key
# Example output data (Key=Payment, Value=Sum of Sales)
# Visa  205.96
# Cash  455.51

# Previous key is initialized with None, we just started
previous_key = None

# sum of sales
sum_of_values = 0

# count starts at 0
count = 0

# Category dictionary 
category_data = {}
# For each new line in the standard input 
for line in sys.stdin:

    # split the line at the tabulator ("\t")
    # strip removes whitespaces and new lines at the beginning and end of the line
    # The result is a tuple with 2 elements
    data = line.strip().split("\t")

    # Store the 2 elements of this line in seperate variables
    category, sales = data

    # Update the count for the category
    if category in category_data:  
       category_data[category]["count"] += 1
       category_data[category]["total_sales"] += float(sales)
    else:
       category_data[category] = {"count": 1, "total_sales":float(sales)}
for category, data in category_data.items():
    count = data["count"]
    total_sales = data["total_sales"]    
    average_sales = total_sales / count

    if count > 114:        
       sys.stdout.write("{0}\t{1}\n".format(category, average_sales))

    
