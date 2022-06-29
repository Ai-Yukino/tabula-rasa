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

# # `tabula-rasa/py/sklearn/C.ipynb`
#
# ---
#
# My solutions for part C of [/12_mod_scikitlearn/05-Exercises.ipynb](https://github.com/lrangellara/tts-ds-fundamentals-course/blob/main/datascience/python/12_mod_scikitlearn/05-Exercises.ipynb)

# + [markdown] tags=[]
# ## 🐍 Python imports 🐍

# +
import os

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
# -

from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

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

df
# -

# ## ❄ Exercise 1.
#
# ---
#
# Write a Python program to split the iris dataset into its attributes (X) and labels (y). The X variable contains the first four columns (i.e. attributes) and y contains the labels of the dataset.

# +
X = df.drop(columns=["Id", "Species"], inplace=False)

X

# +
Y = df["Species"]

Y
# -

# ## 🌸 Exercise 2.
#
# ---
#
# Write a Python program using Scikit-learn to split the iris dataset into 70% train data and 30% test data. Out of total 150 records, the training set will contain 120 records and the test set contains 30 of those records. Print both datasets.

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.30, random_state=2022
)

X_train

Y_train

X_test

Y_test

# + [markdown] tags=[]
# ## ❄ Exercise 3.
#
# ---
#
# Write a Python program using Scikit-learn to convert Species columns in a numerical column of the iris dataframe. To encode this data map convert each value to a number. e.g. Iris-setosa:0, Iris-versicolor:1, and Iris-virginica:2. Now print the iris dataset into 80% train data and 20% test data. Out of total 150 records, the training set will contain 120 records and the test set contains 30 of those records. Print both datasets.

# +
le = preprocessing.LabelEncoder()

df["Species"] = le.fit_transform(df["Species"])

# +
X = df.drop(columns=["Id", "Species"], inplace=False)

X

# +
Y = df["Species"]

Y
# -

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.20, random_state=2022
)

X_train

Y_train

X_test

Y_test

# ## 🌸 Exercise 4.
#
# ---
#
# Write a Python program using Scikit-learn to split the iris dataset into 70% train data and 30% test data. Out of total 150 records, the training set will contain 105 records and the test set contains 45 of those records. Predict the response for test dataset (SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm) using the K Nearest Neighbor Algorithm. Use 5 as number of neighbors.

# +
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, Y_train)
Y_pred = knn.predict(X_test)

Y_pred
# -

Y_pred == Y_test

# ## ❄ Exercise 5.
#
# ---
#
#
#
# Write a Python program using Scikit-learn to split the iris dataset into 80% train data and 20% test data. Out of total 150 records, the training set will contain 120 records and the test set contains 30 of those records. Train or fit the data into the model and calculate the accuracy of the model using the K Nearest Neighbor Algorithm.
#

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, Y_train)
knn.score(X_test, Y_test)

# ## 🌸 Exercise 6.
#
# ---
#
# Write a Python program using Scikit-learn to split the iris dataset into 80% train data and 20% test data. Out of total 150 records, the training set will contain 120 records and the test set contains 30 of those records. Train or fit the data into the model and using the K Nearest Neighbor Algorithm calculate the performance for different values of k.

for i in np.arange(1, 15):
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train, Y_train)
    print(f"For k = {i} accuracy is {knn2.score(X_test, Y_test)}")

# ## ❄ Exercise 7.
#
# ---
#
# Write a Python program using Scikit-learn to split the iris dataset into 80% train data and 20% test data. Out of total 150 records, the training set will contain 120 records and the test set contains 30 of those records. Train or fit the data into the model and using the K Nearest Neighbor Algorithm and create a plot to present the performance for different values of k.

a_index = list(range(1, 11))
a = pd.Series(dtype="float64")

for i in list(range(1, 11)):
    model = KNeighborsClassifier(n_neighbors=i)
    model.fit(X_train, Y_train)
    prediction = model.predict(X_test)
    a = pd.concat([a, pd.Series(metrics.accuracy_score(prediction, Y_test))])

# +
plt.plot(a_index, a)

plt.xlabel("Number of neighbors")
plt.ylabel("Accuracy")
plt.title("Accuracy for different number of neightbors")

plt.show()
# -

# ## 🌸 Exercise 8.
#
# ---
#
# Write a Python program using Scikit-learn to split the iris dataset into 80% train data and 20% test data. Out of total 150 records, the training set will contain 120 records and the test set contains 30 of those records. Train or fit the data into the model and using the K Nearest Neighbor Algorithm and create a plot of k values vs accuracy.

# ## Solution
#
# I modified the sample solution from [here](https://www.w3resource.com/machine-learning/scikit-learn/iris/python-machine-learning-k-nearest-neighbors-algorithm-exercise-8.php) so that it would work the training set variables I already generated.

# +
knn.fit(X_train, Y_train)

no_neighbors = np.arange(1, 9)
train_accuracy = np.empty(len(no_neighbors))
test_accuracy = np.empty(len(no_neighbors))

for i, k in enumerate(no_neighbors):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, Y_train)
    train_accuracy[i] = knn.score(X_train, Y_train)
    test_accuracy[i] = knn.score(X_test, Y_test)

plt.title("k-NN: Varying Number of Neighbors")
plt.plot(no_neighbors, test_accuracy, label="Testing Accuracy")
plt.plot(no_neighbors, train_accuracy, label="Training Accuracy")
plt.legend()
plt.xlabel("Number of Neighbors")
plt.ylabel("Accuracy")
plt.show()
