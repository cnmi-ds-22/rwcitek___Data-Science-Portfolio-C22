# Naive Bayes Classification to Predict Titanic Survival


**Deep Dive Coding Data Science Bootcamp Sample Project**

---
Robert Citek - October 5th, 2026



## Problem Definition

We would like to tell a passenger on the Titanic whether or not they will survive.  The target column is Survived which is a binary field.  Therefore, this is a supervised, binary classification problem.  We will be using Gaussian Naive Bayes to analyze the data.





## Data Collection/Sources


### Data Overview


This data comes from [Kaggle](https://www.kaggle.com/c/titanic/data), which was then copied to AWS for easy access.

https://ddc-datascience.s3.amazonaws.com/Projects/Example/Data/Titanic.train.csv



### Imports

```python
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from sklearn import metrics
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
```

### File Paths

Create a variable `url` that contains the web link to the CSV data

```python
url = 'https://ddc-datascience.s3.amazonaws.com/Projects/Example/Data/Titanic.train.csv'    # insert url here
url
```

### Load data

Load the data into a data frame named `titanic_df`.

```python
# load data
titanic_df = pd.read_csv( url )
titanic_df

```


### head


Look at the first few rows

```python
# first few rows
titanic_df.head()

```


### tail


Look at the last few rows


```python
# last few rows
titanic_df.tail()

```


### shape


```python
# shape of data frame
titanic_df.shape

```

### size


```python
# size of data frame
titanic_df.size

```


### Summary meta-data


Run the `info()` method on the data frame.


```python
# display meta-data
titanic_df.info()

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

```python
# display summary statistics
titanic_df.describe()

```


### target value_counts()



The target should be the first field that you look at.  Its data type will tell you what kind of machine learning problem this is ( classification or regression. ) Any nulls should be culled.  You can check for any skew in the data set.

```python
# value_counts on target ; include nulls
titanic_df['Survived'].value_counts( dropna = False )

```


```python
# normalized value_counts on target ; include nulls
titanic_df['Survived'].value_counts( dropna=False, normalize=True ) * 100

```

### Nulls



```python
# look for nulls
titanic_df.isnull().sum().sort_values(ascending=False) * 1000


```


```python
# look for nulls, displaying relative frequency
rel_freq = titanic_df.isnull().mean().sort_values( ascending = False ) * 100
rel_freq

```

### dtypes - column data types


Which data types would be appropriate for Gaussian Naive Bayes?


```python
# display data types
titanic_df.dtypes.sort_values()

```

### Unique elements



If the total number of unique items in a field equals the number of rows, that suggests those fields are unique IDs ( e.g. names, IDs ) and should be dropped.


```python
# number of unique elements in a column
titanic_df.nunique(axis='rows').sort_values(ascending=False)

```
## Data Cleaning



### Backup #1


```python
# make backup
titanic_df_bak = titanic_df.copy()
titanic_df_bak

```

```python
# restore from backup
titanic_df = titanic_df_bak.copy()
titanic_df

```


### Keep only the target and one feature


Select `Survived` for the target and `Age` for the single feature

```python
# select the target and one feature
titanic_df = titanic_df[['Survived','Age']]
titanic_df

```

### Backup #2


```python
# make backup
titanic_df_bak2 = titanic_df.copy()
titanic_df_bak2

```

```python
# restore from backup
titanic_df = titanic_df_bak2.copy()
titanic_df

```

### Address any rows with nulls


- If the number of nulls in a column is low, it would be easiest to drop the row.
- If the number of nulls in a column is high, it would be easiest to drop the column.
- If the number of nulls in a column is between the low and high, one should impute values for the nulls.



#### Impute


Impute with the median.


```python
# Calculate the median
titanic_median = titanic_df['Age'].median()
titanic_median

```

```python
# Assign median to nulls
# titanic_df['Age'].fillna( value = titanic_median, inplace = True)  ### the old way
titanic_df.fillna({'Age': titanic_median}, inplace=True)
titanic_df

```

```python
# Verify there are no nulls
titanic_df.isnull().sum()

```

```python
# Verify median is about the same as before
titanic_df['Age'].median()

```

## Exploratory Data Analysis



GNB has two requirements:
1. the features are normally distributed
1. the features are not correlated with each other






### normal distribution of features: histogram


```python
# Display a histogram
titanic_df.hist()

```


### no correlation with single feature




## Processing



```python
titanic_df

```

```python
# Split data frame into target and features
target_col = 'Survived'
target = titanic_df[ target_col ]
features = titanic_df.drop( columns = [ target_col ] )

# features = titanic_df[['Age']]

```

```python
# Verify features
features

```

```python
# Verify target
target

```

### Single Cross Validation ( CV )


Run a single Cross Validation


#### Train Test Split

```python
# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size = 0.25 )

```

```python
# Verify shape of each data set from Train Test Split
for x in [X_train, X_test, y_train, y_test]:
  display(x.shape)

```

#### Model


```python
# Create an empty GNB model
modelGNB = GaussianNB()

```

#### Fit



```python
# Train ( fit ) the model
modelGNB.fit(X_train, y_train)

```

#### Prediction


```python
# Make predicitons using the model
results = modelGNB.predict(X_test)
results

```

```python
results * 100
```

#### Performance



We'll meassure accuracy, which is the proportions of the number correctly predicted, which is mathematically the same as one minus the proportion incorrectly predicted.

```python
# Calculate the accuracy
accuracy = metrics.accuracy_score(y_test, results)
accuracy

```

```python
# Display a confusion matrix
matrix = metrics.confusion_matrix(
    y_test,
    results,
)
matrix

```

```python
sns.heatmap(
    matrix.T,
    square = True,
    annot=True,
    fmt='d',
    cbar=False,

)
plt.xlabel("Actual")
plt.ylabel("Predicted")

```

### Multiple Cross Validation ( CV )


Create a CV loop with 100 iterations.  Capture performance metric in an array names `results`.
Use accuracy for the performance metric.


```python
n = 1_000
results = np.zeros(n)

# Multiple CV loop
for i in range(n):
  # Train Test Split
  X_train, X_test, y_train, y_test = train_test_split(features, target, test_size = 0.25 )

  # Create an empty GNB model
  modelGNB = GaussianNB()

  # Train ( fit ) the model
  modelGNB.fit(X_train, y_train)

  # Make predicitons using the model
  y_pred = modelGNB.predict(X_test)

  # Calculate the accuracy
  results[i] = metrics.accuracy_score(y_test, y_pred)

results
```

```python
# Calculate mean of results
results.mean()

```

```python
# Display a confusion matrix
matrix = metrics.confusion_matrix(
    y_test,
    y_pred,
)
matrix

```

```python
sns.heatmap(
    matrix.T,
    square = True,
    annot=True,
    fmt='d',
    cbar=False,

)
plt.xlabel("Actual")
plt.ylabel("Predicted")

```

```python
# Display a histogram of the results
pd.Series(results).hist()

```


## Communication of Results


Conclusion:

- Lots of false negatives, most likely because we have an unbalance data set with more negatives than positives
- Accuracy is only 62% on average, suggesting that Age is not a very good predictor of surival
- Reasonably good distribution of results, suggesting moslty homogeneous population



Future work:
- add in more features, e.g. Fare
- balance data set
- use other classification methods, e.g. Random Forest

