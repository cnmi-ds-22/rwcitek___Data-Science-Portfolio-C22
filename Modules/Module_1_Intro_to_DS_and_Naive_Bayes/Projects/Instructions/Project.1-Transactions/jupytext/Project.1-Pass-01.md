# Project 1 - Pass 01





## Problem Definition





1. State the business problem. Translate the business problem into a Data Science problem by stating what kind of problem it is ( supervised vs unsupervised ) and whether it is a classification, regression, or clustering problem.  Mention which model will be used, if known.





## Data Collection




2. Load Pandas, Numpy, and Matplotlib modules



```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

```

3. Load data Train.csv from AWS S3.



```python
url = 'https://ddc-datascience.s3.amazonaws.com/Projects/Project.1-Transactions/Data/Transaction.train.csv'
url

```

```python
df = pd.read_csv(
  url,
  usecols=range(5),
  nrows=1_000,
)
df

```

## Data Cleaning




4. Examine the data using tools we have used in class. You should be identifying the various columns such as ...

    - target column
    - feature columns
    - identifier columns
    - null columns
    - null rows

    Tools you should be using include, but are not limited to:




    - head


```python
df.head()

```

    - tail


```python
df.tail()

```

    - shape


```python
df.shape

```

    - size


```python
df.size

```

    - info


```python
df.info()

```

    - describe


```python
df.describe()

```

    - nunique


```python
df.nunique()

```

    - unique


```python
df['target'].unique()

```

    - isnull/isna




```python
df.isnull().sum()

```

5. NOTE: the ‘target’ column indicates a successful transaction (‘1’) or a no-transaction (‘0’). Verify these are the only values in that column, and that there are no nulls.



```python

```

1. If there are data cleaning issues, develop recommendations for how to deal with them.  Specifically, handle these common issues:

    - identifer columns
    - target column with null counts
    - feature columns with high null counts
    - feature columns with low null counts
    - feature columns with medium null counts

## Exploratory Data Analysis

Produce some visual analysis of the data.  Recall that Gaussian Naive Bayes assumes the features are normally distributed and independent. Note: you might have to do multiple plots in groups.

7. Check the distributions of all variables by plotting.



1. Check the correlation values between all **feature columns** to ensure there are no substantial correlations between features. This is important to support the decision to classify the ‘target’ using Naïve Bayes.




1. Create two data frames: one with all successful transactions, one with all unsuccessful transactions. **Make sure they are copies and not slices**.





## Data Processing

### Single Cross-validation ( CV )

10. Create two data sets: one with all the feature columns (everything except for Unnamed: 0, ID_code and target) and one with just the target. Make sure they are copies and not slices.  And make sure they are the correct dimensions.

1. Define an empty Gaussian Naïve Bayes model using Sklearn.

1. Divide the two data sets you created in step #10 into training and testing subsets, i.e. train-test split.

1. Train ( fit ) the model using the training subset of the dataset.

1. Test the model ( predict ) using the testing subset of the dataset.

1. Calculate and report the accuracy.

1. Present a confusion matrix and heatmap

1. Present the results of a Classification Report (sklearn.metrics.classification_report).
