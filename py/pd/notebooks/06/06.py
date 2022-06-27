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

# # `tabula-rasa/py/pd/notebooks/06/06.ipynb`
#
# ---
#
# My solutiosn for [/06_Stats/US_Baby_Names](https://github.com/zachhall/pandas_exercises/tree/master/06_Stats/US_Baby_Names)

# ## ❄ Step 1. Import the necessary libraries

# + tags=[]
import os
import pandas as pd
# -

# ## 🌸 Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/US_Baby_Names/US_Baby_Names_right.csv).
#
# ## ❄ Step 3. Assign it to a variable called baby_names.
#
# ## 🌸 Step 4. See the first 10 entries

# + tags=[]
path = os.path.join(".", "..", "..", "data", "06", "US_Baby_Names_right.csv")
baby_names = pd.read_csv(path)
baby_names.head(10)
# -

# ## ❄ Step 5. Delete the column 'Unnamed: 0' and 'Id'

baby_names.drop(columns=["Unnamed: 0", "Id"], inplace=True)

# ## 🌸 Step 6. Is there more male or female names in the dataset?

genders = baby_names["Gender"]
genders.value_counts()
genders.value_counts().idxmax()

# ## ❄ Step 7. Group the dataset by name and assign to names

# +
gb = baby_names.groupby("Name")
names = gb["Count"].sum()

names
# -

# ## 🌸 Step 8. How many different names exist in the dataset?

names.shape[0]

# ## ❄ Step 9. What is the name with most occurrences?

ser = names == names.max()
names[ser].shape[0]

names[ser].index[0]

# ## 🌸 Step 10. How many different names have the least occurrences?

# + tags=[]
ser = names == names.min()
names[ser].shape[0]
# -

# ## ❄ Step 11. What is the median name occurrence?

names.median()

# ## 🌸 Step 12. What is the standard deviation of names?

names.std()

# ## ❄ Step 13. Get a summary with the mean, min, max, std and quartiles.

names.describe()
