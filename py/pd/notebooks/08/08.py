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

# # `tabula-rasa/py/pd/notebooks/08/08.ipynb`
#
# ---
#
# My solutions for [/08_Creating_Series_and_DataFrames/Pokemon](https://github.com/zachhall/pandas_exercises/tree/master/08_Creating_Series_and_DataFrames/Pokemon)

# ## ❄ Step 1. Import the necessary libraries

import pandas as pd

# ## 🌸 Step 2. Create a data dictionary that looks like the DataFrame below
#
# ## ❄ Step 3. Assign it to a variable called pokemon

dictionary = {
    "evolution": ["Ivysaur", "Charmeleon", "Wartortle", "Metapod"],
    "hp": [45, 39, 44, 45],
    "name": ["Bulbasaur", "Charmander", "Squirtle", "Caterpie"],
    "pokedex": ["yes", "no", "yes", "no"],
    "type": ["grass", "fire", "water", "bug"],
}

# +
df = pd.DataFrame(dictionary)

df
# -

# ## 🌸 Step 4. Ops...it seems the DataFrame columns are in alphabetical order. Place the order of the columns as name, type, hp, evolution, pokedex

# +
df = df[["name", "type", "hp", "pokedex"]]

df
# -

# ## ❄ Step 5. Add another column called place, and insert what you have in mind.

# +
df["place"] = ["Hidden Village", "On a rock", "In a gang", "Viridian Forest"]

df
# -

# ## 🌸 Step 6. Present the type of each column

df.dtypes

# ## 📚 References 📚
#
# - [Ash's Bulbasaur | Bulbapedia](https://bulbapedia.bulbagarden.net/wiki/Ash%27s_Bulbasaur)
# - [Ash's Charizard | Bulbapedia](https://bulbapedia.bulbagarden.net/wiki/Ash%27s_Charizard)
# - [Ash's Squirtle | Bulbapedia](https://bulbapedia.bulbagarden.net/wiki/Ash%27s_Squirtle)
# - [Ash's Butterfree | Bulbapedia](https://bulbapedia.bulbagarden.net/wiki/Ash%27s_Butterfree)
