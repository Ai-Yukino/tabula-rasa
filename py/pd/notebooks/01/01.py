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
# # `01.ipynb`
#
# ---
#
# Ai's solutions for [/01_Getting_&_Knowing_Your_Data/Occupation](https://github.com/zachhall/pandas_exercises/tree/master/01_Getting_%26_Knowing_Your_Data/Occupation)
#
# -

# ## ❄ Step 1. Import the necessary libraries

import os
import pandas as pd

# ## 🌸 Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user).
#
# ## ❄ Step 3. Assign it to a variable called users and use the `user_id` as index

path = os.path.join(".", "..", "..", "data", "01", "u.user")
df = pd.read_csv(path, sep="|")

# ## 🌸 Step 4. See the first 25 entries

df.head(25)

# ## ❄ Step 5. See the last 10 entries

df.tail(10)

# ## 🌸 Step 6. What is the number of observations in the dataset?

df.shape[0]

# ## ❄ Step 7. What is the number of columns in the dataset?

df.shape[1]

# ## 🌸 Step 8. Print the name of all the columns.

df.columns

# ## ❄ Step 9. How is the dataset indexed?

df.index

# ## 🌸 Step 10. What is the data type of each column?

df.dtypes

# ## ❄ Step 11. Print only the occupation column

df["occupation"]

# ## 🌸 Step 12. How many different occupations are in this dataset?

df["occupation"].unique().shape[0]

# ## ❄ Step 13. What is the most frequent occupation?

df["occupation"].value_counts().index[0]

# ## 🌸 Step 14. Summarize the DataFrame.

df.describe()

# ## ❄ Step 15. Summarize all the columns

df.describe(include="all")

# ## 🌸 Step 16. Summarize only the occupation column

df["occupation"].describe()

# ## ❄ Step 17. What is the mean age of users?

df["age"].mean()

# ## 🌸 Step 18. What is the age with least occurrence?

# +
ser = df["age"].value_counts()
first_index = ser.argmin()

ser.index[first_index:].tolist()
# -

# ## 📚 References 📚
#
# - [❄ Platform-independent file paths? | Stack Overflow](https://stackoverflow.com/a/6036156)
#     - [📝 Python 3 docs](https://docs.python.org/3/library/os.path.html#os.path.join)
