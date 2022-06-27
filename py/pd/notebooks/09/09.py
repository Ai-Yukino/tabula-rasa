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

# # `tabula-rasa/py/pd/notebooks/08/08.ipynb`
#
# ---
#
# My solutions for [/09_Time_Series/Investor_Flow_of_Funds_US](https://github.com/zachhall/pandas_exercises/tree/master/09_Time_Series/Investor_Flow_of_Funds_US)

# ## ❄ Step 1. Import the necessary libraries

# +
import os

import pandas as pd
# -

# ## 🌸 Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/datasets/investor-flow-of-funds-us/master/data/weekly.csv).
#
# ## ❄ Step 3. Assign it to a variable called

# +
path = os.path.join(".", "..", "..", "data", "09", "weekly.csv")
df = pd.read_csv(path)

df.head()
# -

# ## 🌸 Step 4. What is the frequency of the dataset?

# ### 📝 Solution 📝
#
# ---
#
# Visually looking at the data, the frequency seems to be weekly.

# ## ❄ Step 5. Set the column Date as the index.

# +
df = df.set_index("Date")

df.head()
# -

# ## 🌸 Step 6. What is the type of the index?

df.index.dtype.name

# ## ❄ Step 7. Set the index to a DatetimeIndex type

df.index = pd.to_datetime(df.index)
df.index.dtype.name

# ## 🌸 Step 8. Change the frequency to monthly, sum the values and assign it to monthly.

# +
df = df.resample("M").sum()
df = df[df != 0]

df
# -

# ## ❄ Step 9. You will notice that it filled the dataFrame with months that don't have any data with NaN. Let's drop these rows.

# +
df = df.dropna()

df
# -

# ## 🌸 Step 10. Good, now we have the monthly data. Now change the frequency to year.

# +
df = df.resample("AS-JAN").sum()

df
