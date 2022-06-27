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

# # `tabula-rasa/py/pd/notebooks/10/10.ipynb`
#
# ---
#
# My solutions for [/10_Deleting/Iris](https://github.com/zachhall/pandas_exercises/tree/master/10_Deleting/Iris)

# ## ❄ Step 1. Import the necessary libraries

# +
import os

import pandas as pd
import numpy as np
# -

# ## 🌸 Step 2. Import the dataset from this [address](https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data)

# +
df = pd.read_csv("./../../data/10/iris.data")

df
# -

# ## 🌸 Step 4. Create columns for the dataset

# +
df.columns = ["sepal_length", "sepal_width", "petal_length", "petal_width", "class"]

df
# -

# ## ❄ Step 5. Is there any missing value in the dataframe?

df.isnull().sum()

# ## 🌸 Step 6. Lets set the values of the rows 10 to 29 of the column 'petal_length' to NaN

# +
index = (df.columns == "petal_length").argmax()
df.iloc[10:30, index] = np.nan

df[9:31]
# -

# ## ❄ Step 7. Good, now lets substitute the NaN values to 1.0

# +
df["petal_length"].fillna(value=1, inplace=True)

df[9:31]
# -

# ## 🌸 Step 8. Now let's delete the column class

# +
df = df.drop(columns="class")

df
# -

# ## ❄ Step 9. Set the first 3 rows as NaN

# +
df.iloc[0:3, :] = np.nan

df
# -

# ## 🌸 Step 10. Delete the rows that have NaN

df = df.dropna(how="any")
df

# ## ❄ Step 11. Reset the index so it begins with 0 again

# +
df = df.reset_index(drop=True)

df
