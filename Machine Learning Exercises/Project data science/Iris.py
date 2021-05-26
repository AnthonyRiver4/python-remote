#Setup ##################
#standard imports
import os

#third party imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import datasets

#local imports


sns.set()

#Load Data ###################
def my_function():
    print("hello world")

data = datasets.load_iris()

data.keys()

## What problem are we trying to solve?
# We are trying to use attributes of flowers to predict the species of the flower
# Specifically we are trying to use the sepal lenght and width and the petal length
# and width to predict if an iris flower is of type
# satosa, versicolo or virginica.
#
# This is a multiclass classification problem
#  

# Create a pandas DataFrame from the data
df = pd.DataFrame(data["data"], columns=data["feature_names"])
df["target"] = data["target"]
df.head()

#basic descriptive statistics
df.describe()


#distributions of features and target
df["sepal length (cm)"].hist()


