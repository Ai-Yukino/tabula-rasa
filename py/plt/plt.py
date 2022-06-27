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

# # `tabula-rasa/py/plt/plt.ipynb`
#
# ---
#
# My solutions for [/11_mod_matplotlib/17-Exercises.ipynb](https://github.com/lrangellara/tts-ds-fundamentals-course/blob/main/datascience/python/11_mod_matplotlib/17-Exercises.ipynb)

# ## 🐍 Python imports 🐍

# +
import os

import matplotlib.pyplot as plt

plt.style.use("./style/ai.mplstyle")

import numpy as np
import pandas as pd
# -

# ## 📁 Data loading 📁

path = os.path.join(".", "data", "company_sales_data.csv")
df = pd.read_csv(path)
df

# ## ❄ Exercise 1.
#
# ---
#
# Read Total profit of all months and show it using a line plot
#
# Total profit data provided for each month. Generated line plot must include the following properties:
#
# 1. X label name = Month Number
# 2. Y label name = Total profit

# +
plt.figure(figsize=[5.12, 3.84], dpi=100)

plt.plot(df["month_number"], df["total_profit"])

plt.title("Total profit of all months")
plt.xlabel("Month Number")
plt.ylabel("Total profit")

plt.show()
# -

# ## 🌸 Exercise 2.
#
# ---
#
# Get Total profit of all months and show line plot with the following Style properties
#
# Generated line plot must include following Style properties:
#
# 1. Line Style dotted and Line-color should be red
# 2. Show legend at the lower right location.
# 3. X label name = Month Number
# 4. Y label name = Sold units number
# 5. Add a circle marker.
# 6. Line marker color as read
# 7. Line width should be 3

# +
plt.figure(figsize=[6, 4], dpi=105)

plt.plot(
    df["month_number"],
    df["total_profit"],
    ls=":",
    c="red",
    marker="o",
    lw=3,
    label="Total profits over time",
)

plt.title("Total profit of all months")
plt.xlabel("Month Number")
plt.ylabel("Sold units number")

plt.legend(loc="lower right")

plt.show()
# -

# ## ❄ Exercise 3.
#
# ---
#
# Read all product sales data and show it using a multiline plot
#
# Display the number of units sold per month for each product using multiline plots. (i.e., Separate Plotline for each product ).

df

# +
fig, ax = plt.subplots(figsize=[8, 4], dpi=100)

ax.plot(df["month_number"], df["facecream"], label="facecream", ls=":", marker="o")
ax.plot(df["month_number"], df["facewash"], label="facewash", ls=":", marker="^")
ax.plot(df["month_number"], df["toothpaste"], label="toothpaste", ls="-")
ax.plot(df["month_number"], df["bathingsoap"], label="bathingsoap", ls="--", marker="v")
ax.plot(df["month_number"], df["moisturizer"], label="moisturizer", ls=":")
ax.plot(df["month_number"], df["shampoo"], label="shampoo", ls="-", marker="o")

plt.xlabel("Month Number")
plt.ylabel("Sold units number")
plt.title("All product sales", loc="left")

fig.legend(loc="upper center")

plt.show()
# -

# ## 🌸 Exercise 4.
#
# ---
#
# Read toothpaste sales data of each month and show it using a scatter plot
#
# Also, add a grid in the plot. gridline style should “–“.

# +
fig, ax = plt.subplots(figsize=[8, 4], dpi=100)

ax.scatter(df["month_number"], df["toothpaste"])

plt.xlabel("Month Number")
plt.ylabel("Toothpaste sold units number")
plt.title("Toothpaste sales")

ax.set_axisbelow(True)
plt.grid(ls="-")

plt.show()
# -


# ## ❄ Exercise 5.
#
# ---
#
# Read face cream and face wash product sales data and show it using the bar chart
#
# The bar chart should display the number of units sold per month for each product. Add a separate bar for each product in the same chart.

# +
fig, ax = plt.subplots(figsize=[8, 4], dpi=100)

ax.bar(df.month_number, df.facewash, label="Facewash", width=0.15)
ax.bar(df.month_number + 0.25, df.facecream, label="Facecream", width=0.15)
ax.legend(loc="upper right")

plt.xlabel("Month Number")
plt.ylabel("Number of Units Sold")
plt.title("Face cream vs. face wash")

plt.show()
