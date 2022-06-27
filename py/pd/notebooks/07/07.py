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

# # `tabula-rasa/py/pd/notebooks/07/07.ipynb`
#
# ---
#
# My solutions for [/07_Visualization/Scores](https://github.com/zachhall/pandas_exercises/tree/master/07_Visualization/Scores)

# ## ❄ Step 1. Import the necessary libraries

# +
import os

import pandas as pd
import matplotlib.pyplot as plt
# -

path = os.path.join(".", "..", "..", "style", "ai.mplstyle")
plt.style.use(path)

# ## 🌸 Step 2. Create the DataFrame that should look like the one below.

dictionary = {
    "first_name": ["Jason", "Molly", "Tina", "Jake", "Amy"],
    "last_name": ["Miller", "Jacobson", "Ali", "Milner", "Cooze"],
    "age": [42, 52, 36, 24, 73],
    "female": [0, 1, 1, 0, 1],
    "preTestScore": [4, 24, 31, 2, 3],
    "postTestScore": [25, 94, 57, 62, 70],
}

df = pd.DataFrame(dictionary)
df

# ## ❄ Step 3. Create a Scatterplot of preTestScore and postTestScore, with the size of each point determined by age
#
# ---
#
# Hint: Don't forget to place the labels

# +
plt.figure(figsize=[5.12, 3.84], dpi=110)

plt.scatter(x=df["preTestScore"], y=df["postTestScore"], s=df["age"])

plt.title("preTestScore vs. postTestScore")
plt.xlabel("preTestScore")
plt.ylabel("postTestScore")
# -

# ## 🌸 Step 4. Create a Scatterplot of preTestScore and postTestScore.
#
# ---
#
# This time the size should be 4.5 times the postTestScore and the color determined by sex

# +
plt.figure(figsize=[7.68, 5.76], dpi=100)

plt.scatter(
    x=df["preTestScore"],
    y=df["postTestScore"],
    s=4.5 * df["postTestScore"],
    c=df["female"],
)

plt.title("preTestScore vs. postTestScore")
plt.xlabel("preTestScore")
plt.ylabel("postTestScore")
