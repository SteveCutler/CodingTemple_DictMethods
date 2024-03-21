# Objective:
# This assignment aims to strengthen your proficiency in Python by tackling 
# challenges that simulate real-world business analytics scenarios. 
# You'll practice copying dictionaries, utilizing built-in methods, 
# managing nested collections, and implementing try-except blocks for error handling.

# Task 1: Sales Data Cloning and Modification
# Gain practical experience in copying dictionaries and modifying data, crucial skills in data analysis.

# Problem Statement:
# You have a dictionary representing weekly sales data for a store. 
# Your task is to create a deep copy of this data and update the sales figures for a specific week.


# Given Sales Data:

# weekly_sales = {
#     "Week 1": {"Electronics": 12000, "Clothing": 5000, "Groceries": 7000},
#     "Week 2": {"Electronics": 15000, "Clothing": 6000, "Groceries": 8000}
# }

#     Create a deep copy of weekly_sales.
#     Update the sales figure for "Electronics" in "Week 2" to 18000 in the copied data.

import copy

weekly_sales = {
    "Week 1": {"Electronics": 12000, "Clothing": 5000, "Groceries": 7000},
    "Week 2": {"Electronics": 15000, "Clothing": 6000, "Groceries": 8000}
}

copied_sales = copy.deepcopy(weekly_sales)

copied_sales["Week 2"]["Electronics"] = 18000

print(f"\noriginal sales = {weekly_sales},\n copied sales = {copied_sales}")