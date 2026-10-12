# Matplotlib

Matplotlib is a classic plotting library for Python.  Later in the class we'll touch on some other plotting options.  Since matplotlib is a historical standard and many other DS libraries integrate its functionality, we will cover it first.  

This notebook is intended to be something of a reference for matplotlib - the goal isn't to memorize what is in here, but to be familiar with what is possible and know where to look when you need it.


## Import

```python
import matplotlib.pyplot as plt
import numpy as np
```

## Setting Styles
All styles can be found [here](https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html).

```python
plt.style.use('seaborn-v0_8-whitegrid') ;
```

```python
plt.style.library
```

## Plotting a Function

```python
#figure is a container with axes, graphics, text, labels
fig = plt.figure()
x = np.linspace(0, 10, 100)
plt.plot(x, np.sin(x), '-');      # solid line
plt.plot(x, np.cos(x), '--');     # dashed line
```

```python
x[:10]
```

### Your Turn
Create a plot of the tangent of x (`np.tan(x)`) using a dashed line.

```python
# Solution
fig = plt.figure()
x = np.linspace(0, 10, 100)
plt.plot(x, np.tan(x), '--');

```

## Saving Plots

```python
# PNG - a raster image
fig.savefig('sine_cosine.png', )

```

```python
# SVG - a vector image
fig.savefig('sine_cosine.svg')

```

```python
ls
```

Click on folder icon to the left to see image.  Right click and download.

```python
# @title Sine and Cosine
from IPython.display import Image
Image('sine_cosine.png')
```

## Line Colors
Named colors in python are located [here](https://matplotlib.org/stable/gallery/color/named_colors.html).

```python
x = np.linspace(0, 10, 100)
plt.plot(x, np.sin(x - 0), color='blue')        # specify color by name
plt.plot(x, np.sin(x - 1), color='g')           # short color code (rgbcmyk)
plt.plot(x, np.sin(x - 2), color='0.75')        # Grayscale between 0 and 1
plt.plot(x, np.sin(x - 3), color='#FFDD44')     # Hex code (RRGGBB from 00 to FF)
plt.plot(x, np.sin(x - 4), color=(1.0,0.2,0.3)) # RGB tuple, values 0 to 1
plt.plot(x, np.sin(x - 5), color='chartreuse'); # all HTML color names supported
```

### Your Turn
Create a plot of the tangent of x using 4 colors. Try to use a few different colors than the ones used in the example above.

```python
# Solution
x = np.linspace(0, 10, 100)
plt.plot(x, np.tan(x - 0), color='blue')
plt.plot(x, np.tan(x - 3), color='cornsilk')
plt.plot(x, np.tan(x - 4), color="tab:orange")
plt.plot(x, np.tan(x - 5), color='xkcd:cornflower blue');
```

## Line Styles

```python
plt.plot(x, x + 0, linestyle='solid')
plt.plot(x, x + 1, linestyle='dashed')
plt.plot(x, x + 2, linestyle='dashdot')
plt.plot(x, x + 3, linestyle='dotted');

# For short, you can use the following codes:
plt.plot(x, x + 4, linestyle='-')  # solid
plt.plot(x, x + 5, linestyle='--') # dashed
plt.plot(x, x + 6, linestyle='-.') # dashdot
plt.plot(x, x + 7, linestyle=':');  # dotted
```

```python
# Combining styles and colors
plt.plot(x, x + 0, 'g-')  # solid green
plt.plot(x, x + 1, '--c') # dashed cyan
plt.plot(x, x + 2, '-.k') # dashdot black
plt.plot(x, x + 3, ':r')  # dotted red

# explicit is preferred
plt.plot(
    x,
    x + 4,
    linestyle = "solid",
    color = "green",
) ;  # solid green

```

### Your Turn
1. Create a variable called `time`. Set it equal to a numpy array of 20 equally spaced points between 0 and 1.
2. Create a second variable called `population` and set it equal to the following
`population = np.exp(time)`
3. Plot `population` versus `time` using a dashdot blue line.  

```python
# Solution
time = np.linspace(0, 1, 20)
time

```

```python
# Solution
population = np.exp(time)
population

```

```python
# Solution
plt.plot(
    time,
    population,
    linestyle = "dashdot",
    color = "blue",
) ;  # dashdot blue line

```

## Axes Settings

```python
plt.plot(x, np.sin(x))

# Set them individually
plt.xlim(-1, 11)
plt.ylim(-1.5, 1.5)
```

```python
plt.plot(x, np.sin(x))
# set them together [xmin, xmax, ymin, ymax]
plt.axis([-1, 11, -1.5, 1.5]);
```

```python
# make a square plot
plt.plot(x, np.sin(x))
plt.axis('square');
```

```python
help(plt.axis)
```

## Labeling Plots/ Text Size

```python
plt.plot(x, np.sin(x))
plt.title("A Sine Curve", size=40, bbox=dict(facecolor='blue', alpha=0.1))
plt.xlabel("x", size=20)
plt.ylabel("sin(x)");

```

```python
help(plt.xlabel)
```

```python
help(plt.text)
```

### Your Turn
Create a plot of population versus time using a solid green line. Add x- and y-axis labels. Add a title to your plot. Change the y-axis limits to be from 0 to 3.

```python
# Solution
plt.plot(
    time,
    population,
    linestyle = "solid",
    color = "green",
) ;  # solid greeen

plt.title("Population Future", size=35,)
plt.xlabel("Time", size=20)
plt.ylabel("Population", size=20);
plt.ylim(0, 3)

```

## Scatter Plots


```python
x = np.linspace(0, 10, 30)
y = np.sin(x)
#changing the symbol from '-' to 'o' is all it takes to change
#from a line plot to a scatter plot
plt.plot(x, y, 'o', color='blue');
```

```python
plt.scatter(x, y, color = 'black') ; # or you can use plt.scatter
```

## Symbol types

```python
# rng = np.random.RandomState(0)
plt.figure(figsize = (20,5))
i = 0
for marker in ['o', '.', 'p', 'x', '+', 'v', '^', '<', '>', 's', 'd']:
    plt.plot(i, i, marker, label=f"marker='{marker}'", markersize = 12)
    i += 1
plt.legend(loc = 'upper left', numpoints=2)
plt.xlim([-1,11])
plt.ylim([-1,16]) ;
```

```python
plt.figure(figsize = (10,5))
for i, marker in enumerate( ['o', '.', 'p', 'x', '+', 'v', '^', '<', '>', 's', 'd'] ):
    plt.plot(i, i, marker, label=f"marker='{marker}'", markersize = 12)
plt.legend(loc = 'upper left')
plt.xlim([-1,11])
plt.ylim([-1,16]) ;
```

```python
plt.plot(x, y, '--', ) ;
```

```python
# Lines and points
plt.plot(
    x,
    y,

    # line attributes
    color='black',
    linestyle="dashed",
    linewidth=4,

    # marker attributes
    marker = "p",
    markersize=15,
    markerfacecolor='white',
    markeredgecolor='blue',
    markeredgewidth=2,
    )
plt.ylim(-1.2, 1.2);
```

```python
# Lines and points
plt.plot(
    x,
    y,
    '-kp',

    # color='black',
    # linestyle="dashed",
    linewidth=4,

    # marker = "p",
    markersize=15,
    markerfacecolor='white',
    markeredgecolor='blue',
    markeredgewidth=2,
    )
plt.ylim(-1.2, 1.2);
```

### Your Turn
1. Create a scatter plot of population versus time. Use the marker of your choice. Set the color of your marker to 'slateblue'. Change the markersize to 10.
2. Create a second plot of population versus time that has both a line and points. Use a red dashed line with linewidth 3. Use black diamond shaped points with markersize 12.

```python
# Solution
# Solution
plt.plot(
    time,
    population,
    # 'v',
    linestyle = "none",

    marker = "v",
    markersize=10,
    markerfacecolor='slateblue',
    markeredgecolor='black',
    markeredgewidth=2,

) ;


```

```python
# Solution
# Solution
# Solution
plt.plot(
    time,
    population,
    linestyle = "dashed",
    color="red",
    linewidth=3,

    marker = "d",
    markersize=12,
    markerfacecolor='black',
    markeredgecolor='yellow',
    markeredgewidth=1,

) ;


```

## plt.scatter - more powerful scatter plots


plt.scatter - change the marker type dynamically based on the data - good to use the marker type to portray more information.

Downside is it takes longer to make the display - bad for really large datasets.

```python
n = 100
x = np.random.random(n)
y = np.random.random(n)
colors = np.random.random(n)
sizes = 1000 * np.random.random(n)

plt.scatter(
  x,
  y,
  c=colors,
  s=sizes,
  marker="o",
  alpha=.3,
  cmap='RdYlBu',
)
plt.colorbar() ;  # show color scale
```

```python
( x, y, colors, sizes )
```

```python
# Iris data set
from sklearn.datasets import load_iris
import pandas as pd
iris = load_iris()
features = pd.DataFrame(iris.data, columns = iris.feature_names)
features.head()
```

```python
features.shape
```

```python
iris.target_names
```

```python
iris.target
```

```python
(iris.target+1)
```

```python
(iris.target+1)*50
```

```python
plt.scatter?
```

```python
plt.scatter(
  features['sepal length (cm)'],
  features['sepal width (cm)'],
  alpha=0.3,
  # s = (iris.target),
  s = (iris.target+1)*50,
  c = iris.target,
  cmap='viridis'
)
plt.colorbar()
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1]) ;

```

### Your Turn

Use `plt.scatter()` to create a scatterplot of petal width versus petal length. Set the size and color of the points equal to the species. Add x and y axis labels.



```python
# Iris data set
from sklearn.datasets import load_iris
import pandas as pd

iris = load_iris()
iris.keys()
```


```python
# Iris data set
from sklearn.datasets import load_iris
import pandas as pd

iris = load_iris()
iris.keys()
```

```python
# Solution
x_name = iris.feature_names[2]
y_name = iris.feature_names[3]
x_name, y_name

```

```python
plt.scatter(
  features[x_name],
  features[y_name],
  alpha=0.3,
  # s = (iris.target),
  s = (iris.target+130),
  c = iris.target,
  cmap='viridis'
)
plt.colorbar()
plt.xlabel(x_name)
plt.ylabel(y_name) ;

```

## Histograms


```python
np.random.seed(100)
x1 = np.random.normal(0, 0.8, 1000)
x2 = np.random.normal(-2, 1, 1000)
x3 = np.random.normal(3, 2, 1000)
n = int(1000**(1/2))
# n= None
plt.hist(x1, alpha=0.6, bins=n, color='black')
plt.hist(x2, alpha=0.3, bins=n)
n = 1_000
plt.hist(x3, alpha=0.3, bins=n)
n

```

```python
((x3>=6) & (x3 < 7)).sum()
```

### Your Turn
1. Create a variable called `weight` and set it equal to 1000 numbers generated from a normal distribution with mean 150 and standard deviation 10.
2. Create a histogram of `weight` with 5 bins.
3. Create a separate histogram of `weight` with 30 bins.

```python
# Solution
weight = np.random.normal(150, 10, 1_000)
weight.size

```

```python
# Solution
plt.hist(weight, bins = 5 ) ;

```

```python
# Solution
plt.hist(weight, bins = 30 ) ;

```

```python
plt.hist(weight, bins = 5 ) ;
plt.hist(weight, bins = 30 ) ;

```

## Legends

```python
x = np.linspace(0, 10, 100)
plt.plot(
    x,
    np.sin(x),
    '-',
    label='sine',
    ) ;

plt.plot(
    x,
    np.cos(x),
    '--r',
    label='cosine',
    ) ;

# the legend will include the lines with labels
plt.legend();

```

```python
plt.plot(x, np.sin(x), '-', label='sine')
plt.plot(x, np.cos(x), '--r', label='cosine')

#frame alpha determines transparency
plt.legend(
    loc='upper right',
    frameon=True,
    framealpha=0.3,
    ) ;

```

```python
plt.plot(
    x,
    np.sin(x),
    '-',
    label='sine',
    )
plt.plot(
    x,
    np.cos(x),
    '--r',
    label='cosine',
    )
plt.legend(
    ncol=2,
    frameon=True,
    framealpha=0.8,
    bbox_to_anchor=(0.70, -.05),
    ); # Put legend outside of plot
```

### Your Turn
1. Create a variable called `weight_kids` that is 100 values generated from a normal distribution with mean 50 and standard deviation 5.
2. Create a variable called `weight_adults` that is 100 values generaated from a normal distribution with mean 170 and standard deviation 20.
3. Plot histograms of `weight_kids` and `weight_adults` on the same plot. Include a legend for your two histograms.

```python
# Solution
weight_kids = np.random.normal(50, 5, 100)
weight_kids.size

```

```python
# Solution
weight_adults = np.random.normal(170, 20, 100)
weight_adults.size

```

```python
# Solution
plt.hist(
    weight_kids,
    label="Kids",
)
plt.hist(
    weight_adults,
    label="Adults",
)

plt.legend(
    ncol=2,
    frameon=True,
    framealpha=0.8,
    bbox_to_anchor=(0.70, -.05),
    ); # Put legend outside of plot
```

## Dictionaries to set styles

```python
# Set the font dictionaries (for plot title and axis titles)
title_font = {
    'size':'16',
    'color':'olive',
    'weight':'normal',
    'verticalalignment':'bottom',
    } # Bottom vertical alignment for more space

axis_font = {
    'color':'green',
    'size':'20',
    # 'size':'10',
   }

title_font, axis_font

```

```python
plt.plot(x, np.sin(x)) ;

plt.title("A Sine Curve", **title_font)
plt.xlabel("x", **axis_font)
plt.ylabel("sin(x)", **axis_font) ;

```

## More Styles

```python
# reset everything to classic
# otherwise some settings may not be overridden when setting a new style
plt.style.use('classic')
#set the style for the whole session
plt.style.use('fivethirtyeight')
fig = plt.figure()
x = np.linspace(0, 10, 100)
plt.plot(x, np.sin(x), '-')
plt.plot(x, np.cos(x), '--');

```

```python
plt.plot(x, np.tan(x), '-') ;


```

```python
# plt.style.use('classic')
# temporarily set a style
with plt.style.context('classic'):
  with plt.style.context('seaborn-v0_8-pastel'):
    plt.plot(x, np.sin(x), '-')
    plt.plot(x, np.cos(x), '--')

```

```python
plt.plot(x, np.sin(x), '-')
plt.plot(x, np.cos(x), '--') ;

```

```python
plt.style.use('classic') # reset everything back to classic

```

```python
plt.plot(x, np.sin(x), '-')
plt.plot(x, np.cos(x), '--') ;

```

##  Seaborn



Seaborn is another commonly used plotting package in Python.
- Built on top of matplotlib
- Sets some better default settings
- Has additional plotting options

```python
import seaborn as sns
sns.set()
plt.plot(x, np.sin(x), '-')
plt.plot(x, np.cos(x), '--');
```

```python
# Seaborn dist plot
x = np.random.normal(0,1,1000)
sns.displot(
    x,
    color='green',
    kde = True,
    ) ;
```

### Your Turn


Create a seaborn violin plot using the `x` variable that was created in the previous example.

```python
sns.violinplot?
```

```python
# Solution
# Seaborn dist plot
x = np.random.normal(0,1,1000)
sns.violinplot(
    x,
    color='green',
    orient = "h",
    ) ;
```

## Pandas


Use the plot() method on the dataframe directly

```python
import pandas as pd

df = pd.DataFrame(
    np.random.randn(100, 4),
    index=pd.date_range('1/1/2000', periods=100),
    columns=list('ABCD'),
    )

df.head()
```

```python
df.shape

```

```python
# Plot all columns vs. index - just call plot()
df.plot();
```

```python
df[["A","B"]].plot();
```

Explicitly pass columns to matplotlib as values to plot

```python
plt.plot(df.index, df['A'])
plt.plot(df.index, df['B']) ;
```

```python
df.plot(
    x = 'A',
    y = 'B',
    kind='scatter',
)
plt.title('A and B') ;
```

```python
df2 = pd.DataFrame(np.random.rand(10, 4), columns=['a', 'b', 'c', 'd'])
df2.plot(kind='bar') ;
```

```python
df2
```

## Subplots

```python
# Some example data to display
x = np.linspace(0, 2 * np.pi, 400)
y = np.sin(x ** 2)

# Create subplot
fig, axs = plt.subplots(2)
axs[0].plot(x, y*2)
axs[1].plot(x, -y) ;
```

```python
type(axs[0])
```

```python
type(axs)
```

```python
axs.shape
```

```python
# 2 x 2 subplots
fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(x, y)
axs[0, 1].plot(x, y, 'purple')
axs[1, 0].plot(x, -y, 'green')
axs[1, 1].plot(x, -y, 'red') ;
```

```python
# adding labels and legends to subplots
fig, axs = plt.subplots(2, 2, figsize = (12,8))
colors = ['blue', 'purple', 'green', 'red']
labels = ['plot 1', 'plot 2', 'plot 3', 'plot 4']
n = 0
for i in range(2):
  for j in range(2):
    axs[i,j].plot(x, y, colors[n], label = labels[n])
    axs[i,j].legend()
    axs[i,j].set_xlabel('x')
    axs[i,j].set_ylabel('y')
    n += 1
```

```python
(axs).shape
```

```python
# adding labels and legends to subplots
fig, axs = plt.subplots(2, 2, figsize = (12,8))
colors = ['blue', 'purple', 'green', 'red']
labels = ['plot 1', 'plot 2', 'plot 3', 'plot 4']

subplots = axs.flatten()
for n, sp in enumerate(subplots):
  sp.plot(x, y, colors[n], label = labels[n])
  sp.legend()
  sp.set_xlabel('x')
  sp.set_ylabel('y')

```

```python
df.columns
```

```python
df.columns[2]
```

```python
# Subplot with pandas data frame
fig, axs = plt.subplots(4, figsize = (8,8))
for i, col in enumerate(df.columns):
  axs[i].hist(df[col], label = col )
  axs[i].legend()

```

```python
# Subplot with pandas data frame
fig, axs = plt.subplots(4, figsize = (8,8))
for i, sp in enumerate(axs.flatten()):
  sp.hist(df[df.columns[i]], label = df.columns[i])
  sp.legend()

```

### Your Turn

Create a 2x2 subplot of boxplots for each column in the `df` data frame.



```python
df = pd.DataFrame(
    np.random.randn(100, 4),
    index=pd.date_range('1/1/2000', periods=100),
    columns=list('ABCD'),
    )
```

```python
np.random.randn?
```

```python
df = pd.DataFrame(
    np.random.randn(100, 4),
    index=pd.date_range('1/1/2000', periods=100),
    columns=list('ABCD'),
    )
```

```python
df.head()
```

```python
# Solution
fig, axs = plt.subplots(2, 2, figsize = (20,16))
for i, sp in enumerate(axs.flatten()):
  sp.boxplot(df[df.columns[i]], label = df.columns[i])
  sp.legend()
  sp.set_xlabel(df.columns[i])

```

## References


Some parts of this notebook are from the [Data Science Handbook](https://learning.oreilly.com/library/view/python-data-science/9781098121211/) on [GitHub](https://github.com/jakevdp/PythonDataScienceHandbook/tree/master/notebooks).  This is a good resource if you want to dive in more.  

Also, the [matplotlib documentation](https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html#plotting-directly-with-matplotlib)

[Matplotlib gallery - 100s of examples](https://matplotlib.org/gallery.html)


## Homework

Take some time to make the plots in your project look good.  Make sure they have the seven items of a graph:

- chart title
- X-axis title
- Y-axis title
- X-axis tick labels
- Y-axis tick labels
- origin
- legend

In addition, look at how other people code their plots then deconstruct and reconstruct them.  That is, take them apart and put them back together line by line.



## stygian blue

"A [chimerical color]( https://en.wikipedia.org/wiki/Impossible_color#Chimerical_colors
 ) is an imaginary color that can be seen temporarily by looking steadily at a strong color until some of the cone cells become fatigued, temporarily changing their color sensitivities, and then looking at a markedly different color."




```python
import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots(figsize = (30,30))
rect = patches.Rectangle((0.1, 0.2), 0.5, 0.3, facecolor='#BEEF00')
ax.add_patch(rect)
ax.set_xlim(0.4, 0.5)
ax.set_ylim(0.4, 0.5)
plt.plot(0.45, 0.45, color='black', marker = '.', markersize=20)
plt.title('''
Center the image on your screen.
Stare at the center dot without moving your eyes for 30s.
Then cover your eyes with your hand and close them.
''')
plt.show()

```

```python

```
