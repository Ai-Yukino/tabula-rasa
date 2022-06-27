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

# # `tabula-rasa/py/pd/04.ipynb`
#
# ---
#
# My solutions for [/04_Apply/Students_Alcohol_Consumption](https://github.com/zachhall/pandas_exercises/tree/master/04_Apply/Students_Alcohol_Consumption)

# ## ❄ Step 1. Import the necessary libraries

# +
import os

import pandas as pd
import numpy as np
# -

# ## 🌸 Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/Students_Alcohol_Consumption/student-mat.csv).
#
# ## ❄ Step 3. Assign it to a variable called `df`.

path = os.path.join(".", "..", "..", "data", "04", "student-mat.csv")
df = pd.read_csv(path)
df

# ## 🌸 Step 4. For the purpose of this exercise slice the dataframe from `school` until the `guardian` column

df = df.loc[0:, "school":"guardian"]
df

# ## ❄ Step 5. Create a lambda function that will capitalize strings.

cap = lambda s: s.capitalize()

# ## 🌸 Step 6. Capitalize both Mjob and Fjob
#
# ## 🌸 Step 8. Did you notice the original dataframe is still lowercase? Why is that? Fix it and capitalize Mjob and Fjob.

columns = ["Mjob", "Fjob"]
df[columns] = df[columns].applymap(cap)
df[columns]

# ## ❄ Step 7. Print the last elements of the data set.

ser = df.iloc[-1, 0:]
pd.DataFrame(ser).T

# ## ❄ Step 9. Create a function called majority that returns a boolean value to a new column called legal_drinker (Consider majority as older than 17 years old)

majority = lambda age: age > 17
df["legal_drinker"] = df["age"].apply(majority)
df

# ## 🌸 Step 10. Multiply every number of the dataset by 10.
#
# ---
#
# I know this makes no sense, don't forget it is just an exercise

why = lambda x: 10 * x if type(x) is int else x
df = df.applymap(why)
df
