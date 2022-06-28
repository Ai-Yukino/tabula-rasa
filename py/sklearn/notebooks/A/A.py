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

# # `tabula-rasa/py/sklearn/sklearn.ipynb`
#
# ---
#
# My solutions for part A of [/12_mod_scikitlearn/05-Exercises.ipynb](https://github.com/lrangellara/tts-ds-fundamentals-course/blob/main/datascience/python/12_mod_scikitlearn/05-Exercises.ipynb)

# ## 🐍 Python imports 🐍

# +
import os

import pandas as pd
import numpy as np
from scipy import sparse
# -

# ## ❄ Exercise 1.
#
# ---
#
# Write a Python program to load the iris data from a given csv file into a dataframe and print the shape of the data, type of the data and first 3 rows.

# +
# pd.read_csv("./../../data/iris.csv")

path = os.path.join(".", "..", "..", "data", "iris.csv")
df = pd.read_csv(path)
# -

df.shape

df.dtypes

df.head(3)

# ## 🌸 Exercise 2.
#
# ---
#
# Write a Python program using Scikit-learn to print the keys, number of rows-columns, feature names and the description of the Iris data.

df.keys()

df.shape

df["Species"].unique()

df.describe()

# ## ❄ Exercise 3.
#
# ---
#
# Write a Python program to get the number of observations, missing values and nan values.

df.shape[0]

(df == 0).sum()

(df.isnull()).sum()

# ## 🌸 Exercise 4.
#
# ---
#
# Write a Python program to create a 2-D array with ones on the diagonal and zeros elsewhere. Now convert the NumPy array to a SciPy sparse matrix in [CSR format](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.csr_matrix.html).

matrix = np.eye(5)
print(matrix)

matrix = sparse.csr_matrix(matrix)
print(matrix)

# ## ❄ Exercise 5.
#
# ---
#
# Write a Python program to view basic statistical details like percentile, mean, std etc. of iris data.

df.describe()

# ## 🌸 Exercise 6.
#
# ---
#
# Write a Python program to get observations of each species (setosa, versicolor, virginica) from iris data.

df["Species"].value_counts()

# ## ❄ Exercise 7.
#
# ---
#
# Write a Python program to drop Id column from a given Dataframe and print the modified part. Call iris.csv to create the Dataframe.

df

df.drop(columns="Id", inplace=False)

# ## 🌸 Exercise 8.
#
# ---
#
# Write a Python program to access first four cells from a given Dataframe using the index and column labels. Call iris.csv to create the Dataframe.

df.iloc[1, 0:4]
