# Naive Bayes Classification to Predict Titanic Survival

**Deep Dive Coding Data Science Bootcamp Sample Project**

---
Robert Citek - October 5th, 2026


## Problem Definition

State the business problem. Translate the business problem into a Data Science problem by stating what kind of problem it is ( supervised vs unsupervised ) and whether it is a classification, regression, or clustering problem.  Mention which model will be used, if known.

## Data Collection/Sources

### Data Overview

This data comes from [Kaggle](https://www.kaggle.com/c/titanic/data), which was then copied to AWS for easy access.

https://ddc-datascience.s3.amazonaws.com/Projects/Example/Data/Titanic.train.csv


### Imports


```
from IPython.display import Image
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px
import seaborn as sns

from sklearn import datasets, metrics, model_selection
from sklearn import model_selection
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
```

### File Paths

Create a variable `url` that contains the web link to the CSV data


```
url = ''    # insert url here
url
```

### Load data

Load the data into a data frame named `titanic_df`.


```
# load data

```

### head

Look at the first few rows


```
# first few rows

```

### tail

Look at the last few rows



```
# last few rows

```

### shape



```
# shape of data frame

```

### size



```
# size of data frame

```

### Summary meta-data

Run the `info()` method on the data frame.



```
# display meta-data

```

### Summary statistics

Summary statistics give you a quick overview of the data.  Some items to spot check:
- the Target:
  - look for nulls
    - null will be culled
  - look at min, max, median, and mean
    - is it a categorical field masquerading as a number?
- the Features:
  - numerical
    - look at min, max, median, and mean
      - a min=1 and max=count suggests an ID
  - categorical
    - look at unique and freq
      - freq=1, unique=count suggests an ID
      - freq=count suggests a meaningless feature

Run the `describe()` method on the data frame.


```
# display summary statistics

```

### target value_counts()


The target should be the first field that you look at.  Its data type will tell you what kind of machine learning problem this is ( classification or regression. ) Any nulls should be culled.  You can check for any skew in the data set.


```
# value_counts on target ; include nulls

```


```
# normalized value_counts on target ; include nulls

```

### Nulls




```
# look for nulls

```


```
# look for nulls, displaying relative frequency

```

### dtypes - column data types

Which data types would be appropriate for Gaussian Naive Bayes?



```
# display data types

```

### Unique elements


If the total number of unique items in a field equals the number of rows, that suggests those fields are unique IDs ( e.g. names, IDs ) and should be dropped.



```
# number of unique elements in a column

```




## Data Cleaning


### Backup #1



```
# make backup

```


```
# restore from backup

```

### Keep only the target and two features

Select `Survived` for the target and `Age` and `Fare` for the features


```
# select the target and one feature

```

### Backup #2



```
# make backup

```


```
# restore from backup

```

### Address any rows with nulls

- If the number of nulls in a column is low, it would be easiest to drop the row.
- If the number of nulls in a column is high, it would be easiest to drop the column.
- If the number of nulls in a column is between the low and high, one should impute values for the nulls.


#### Impute

Impute with the median.



```
# Calculate the median

```


```
# Assign median to nulls

```


```
# Verify there are no nulls

```


```
# Verify median is about the same as before

```

## Exploratory Data Analysis


GNB has two requirements:
1. the features are normally distributed
1. the features are not correlated with each other

### normal distribution of features: histogram



```
# Display a histogram

```

### independence of features: correlation


```
# Calculate a correlation matrix

```


```
# Display the correlation matrix

```

## Processing




```
# Split data frame into target and features

```


```
# Verify features

```


```
# Verify target

```

### Single Cross Validation ( CV )

Run a single Cross Validation

#### Train Test Split


```
# Train Test Split

```


```
# Verify shape of each data set from Train Test Split

```

#### Model



```
# Create an empty GNB model

```

#### Fit




```
# Train ( fit ) the model

```

#### Prediction



```
# Make predicitons using the model

```

#### Performance


We'll meassure accuracy, which is the proportions of the number correctly predicted, which is mathematically the same as one minus the proportion incorrectly predicted.


```
# Calculate the accuracy

```


```
# Display a confusion matrix

```

### Multiple Cross Validation ( CV )

Create a CV loop with 100 iterations.  Capture performance metric in an array names `results`.
Use accuracy for the performance metric.



```
# Multiple CV loop

```


```
# Calculate mean of results

```


```
# Display a confusion matrix

```


```
# Display a histogram of the results

```

## Communication of Results

Conclusion:

Future work:


