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

# # `tabula-rasa/py/sklearn/D.ipynb`
#
# ---
#
# My solutions for part D of [/12_mod_scikitlearn/05-Exercises.ipynb](https://github.com/lrangellara/tts-ds-fundamentals-course/blob/main/datascience/python/12_mod_scikitlearn/05-Exercises.ipynb)

# + [markdown] tags=[]
# ## 🐍 Python imports 🐍

# +
import os

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
# -

from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.linear_model import LogisticRegression

# ## 🎨 Styling 🎨

# +
# plt.style.use("./../../style/ai.mplstyle")

path = os.path.join(".", "..", "..", "style", "ai.mplstyle")
plt.style.use(path)
# -

# ## 📁 Data loading 📁

# +
# pd.read_csv("./../../data/iris.csv")

path = os.path.join(".", "..", "..", "data", "iris.csv")
df = pd.read_csv(path)

df.head(3)
# -

df.drop(columns="Id", inplace=True)

df.head(3)

# ## ❄ Exercise 1.
#
# ---
#
# Write a Python program to view some basic statistical details like percentile, mean, std etc. of the species of 'Iris-setosa', 'Iris-versicolor' and 'Iris-versicolor'.

# +
ser = df["Species"] == "Iris-setosa"
df_setosa = df[ser]

df_setosa.tail(3)
# -

df_setosa.describe()

# +
ser = df["Species"] == "Iris-versicolor"
df_versicolor = df[ser]

df_versicolor.tail(3)
# -

df_versicolor.describe()

# +
ser = df["Species"] == "Iris-virginica"
df_virginica = df[ser]

df_virginica.tail(3)
# -

df_virginica.describe()

# ## 🌸 Exercise 2.
#
# ---
#
# Write a Python program to create a scatter plot using sepal length and petal_width to separate the Species classes.

# +
fix, ax = plt.subplots(figsize=[9, 5], dpi=100)

sns.scatterplot(ax=ax, data=df, x="SepalLengthCm", y="SepalWidthCm", hue="Species")

plt.xlabel("Sepal length (cm)")
plt.ylabel("Sepal width (cm)")
plt.legend(loc="upper left")

plt.show()
# -

# ## ❄ Exercise 3.
#
# ---
#
# In statistical modeling, regression analysis is a set of statistical processes for estimating the relationships among variables. It includes many techniques for modeling and analyzing several variables, when the focus is on the relationship between a dependent variable and one or more independent variables (or 'predictors'). Write a Python program to get the accuracy of the Logistic Regression.

# +
X = df.drop(columns="Species", inplace=False).values
Y = df["Species"].values

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.20, random_state=2022
)
# -

model = LogisticRegression(random_state=2022, solver="lbfgs", multi_class="multinomial")
model.fit(X_train, Y_train)

prediction = model.predict(X_test)
metrics.accuracy_score(prediction, Y_test)
