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

# + [markdown] tags=[]
# # `03.ipynb`
#
# ---
#
# Ai's solutions for [/03_Grouping/Alcohol_Consumption](https://github.com/zachhall/pandas_exercises/tree/master/03_Grouping/Alcohol_Consumption)
# -

# ## ❄ Step 1. Import the necessary libraries

import os
import pandas as pd

# ## 🌸 Step 2. Import the dataset from this address.
#
# ## ❄ Step 3. Assign it to a variable called drinks.

# +
path = os.path.join(".", "..", "..", "data", "03", "drinks.csv")
df = pd.read_csv(path)

df
# -

# ## 🌸 Step 4. Which continent drinks more beer on average?

gb_df = df.groupby("continent")
gb_ser = gb_df["beer_servings"]
gb_ser.mean()

# ## ❄ Step 5. For each continent print the statistics for wine consumption.

gb_df = df.groupby("continent")
gb_ser = gb_df["wine_servings"]
gb_ser.describe()

# ## 🌸 Step 6. Print the mean alcohol consumption per continent for every column

gb_df = df.groupby("continent")
gb_df.mean()

# ## ❄ Step 7. Print the median alcohol consumption per continent for every column

gb_df = df.groupby("continent")
gb_df.median()

# ## 🌸 Step 8. Print the mean, min and max values for spirit consumption.
#
# ---
#
# This time output a DataFrame

gb_df = df.groupby(df["continent"])
gb_ser = gb_df["spirit_servings"]
gb_ser.agg(["mean", "min", "max"])
