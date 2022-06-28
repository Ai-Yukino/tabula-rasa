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

# # `tabula-rasa/py/sklearn/B.ipynb`
#
# ---
#
# My solutions for part B of [/12_mod_scikitlearn/05-Exercises.ipynb](https://github.com/lrangellara/tts-ds-fundamentals-course/blob/main/datascience/python/12_mod_scikitlearn/05-Exercises.ipynb)

# ## 🐍 Python imports 🐍 

# +
import os

import pandas as pd
import matplotlib.pyplot as plt
# -

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
# -

# ## ❄ Exercise 1.
#
# ---
#
# Write a Python program to create a plot to get a general Statistics of Iris data.

df_describe = df.describe()
df_describe

# +
fig, ax = plt.subplots(figsize=[8, 4], dpi=100)

df_describe.plot(kind = "area",fontsize = 16, figsize = (8,5))
plt.xlabel('Statistics',)
plt.ylabel('Value')
plt.title("General Statistics of Iris Dataset")
plt.show()
# -

# ## 🌸 Exercise 2.
#
# ---
#
# Write a Python program to create a Bar plot to get the frequency of the three species of the Iris data.

# ## ❄ Exercise 3.
#
# ---
#
# Write a Python program to create a Pie plot to get the frequency of the three species of the Iris data.

# ## 🌸 Exercise 4.
#
# ---
#
# Write a Python program to create a graph to find relationship between the sepal length and width.

# ## ❄ Exercise 5.
#
# ---
#
# Write a Python program to create a graph to find relationship between the petal length and width.

# ## 🌸 Exercise 6.
#
# ---
#
# Write a Python program to create a graph to see how the length and width of SepalLength, SepalWidth, PetalLength, PetalWidth are distributed.

# ## ❄ Exercise 7.
#
# ---
#
# Write a Python program to create a joinplot to describe individual distributions on the same plot between Sepal length and Sepal width. Note: joinplot - Draw a plot of two variables with bivariate and univariate graphs.

# ## 🌸 Exercise 8.
#
# ---
#
# Write a Python program to create a joinplot using "hexbin" to describe individual distributions on the same plot between Sepal length and Sepal width. Note: The bivariate analogue of a histogram is known as a "hexbin" plot, because it shows the counts of observations that fall within hexagonal bins. This plot works best with relatively large datasets. It's available through the matplotlib plt.hexbin function and as a style in jointplot(). It looks best with a white background.

# ## ❄ Exercise 9.
#
# ---
#
# Write a Python program to create a joinplot using "kde" to describe individual distributions on the same plot between Sepal length and Sepal width. Note: The kernel density estimation (kde) procedure visualize a bivariate distribution. In seaborn, this kind of plot is shown with a contour plot and is available as a style in jointplot().

# ## 🌸 Exercise 10.
#
# ---
#
# Write a Python program to create a joinplot and add regression and kernel density fits using "reg" to describe individual distributions on the same plot between Sepal length and Sepal width.

# ## ❄ Exercise 11.
#
# ---
#
# Write a Python program to draw a scatterplot, then add a joint density estimate to describe individual distributions on the same plot between Sepal length and Sepal width.

# ## 🌸 Exercise 12.
#
# ---
#
# Write a Python program to create a joinplot using "kde" to describe individual distributions on the same plot between Sepal length and Sepal width and use '+' sign as marker. Note: The kernel density estimation (kde) procedure visualize a bivariate distribution. In seaborn, this kind of plot is shown with a contour plot and is available as a style in jointplot().

# ## ❄ Exercise 13.
#
# ---
#
# Write a Python program to create a pairplot of the iris data set and check which flower species seems to be the most separable.

# ## 🌸 Exercise 14.
#
# ---
#
# Write a Python program using seaborn to Create a kde (Kernel Density Estimate ) plot of sepal_length versus sepal width for setosa species of flower.

# ## ❄ Exercise 15.
#
# ---
#
# Write a Python program using seaborn to Create a kde (Kernel Density Estimate ) plot of petal_length versus petal width for setosa species of flower.

# ## 🌸 Exercise 16.
#
# ---
#
# Write a Python program using seaborn to Create a kde (Kernel Density Estimate ) plot of petal_length versus petal width for setosa species of flower.

# ## ❄ Exercise 17.
#
# ---
#
# Write a Python program to find the correlation between variables of iris data. Also create a hitmap using Seaborn to present their relations.

# ## 🌸 Exercise 18.
#
# ---
#
# Write a Python program to create a box plot (or box-and-whisker plot) which shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable of iris dataset. Use seaborn.

# ## ❄ Exercise 19.
#
# ---
#
# Write a Python program to create a Principal component analysis (PCA) of iris dataset.
