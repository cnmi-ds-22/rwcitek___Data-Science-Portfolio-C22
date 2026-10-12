#Numpy

```python
import pandas as pd
import numpy as np

```

## What is [Numpy]( https://en.wikipedia.org/wiki/NumPy )?


- A Python library written in Python and C
- Used for arrays and matrices
- Arrays are similar to Python lists
- More effecient than lists because every element is the **same data type**
- Some math functions - trig functions, random numbers, Boolean logic, etc.
- Can use "vectorization" to efficiently operate on array
- The basis for other data science libraries like Pandas



## Creating arrays


Numpy has some really nice utilities for creating and operating on arrays.



```python
# Create an array using a list
np.array([1,2,3,4,5])

```

```python
arr = np.array([1,2,3,4,5])
type(arr)

```

```python
# Create an array using range()
np.array(range(10))

```

### Your Turn
Create a numpy array of the numbers 1 - 8 using:
1. A list
2. The `range()` function

```python
# Solution

```

```python
# Solution

```

## Similarity to Python lists



Indexing


```python
arr = np.array([1,2,3,4,5])
arr[0]

```

Slicing


```python
arr[1:3]

```

```python
arr[::-1]

```

Many list methods don't work on arrays.


```python
# arr.index(2)
```

But there are often alternatives.


```python
# convert the array to a list
list(arr).index(2)

```

```python
# use a numpy method
(arr == 2).argmax()

```

```python
(arr == 2)

```

```python
arr = arr[::-1]
display(arr)

np.sort( arr )

```

```python
arr

```

## Create Special Types of Arrays



```python
# Create an array of zeros
np.zeros(15)

```

```python
# Create an array of ones
np.ones(5)

```

Using a list and '*'

```python
five_ones = [1] * 5
five_ones

```

```python
five_ones * 4

```

Using an array and '*'


```python
np.ones(5)*4

```

```python
# Create an array (of length 10) full of 7's
np.full(10, 7)

```

```python
# Float
np.full(10, 1.0)

```

```python
# Create an array from 0 to 29 incremented by 3s
# equivalent to np.array(range(0,30,3))
np.arange(0,30,3)

```

```python
# Create an array of 5 equally spaced numbers from 0 to 1
np.linspace(0,1,5)

```

```python
np.linspace(0,1,11)

```

### Your Turn
1. Create an array of the numbers 0 to 20 incremented by 2s. Save it to a variable called `evens`. Then display or print out `evens`.
2. Create the following array
```
array([0.        , 0.33333333, 0.66666667, 1.        ])
```


```python
# Solution

```

```python
# Solution

```


## Two Dimensional Arrays

```python
# Create an array using a list of lists
np.array([[1,2,3], [4,5,6], [7,8,9]])

```

```python
# Create an array using a for loop or list comprehension
np.array([ range(i, i+3) for i in [2,4,6]] )

```

```python
# Create a 2-dimensional array of ones
np.ones((4,5))

```

```python
# Create a 2-dimensional array filled with 7's
np.full((4,5), 7)

```

```python
np.ones((4,5)) * 5

```

```python
# works in a Python list
[[1,2,3], [4,6], [7,8,9]]

```

```python
# Doest not work in numpy
# np.array([[1,2,3], [4,6], [7,8,9]])

```

### Your Turn
1. Create a 2x2 array filled with the word "HI".
2. Create the a 3x3 array with 1's in the first row, 2's in the second row, and 3's in the third row.

```python
# Solution

```

```python
# Solution

```


## Generating Random Numbers


### Floats between 0 and 1

```python
# Generate 10 random numbers from 0 to 1
np.random.random(10)

```


### Normal distribution

```python
# Generate 10 random numbers from a normal distribution with
# a mean 0 and standard deviation of 1
np.random.normal(0,1,10)

```

```python
# pd.Series(np.random.normal(0,1,10)).hist( ) ;
pd.Series(np.random.normal(0,1,100_000)).hist( bins=100 ) ;
pd.Series(np.random.normal(25,3,100_000)).hist( bins=100 ) ;

```

```python
# Generate a 3x3 matrix of random numbers from a normal distribution with
# mean 0 and standard deviation 1
np.random.normal(0, 1, (3,3))

```


### Integers between a range, inclusive to exclusive, [min, max)

```python
# Setting the seed for repeatability
np.random.seed(42)
np.random.randint(1, 7, 25)   # simulating the rolling of a die

```

```python
# Generate a 3x3 matrix of random integers from 0 to 9
np.random.seed(42)
np.random.randint(1, 10, (3,3))

```

### Your Turn
Generate 10 random numbers from the **lognormal** distribution with a mean 0 and standard deviation of 1.

Be sure to set a random seed:
```python
np.random.seed(42)
```

```python
# Solution

```

## dtypes


All elements of the array must be the same data type.  `dtypes` tells us what is the data type of the elements in the array.


```python
arr = np.random.randint(0, 10, (3,3))
print(type(arr))
print(arr.dtype)
print(arr)

```

```python
type(arr[0][0])

```

```python
arr[0,0] = 2.2
print(arr)

```

It will 'upcast' if needed.  
- In this example since we have one float, the integers are upcast to floats too

```python
arr = np.array([1,2,3,4,5,6.2])
print(arr.dtype, arr)

```

We can also specify the datatype.

```python
arr = np.array([1,2,3,4,5], dtype='float16')
arr.dtype

```

```python
arr

```

```python
arr = np.array([1,2,3,4,5], dtype='float')
arr.dtype

```

```python
arr
```

### Your Turn
1. Create an array of the integers 0 - 10. Save it to a variable called `my_array`. 
1. Change the 4 in your array to be equal to 1.4. Print out `my_array`.

```python
# Solutionn

```

```python
# Solutionn

```


## Array Attrributes


What are attributes?
- values associated with an object
- accessed by object.attribute (like methods but without the ())
- lots of objects have attributes

```python
arr1 = np.random.randint( 10, size = 9 )
arr2 = np.random.randint( 10, size = (5,7) )

print(arr1)
print(arr2)

```

```python
#data type
print(arr1.dtype)
print(arr2.dtype)

```

```python
#number of dimensions
print(arr1.ndim)
print(arr2.ndim)

```

```python
#shape (the size of each dimension)
print(arr1.shape)
print(arr2.shape)
```

### Your Turn
1. What does the **size** attribute do?
2. Find the size of `arr1` and `arr2`.

For consistency, set a random seed and the arrays:
```python
np.random.seed(42)
arr1 = np.random.randint( 10, size = 9 )
arr2 = np.random.randint( 10, size = (5,7) )
arr1, arr2

```


```python
# Solution

```

```python
# Solution

```

## Array Indexing


One dimensional arrays - square brackets, starting at 0 (just like lists)

```python
arr = np.random.randint(10, size = 9)
print(arr)
print(arr[0])
print(arr[8])

```

```python
print(arr[-1])

```

Two dimensional arrays - square brackets, starting at 0, comma-separated tuple of indices

```python
np.random.seed(42)
arr = np.random.randint(10, size = (5,4))

print(arr)
print()
print(arr[2,3]) #[row, column]

```

```python
arr

```

```python
arr[2][3]

```

```python
arr[:2]

```

```python
[ [1, 4, 7, 3],
  [5, 3, 3, 1],
  [6, 8, 1, 1],
  [7, 4, 8, 5],
  [5, 2, 5, 7]][2][3]

```

### Your Turn
1. Create an array of 11 equally spaced points from 1 to 5. Save it to a variable called `one_to_five_array`.
2. Use indexing to pull out the `3`.

```python
# Solution

```

```python
# Solution

```

## Slicing Arrays


Note: Default is to return views and not copies



One dimensional

```python
a=5
b=a
c=5

print(a, b, c)

```

```python
a=7
print(a, b, c)

# What's the output?
# 7, 7, 5
# 7, 5, 5
# error
# hello world

```

```python
# Using lists to demonstrate "view" and "copy" concept
a=np.array([1,2,3,4,5])
b=a
c=a.copy()
print("Before ...")
print(f"a: {a}")
print(f"b: {b}")
print(f"c: {c}")

```

```python
a[1]=8
print("After ...")
print(f"a: {a}")
print(f"b: {b}")
print(f"c: {c}")
# a: 1, 8, 3, 4, 5  , b: 1, 2, 3, 4, 5  , c: 1, 2, 3, 4, 5
# a: 1, 8, 3, 4, 5  , b: 1, 8, 3, 4, 5  , c: 1, 2, 3, 4, 5
# a: 1, 2, 3, 4, 5  , b: 1, 8, 3, 4, 5  , c: 1, 2, 3, 4, 5

```

```python
b[3]=23
print(a)
print(b)
print(c)
```

```python
c[3]=20
print(a)
print(b)
print(c)
```

```python
a = 8
print("After ...")
print(f"a: {a}")
print(f"b: {b}")
print(f"c: {c}")
# a: 8  , b: 8  , c: 1, 2, 3, 4, 5
# a: 8  , b: 1, 8, 3, 23, 5  , c: 1, 2, 3, 20, 5
# a: 1, 8, 3, 23, 5  , b: 8  , c: 1, 2, 3, 20, 5
#

```

```python
arr1 = np.random.randint(10, size = 9)
print(arr)

```

```python
# What happens if we don't copy?
arr2 = arr1
arr3 = arr1.copy()
print(f"arr1: {arr1}")
print(f"arr2: {arr2}")
print(f"arr3: {arr3}")

```

```python
arr1[0] = 10
print(f"arr1 (updated): {arr1}")
print(f"arr2 (without copying): {arr2}")
print(f"arr3 (with copying): {arr3}")

```

```python
arr1

```

```python
print(arr1[:7]) #[start:stop:increment]
print(arr1[4:])
print(arr1[4:7])
print(arr1[4:7:2])
print(arr1[4:1:-1])
print(arr1[-5:1:-1])

```

```python
arr1

```

```python
bar = arr1[1::2]
bar

```

```python
arr1[1] = 8

```

```python
arr1

```

```python
bar

```

```python
bar[0] = 22

```

```python
bar

```

```python
arr1

```

### Your Turn
1. Create an 10-element array with numbers 10 through 1. Assign it to a variable called `seq_array`.
2. Make a copy of `seq_array` and save it as `seq_array_copy`.
3. Use slicing to pull out the first 3 elements of `seq_array_copy`.

```python
# Solution

```

```python
# Solution

```

```python
# Solution

```

## Two dimensional slicing

```python
np.random.seed(42)
arr = np.random.randint(10, size = (5,4))
print(arr, '\n')
print(arr[2:4, :]) #[row, column]
print()
print(arr[:, 0:3]) #[row, column]
print()
print(arr[2:4, 0:3]) #[row, column]

```

```python
arr

```

```python
# pull first two columns of an array
print(arr[:,0:2])

```

```python
# slicing both rows and columns, returns a 2-D array
arr[:1,:]

```

```python
# index on rows and slice on columns, returns a 1-D array
arr[0,:]

```

### Your Turn
1. Create a 3x3 array filled with random numbers from a normal distribution with mean 0 and standard deviation 1. Save it to a variable called `normal_array`.
2. Pull out the first row of `normal_array`.

Be sure to set this seed:
```python
np.random.seed(42)
```


```python
# Solution

```

```python
# Solution

```

## Reshaping of Arrays


```python
np.arange?

```

```python
arr = np.arange(9)
arr

```

```python
arr.shape

```

```python
arr = arr.reshape((3,3))
print(arr)
print()
print(arr.reshape(9,))

```

```python
arr

```

```python
arr.shape

```

```python
arr.flatten()

```

```python
arr

```

```python
(
np.arange(3*3*3)
  .reshape((3,3,3))
  .flatten()
)

```

```python
(
np.arange(3*3*3)
.reshape((-1,3))
)

```

### Your Turn
1. Create a 3x3 array full of ones. Assign it to a variable called `ones_matrix`. Display/print `ones_matrix`.
2. Flatten the array. Assign it to a variable called `ones_array`. Display/print `ones_array`.

```python
# Solution

```

```python
# Solution

```

```python
# Solution

```

## Joining and Splitting Arrays

```python
arr1 = np.array([[1,1,1],[2,2,2]])
arr2 = np.array([[3,3,3],[4,4,4]])
print(arr1)
print('')
print(arr2)

```

```python
#default is to concatenate along the first axis (axis=0) - add rows
arr3 = np.concatenate([arr1, arr2])
print(arr3)

```

```python
#can specify to concatenate along the second axis (0 indexing) - add columns
arr4 = np.concatenate([arr1,arr2], axis=1)
print(arr4)

```

```python
arr1[:,0:2]

```

```python
arr1[:,0:2].transpose()

```

```python
arr1[:,2:]

```

```python
arr2

```

```python
np.concatenate([arr1[:,0:2].transpose(),
                arr2,
                arr1[:,2:],
                arr2],
    axis=1)
```

### Your Turn
1. Create a 2x2 array filled with ones. Save it as `ones_array`. Display/print `ones_array`.
2. Create a 2x2 array filled with zeros. Save it as `zeros_array`. Display/print `zeros_array`.
3. Concatenate `ones_array` and `zeros_array` along the first axis (adding more rows) and display/print result.

```python
# Solution

```

```python
# Solution

```

```python
# Solution

```

## Ufuncs
Ufunc is a function that operates on ndarrays in an element-by-element manner.

U is for:

- Universal


```python
my_list = list(range(10))
my_list

```

```python
[
  i * 5
    for i in my_list
]

```

```python
my_nested_list = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
my_nested_list

```

```python
[
[  i * 5
    for i in x
]      for x in my_nested_list
]

```

```python
arr = np.arange(9).reshape((3,3))
print(arr)

```

```python
arr

```

```python
print(arr + 5)

```

```python
print(arr - 5)

```

```python
print(arr / 5)

```

```python
print(arr // 5)

```

```python
print(3 ** arr)

```

```python
3 ** 8

```

```python
print(arr ** 3)

```

```python
8 ** 3

```

```python
print(arr % 3)

```

```python
arr.reshape(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,3) + 1

```

## Aggregate Functions

```python
# Sum across all elements
print(arr)
print(np.sum(arr))  # function
print(arr.sum())   # method
print(8*(8+1)//2)  # n(n+1)/2 = sum of a seres of number from 0

```

```python
# Find the minimum
np.min(arr)  # function
arr.min()    # method

```

```python
# Find the maximum
np.max(arr)  # function
arr.max()    # method

```

```python
# Calculate the mean
np.mean(arr)  # function
arr.mean()    # method

```

```python
# Find the median
np.median(arr)  # function
# arr.median()    # method

```

```python
# use a list as an argument
mylist = [1,2,3]
np.mean(mylist)

```

### Your Turn
1. Create a 100-element array filled with random numbers from a normal distribution with mean 10 and standard deviation 1. Save it as `random_array`. Display/print `random_array`.
2. Display/print these five summary statistics of your array:
  - min
  - max
  - mean
  - **sample** standard deviation
  - **population** standard deviation 

Be sure to set this seed:
```python
np.random.seed(42)
```


```python
# Solution

```

```python
# Solution

```


## Boolean Arrays

```python
np.random.seed(42)
arr = np.random.randint(10, size=(4,5))
print(arr)

```

```python
filter = ( arr < 3 )
print( filter )

```

```python
# filtering
arr[ filter ]

```

```python
( filter ) * 1

```

```python
( filter ) + 0

```

```python
arr[ filter + 0 ]

```

```python
# count of elements that meet a condition
np.count_nonzero( filter )

```

```python
# count of elements that meet a condition
np.sum( filter )

```

```python
( filter ).sum()

```

```python
# proportion that meets a conditions - nb: there are 20 elements
( filter ).mean()

```

Boolean Masks - Boolean Indexing

```python
mask = ( arr < 3 )
print(arr)

```

```python
print(mask)

```

```python
arr * mask

```

```python
arr.flatten()

```

```python
mask.flatten()

```

```python
mask.flatten()+0

```

```python
arr.flatten() * (mask.flatten()+0)

```

```python
arr.flatten(), mask.flatten()+0, arr.flatten() * (mask.flatten()+0)

```

```python
(arr.flatten() * (mask.flatten()+0)).reshape(4,5)

```

```python
arr*(arr < 4)

```

```python
arr*(arr < 4)

```

For logical AND and OR, use `&` or `|` (NOT and, or)

```python
mask = ((arr % 2 == 0) & (arr >= 6))
mask+0

```

```python
arr * ( mask )

```

```python
mask = np.logical_and((arr % 2 == 0),(arr >= 6))
arr*mask

```

```python
mask = (arr % 2 == 0) | (arr >= 6)
print((arr*mask)*100)
print("")
filter = mask
print((arr[filter])*100)

```

```python
arr*((arr % 2 == 0) | (arr >= 6))

```

```python
mask = np.logical_or((arr % 2 == 0), (arr >= 6))
arr*mask

```

Logical XOR

```python
arr*((arr % 2 == 0) ^ (arr >= 6))

```

```python
arr*np.logical_xor((arr % 2 == 0), (arr >= 6))

```

Logical NOT

```python
arr

```

```python
arr >= 6

```

```python
arr*(arr >= 6)

```

```python
arr*np.logical_not(arr >= 6)

```

### Your Turn
1. Create an 20 element array with random integers from 0 to 20. Assign it to a variable called `my_array`.  Display/print `my_array`.
2. Use boolean indexing to display/print the values of the array that are greater than 10.
3. Use boolean indexing to display/print the values of the array that are less than 3 or greater than 15.

Feel free to use either filtering, masking, or both.

You may want to adjust the line width for displaying long arrays.  And set a random seed.
```python
lw = 200  # Adjust the value as needed
np.set_printoptions(linewidth = lw)
np.random.seed(42)
````

```python
# Solution

```

```python
# Solution

```

```python
# Solution

```

