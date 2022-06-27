# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.8
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# # `tabula-rasa/py/pd/notebooks/05/05.ipynb`
#
# ---
#
# My solutions for [/05_Merge/Fictitous Names](https://github.com/zachhall/pandas_exercises/tree/master/05_Merge/Fictitous%20Names)

# ## ❄ Step 1. Import the necessary libraries

import pandas as pd

# ## 🌸 Step 2. Create the 3 DataFrames based on the following raw data
#
# ## ❄ Step 3. Assign each to a variable called data1, data2, data3

# +
raw_data_1 = {
    "subject_id": ["1", "2", "3", "4", "5"],
    "first_name": ["Alex", "Amy", "Allen", "Alice", "Ayoung"],
    "last_name": ["Anderson", "Ackerman", "Ali", "Aoni", "Atiches"],
}

raw_data_2 = {
    "subject_id": ["4", "5", "6", "7", "8"],
    "first_name": ["Billy", "Brian", "Bran", "Bryce", "Betty"],
    "last_name": ["Bonder", "Black", "Balwner", "Brice", "Btisan"],
}

raw_data_3 = {
    "subject_id": ["1", "2", "3", "4", "5", "7", "8", "9", "10", "11"],
    "test_id": [51, 15, 15, 61, 16, 14, 15, 1, 61, 16],
}

# +
dfs = {
    1: pd.DataFrame(raw_data_1, index=raw_data_1["subject_id"]),
    2: pd.DataFrame(raw_data_2, index=raw_data_2["subject_id"]),
    3: pd.DataFrame(raw_data_3, index=raw_data_3["subject_id"]),
}

dfs
# -

dfs[1]

dfs[2]

dfs[3]

# ## 🌸 Step 4. Join the two dataframes along rows and assign all_data

dfs["all_data"] = pd.concat([dfs[1], dfs[2]])
dfs["all_data"]

# ## ❄ Step 5. Join the two dataframes along columns and assing to all_data_col

dfs["all_data_cols"] = pd.concat([dfs[1], dfs[2]], axis=1)
dfs["all_data_cols"]

# ## 🌸 Step 6. Print data3

dfs[3]

# ## ❄ Step 7. Merge all_data and data3 along the subject_id value

dfs["all_data"].merge(dfs[3], on="subject_id")

# ## 🌸 Step 8. Merge only the data that has the same 'subject_id' on both data1 and data2

dfs[1].merge(dfs[2], how="outer", on="subject_id")

# ## ❄ Step 9. Merge all values in data1 and data2, with matching records from both sides where available.

dfs[1].merge(dfs[2], how="inner", on="subject_id")
