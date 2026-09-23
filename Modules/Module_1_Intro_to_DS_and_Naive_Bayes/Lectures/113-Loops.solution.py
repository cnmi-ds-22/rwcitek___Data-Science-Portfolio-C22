# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.5
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown] id="Gct0z2jFTl3b"
# # Python Loops

# %% executionInfo={"elapsed": 7, "status": "ok", "timestamp": 1780945672985, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="UL6yn3NydmWi"
import time


# %% [markdown] id="tzINHixzMwSD"
# ## The Challenge
#

# %% [markdown] id="v-EiYaSqBcFu"
# We would like to print every element in a list.
#
# Specifically, given the list `['a', 'b', 'c', 'd']`, we would like this output:
#
# ```
# Hello, a
# Hello, b
# Hello, c
# Hello, d
# ```

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 17, "status": "ok", "timestamp": 1780945673005, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="qjeturwh483K" outputId="11770ac2-4f05-46ce-f90d-dc5b499da9f1"
mylist = ['a', 'b', 'c', 'd']
print(mylist)


# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 24, "status": "ok", "timestamp": 1780945673031, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="8b5SnR6Z48z-" outputId="4871a649-3ce9-4c41-8836-4be1a17700f6"
# one solution: use indexing
print(mylist)
print("Hello, " + mylist[0])
print("Hello, " + mylist[1])
print("Hello, " + mylist[2])
print("Hello, " + mylist[3])


# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 28, "status": "ok", "timestamp": 1780945673052, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="d6z28ZYuHywZ" outputId="6f273c7a-30e0-42aa-f195-01b0b6b90320"
# another solution: use indexing with an index variable
print(mylist)
i = 0 ; print("Hello, " + mylist[i])
i = 1 ; print("Hello, " + mylist[i])
i = 2 ; print("Hello, " + mylist[i])
i = 3 ; print("Hello, " + mylist[i])


# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 26, "status": "ok", "timestamp": 1780945673078, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="cGCjPSSWIO7N" outputId="6ad96c47-11b4-402d-8c36-105c0757d5a5"
# another solution: use indexing with a value variable
print(mylist)
letter = mylist[0] ; print("Hello, " + letter)
letter = mylist[1] ; print("Hello, " + letter)
letter = mylist[2] ; print("Hello, " + letter)
letter = mylist[3] ; print("Hello, " + letter)


# %% [markdown] id="Hubr3Z1f5MoC"
# But what if the list changes?

# %% colab={"base_uri": "https://localhost:8080/", "height": 245} executionInfo={"elapsed": 24, "status": "error", "timestamp": 1780945673142, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="b2r2o81E48wp" outputId="e009b72f-a103-4208-d2cc-401a4b7fee45"
# delete the last element
mylist = ['a', 'b', 'c', 'd']
mylist.pop()

print(mylist)
letter = mylist[0] ; print("Hello, " + letter)
letter = mylist[1] ; print("Hello, " + letter)
letter = mylist[2] ; print("Hello, " + letter)
letter = mylist[3] ; print("Hello, " + letter)


# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 38, "status": "ok", "timestamp": 1780945678437, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="kZuxgol248tX" outputId="bae6eafe-4f35-4591-8585-132f06dfbaf5"
# extend the list
mylist = ['a', 'b', 'c', 'd']
mylist.extend(["x","y"])

print(mylist)
letter = mylist[0] ; print("Hello, " + letter)
letter = mylist[1] ; print("Hello, " + letter)
letter = mylist[2] ; print("Hello, " + letter)
letter = mylist[3] ; print("Hello, " + letter)


# %% [markdown] id="PGJCytTkK-L3"
# What if the list is really large?
#

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 14, "status": "ok", "timestamp": 1780945678891, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="7ZNSvr6aLBop" outputId="e4ecb74c-883b-4a3a-ded5-b9d5c331faa8"
mylist_large = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")

print(mylist_large)
letter = mylist_large [0] ; print("Hello, " + letter)
letter = mylist_large [1] ; print("Hello, " + letter)
letter = mylist_large [2] ; print("Hello, " + letter)
letter = mylist_large [3] ; print("Hello, " + letter)
letter = mylist_large [4] ; print("Hello, " + letter)
letter = mylist_large [5] ; print("Hello, " + letter)
letter = mylist_large [6] ; print("Hello, " + letter)
letter = mylist_large [7] ; print("Hello, " + letter)
letter = mylist_large [8] ; print("Hello, " + letter)
letter = mylist_large [9] ; print("Hello, " + letter)
letter = mylist_large[10] ; print("Hello, " + letter)
letter = mylist_large[11] ; print("Hello, " + letter)
letter = mylist_large[12] ; print("Hello, " + letter)
letter = mylist_large[13] ; print("Hello, " + letter)
letter = mylist_large[14] ; print("Hello, " + letter)
letter = mylist_large[15] ; print("Hello, " + letter)
letter = mylist_large[16] ; print("Hello, " + letter)
letter = mylist_large[17] ; print("Hello, " + letter)
letter = mylist_large[18] ; print("Hello, " + letter)
letter = mylist_large[19] ; print("Hello, " + letter)
letter = mylist_large[20] ; print("Hello, " + letter)
letter = mylist_large[21] ; print("Hello, " + letter)
letter = mylist_large[22] ; print("Hello, " + letter)
letter = mylist_large[23] ; print("Hello, " + letter)
letter = mylist_large[25] ; print("Hello, " + letter)
letter = mylist_large[25] ; print("Hello, " + letter)
letter = mylist_large[26] ; print("Hello, " + letter)
letter = mylist_large[27] ; print("Hello, " + letter)
letter = mylist_large[28] ; print("Hello, " + letter)
letter = mylist_large[29] ; print("Hello, " + letter)
letter = mylist_large[30] ; print("Hello, " + letter)
letter = mylist_large[31] ; print("Hello, " + letter)
letter = mylist_large[32] ; print("Hello, " + letter)
letter = mylist_large[33] ; print("Hello, " + letter)
letter = mylist_large[34] ; print("Hello, " + letter)
letter = mylist_large[35] ; print("Hello, " + letter)
letter = mylist_large[37] ; print("Hello, " + letter)
letter = mylist_large[38] ; print("Hello, " + letter)
letter = mylist_large[39] ; print("Hello, " + letter)
letter = mylist_large[40] ; print("Hello, " + letter)
letter = mylist_large[41] ; print("Hello, " + letter)
letter = mylist_large[42] ; print("Hello, " + letter)
letter = mylist_large[43] ; print("Hello, " + letter)
letter = mylist_large[44] ; print("Hello, " + letter)
letter = mylist_large[45] ; print("Hello, " + letter)
letter = mylist_large[46] ; print("Hello, " + letter)
letter = mylist_large[47] ; print("Hello, " + letter)
letter = mylist_large[48] ; print("Hello, " + letter)
letter = mylist_large[49] ; print("Hello, " + letter)
letter = mylist_large[50] ; print("Hello, " + letter)
letter = mylist_large[51] ; print("Hello, " + letter)


# %% [markdown] id="_CcToAuI_Idn"
# Shortcomings with all these approaches:
# - If you modify the list, you also have to modify the code.
#   - That's merely tedious for small lists, but impractical for large lists.
# - Lots of repetitive code
#   - Ripe for bugs - "Copy pasta is not your friend."
#

# %% [markdown] id="Eyly_3H-Yntn"
# ## For-Loop

# %% [markdown] id="9RJme6aIVw0A"
# "The Python `for` statement iterates over the members of a sequence in order, executing the block each time." - python documentation

# %% [markdown] id="uYUqH7wGUjbk"
# ### Terminology

# %% [markdown] id="C-TsUuP-Scpv"
#
# - loop over: perform the same code on each element in a list, range, string, etc.
# - iterate over: the same thing as loop over
# - for loop: this is the code that actually loops over something.  An example of what this looks like is <br>
# ```
# for i in range(1,5):
#   print(i)
# ```
# - iterable: any object that can be iterated over.  For example, a list or range.
# - block: the section of code that is under the control of the for loop.
#

# %% [markdown] id="8xL8dTqyTnar"
# ### Uses: Why for loops are important
#

# %% [markdown] id="5RqXalZLVUIL"
# For loops are one of the most basic programming concepts.  They are extremely useful for repeating code multiple times for different values of an iterable.  
#
# A data scientist might use a for loop to perform an operation on each entry in a data set.  For example, checking to see if the entry matches certain requirements or replacing inconsistent abbreviations with something consistent.  

# %% [markdown] id="ciSZiUROa2hj"
# ### Iterating over a list

# %% [markdown] id="qngIxBTWPHnH"
# In Python, you can loop over a list directly.
#
# This code ...
#
# ```python
# 1 mylist = ['a', 'b', 'c', 'd']
# 2
# 3 print(mylist)
# 4 letter = mylist[0] ; print("Hello, " + letter)
# 5 letter = mylist[1] ; print("Hello, " + letter)
# 6 letter = mylist[2] ; print("Hello, " + letter)
# 7 letter = mylist[3] ; print("Hello, " + letter)
# 8
# ```
#
# becomes this code ...

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 115, "status": "ok", "timestamp": 1780945681169, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="OO6HwYJKXfWs" outputId="e1163c46-1f2a-4f39-ebf2-599133b9e1a5"
mylist = ['a', 'b', 'c', 'd']

print(mylist)
for letter in mylist:
  print("Hello, " + letter)


# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 17, "status": "ok", "timestamp": 1780945681188, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="-ira7DXkEgYd" outputId="7600be04-fc4f-4e93-8266-14ff8995dae3"
# if you shorten the list, you don't have to modify the code
mylist = ['a', 'b', 'c', 'd']
mylist.pop()

print(mylist)
for letter in mylist:
  print("Hello, " + letter)


# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 17, "status": "ok", "timestamp": 1780945681207, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="rnTa3ED1EgVH" outputId="9e58cf85-8787-4b6f-f970-82881fd2e805"
# if you extend the list, you don't have to modify the code
mylist = ['a', 'b', 'c', 'd']
mylist.extend(["x","y"])

print(mylist)
for letter in mylist:
  print("Hello, " + letter)


# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 16, "status": "ok", "timestamp": 1780945681224, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="6gmuXczZNFAg" outputId="cab5d0c6-e18c-44d9-8251-8a069c1f7617"
# if you have large lists, you don't have to duplicate the code
mylist_large = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")

print(mylist_large)
for letter in mylist_large:
  print("Hello, " + letter)


# %% [markdown] id="D_xgOCpH-2ke"
# With a for-loop, you can perform operations on each object in the list.

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 109, "status": "ok", "timestamp": 1780945682901, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="xSCEObZi-2Iq" outputId="428114e2-51c7-456a-eede-da86e5e46537"
# modify every element in the list
mylist = ['a', 'b', 'c', 'd']

for letter in mylist:
  letter_uc = letter.upper()
  print(letter_uc)


# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 16, "status": "ok", "timestamp": 1780945682919, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="7fIguY4iFv_h" outputId="c0dd8e1c-8a58-476f-ed0a-e048f6ac28f3"
print(mylist)

# %% [markdown] id="T_7SlNwc5TNj"
# ### Iterating backwards over a list

# %% [markdown] id="Z88L1ubT_Sju"
# Using slicing.

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 13, "status": "ok", "timestamp": 1780945684700, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="Wu4zBwY5YVSV" outputId="9a9fd163-5fd5-4868-8b01-77d265115b2c"
for letter in mylist[::-1]:
  print(letter)


# %% [markdown] id="5Ux7zNkj_UPT"
# Using a function.

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 16, "status": "ok", "timestamp": 1780945684718, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="761Evoy-FjR7" outputId="688d9db3-b6f4-46fa-c181-a3503dfe26d0"
reversed(mylist)

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 15, "status": "ok", "timestamp": 1780945684735, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="oGWxQs1N5cSy" outputId="5b00a47d-31b2-409a-c364-17075294e6a2"
for letter in reversed(mylist):
  print(letter)


# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 16, "status": "ok", "timestamp": 1780945684753, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="RtQcC5JG-iI8" outputId="bdf04983-6cae-4567-f1ca-1e001807f5b2"
mylist


# %% [markdown] id="NKG9qjd6_WCm"
# Using a method.

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 12, "status": "ok", "timestamp": 1780945684837, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="jU_nUUCK-rQ6" outputId="2188ab6a-a3b7-4f10-c0b0-6a02c9b7a3ea"
mylist.reverse()
for letter in mylist:
  print(letter)


# %% colab={"base_uri": "https://localhost:8080/"} id="p8G1AXEw3kvM" executionInfo={"status": "ok", "timestamp": 1780945686072, "user_tz": 360, "elapsed": 9, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="ac12fb67-0d88-4443-8181-a9b8f4742a14"
mylist


# %% colab={"base_uri": "https://localhost:8080/", "height": 176} executionInfo={"elapsed": 9, "status": "error", "timestamp": 1780945686083, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="IsTy1wEIGo1k" outputId="53b387db-5a38-4198-9e2a-3b32d8f89b84"
# does not work
for letter in mylist.reverse():
  print(letter)


# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 19, "status": "ok", "timestamp": 1780945686106, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="fHzNfbTx-zBQ" outputId="386d55d3-3e4a-4fc7-ca46-24331f1d3134"
mylist


# %% [markdown] id="FXGMTO9x4nyO"
# #### Your Turn
# 1. Create a list called `my_colors` that contains 5 different colors.
# 2. Use a ___for loop___ to print out the colors in alphabetical order.

# %% id="yS3DEA49458g" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780945687491, "user_tz": 360, "elapsed": 93, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="b96c270b-db00-45b1-d50e-63361f1283da"
# Solution 1
my_colors = "red orange yellow green blue".split()
my_colors


# %% id="AVOOUfp-4-4V" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780945687511, "user_tz": 360, "elapsed": 17, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="efa18996-5bc8-41dd-9b86-f535e7ad7539"
# Solution 2
for color in sorted(my_colors):
  print(color)


# %% id="TsK7VUKQKHSz" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780945687527, "user_tz": 360, "elapsed": 14, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="bf07f34d-7189-4164-f61c-ed22c43fc350"
# Solution 2
my_colors.sort()
for color in my_colors:
  print(color)


# %% [markdown] id="frosXQJKawjU"
# ### Iterating a set number of times with a range object

# %% [markdown] id="fx2wIRBiY8l3"
# **Using range**  
# range will return an iterable object.  
# `range(11)` returns the numbers 0 to 10  
# `range(5, 11)` returns the numbers 5 to 10  
# `range(10, 22, 2)` returns the even numbers between 10 and 20  
# `range(10, 0, -1)` returns the numbers from 10 to 1 (counts down through them)

# %% id="oLsl0Ydtbw7q" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780945688692, "user_tz": 360, "elapsed": 58, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="7d643dfe-c7d6-47de-8cc4-8eb55d736537"
range(11)


# %% id="-dIDTPZd72mv" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780945689644, "user_tz": 360, "elapsed": 193, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="3384533c-fa95-4cc8-9b5d-807fbe1b9930"
type(range(11))


# %% id="-gY-LkENZRSq" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780945689699, "user_tz": 360, "elapsed": 11, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="c1e90808-c110-44fe-fb2c-a98c24ba706e"
list(range(11))


# %% id="Nsa5c2bRYkpc" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780945690067, "user_tz": 360, "elapsed": 62, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="b8219865-2a14-443a-bb19-4c43ae4c8cea"
# range(5,11) -> 5, 6, 7, 8, 9, 10
for i in range(5,11):
  print(i)


# %% [markdown] id="uvsuCH-9-g-S"
# A range object is like a list, but with special properties.  
# - Like a list, you can slice a range object.
# - When you slice a list, you get back a list.  When you slice a range object, you get back a range object.  
# - Unlike a list, a range object has "lazy evaluation"; it provides the values as needed rather than creating all values first.
#

# %% id="y1JjxJHWCyxc" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780945691089, "user_tz": 360, "elapsed": 17, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="686e7070-448f-4b1d-852c-e2a322e8ddf7"
range(10)[0::2]

# %% colab={"base_uri": "https://localhost:8080/"} id="DXIBdH4lYecF" executionInfo={"status": "ok", "timestamp": 1780945692788, "user_tz": 360, "elapsed": 18, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="7f4466d2-35a3-4246-e308-cb67011dfd1e"
range(0, 10, 2)


# %% id="B5gYJ9lcC_WB" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780945692805, "user_tz": 360, "elapsed": 15, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="ce5db6f7-f0e8-46a4-a319-f2a8994dc150"
range(10)[::-1]

# %% id="vwD7S2QpFrzQ" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780945692822, "user_tz": 360, "elapsed": 15, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="a7a6b2cd-2b6e-470a-b5ef-7e2089f07a20"
range(1_000_000_000_000_000_000_000_000_000)[-10:]


# %% id="7duNSbAbad-g" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780945692839, "user_tz": 360, "elapsed": 16, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="f42e195e-b86b-452f-d6e0-799c2a22038c"
list(range(1_000_000_000_000_000_000_000_000_000)[-10:])

# %% id="BHP5wgudMZWe" colab={"base_uri": "https://localhost:8080/", "height": 159} executionInfo={"status": "error", "timestamp": 1780945692850, "user_tz": 360, "elapsed": 9, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="dd852d12-61d2-410d-c7c1-4f637c0eb75c"
# does not work
list(range(1_000_000_000_000_000_000_000_000_000))

# %% [markdown] id="sl0wxQ7C4EQB"
# #### Your Turn
# Use a range object in a for loop to print out the following numbers: 1,3,5,7,9,11,13

# %% colab={"base_uri": "https://localhost:8080/"} id="yxhnoxI7Zc-c" executionInfo={"status": "ok", "timestamp": 1780945694945, "user_tz": 360, "elapsed": 105, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="42892379-9b52-45f5-a289-9ad1aa07399e"
for i in range(1,14,2):
  print(i)

# %% id="mjs5o3wv4Sx1" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780945694965, "user_tz": 360, "elapsed": 17, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="4edf0a8a-d3d2-4677-d799-e862d47da35d"
# Solution
list(range(1,14,2))


# %% colab={"base_uri": "https://localhost:8080/"} id="AH5DRshxZHFr" executionInfo={"status": "ok", "timestamp": 1780945695017, "user_tz": 360, "elapsed": 15, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="623bd821-139e-45d9-cf64-203bda48a548"
list(range(1,14))[::2]


# %% colab={"base_uri": "https://localhost:8080/"} id="7egmgT2jZKkf" executionInfo={"status": "ok", "timestamp": 1780945695084, "user_tz": 360, "elapsed": 11, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="981c5d0c-a967-4561-e5d1-a92525e811d7"
list(range(1,14)[::2])


# %% [markdown] id="W5ncVU2sZmMS"
# ### Indexes in a for loop

# %% [markdown] id="gvumeBBCPT7r"
# `enumerate` is an iterator that will return the indexes and elements of a list or other iterable.
#

# %% id="lxknq6idJndO" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780945810758, "user_tz": 360, "elapsed": 53, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="a5af70f7-899a-4c31-db0e-1c0012189ec5"
alphas = ["a", "b", "c", "d" ]
alphas


# %% id="OaG7PsSMG0gu" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780945814162, "user_tz": 360, "elapsed": 58, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="cebadb49-ce14-4e12-8cc8-6bcf3ed8cf16"
enumerate(alphas)


# %% id="VIeHMz-xJrPb" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780945837228, "user_tz": 360, "elapsed": 55, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="afc7b32e-374a-4fd5-abff-21cc4f3cfede"
list(enumerate(alphas))


# %% id="bDE55qLCZoRL" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780945877415, "user_tz": 360, "elapsed": 60, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="ff80fb11-355a-4388-bd51-3a971c340ea2"
alphas = ["a", "b", "c", "d"]

for alpha in enumerate(alphas):
  print(alpha)
  print(type(alpha))


# %% id="5nOnjhcuD0cs" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780946152214, "user_tz": 360, "elapsed": 76, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="c4261f8d-edaf-446a-bae8-48cf7b7afaf2"
alphas = ["a", "b", "c", "d"]

for alpha in enumerate(alphas):
  print(alpha[0], alpha[1], alpha)
  print(type(alpha[0]), type(alpha[1]), type(alpha))


# %% id="mqNLR-3JDruw" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780946237949, "user_tz": 360, "elapsed": 47, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="25b1f20c-d601-492c-af73-1cee074df65b"
alphas = ["a", "b", "c", "d"]

for index, element in enumerate(alphas):
  print(index, element)


# %% id="7vepsPcfLnnd" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780946287666, "user_tz": 360, "elapsed": 76, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="7dc17500-549d-4604-a632-03780ac8e0ee"
alphas = ["a", "b", "c", "d"]

for index, element in enumerate(alphas):
  print(alphas[index], index, element)


# %% id="Rrvtjra2WYzX" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780946514554, "user_tz": 360, "elapsed": 86, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="77116670-1616-4582-deec-43d30e95ef8a"
alphas = ["a", "b", "c", "d"]
nums = [ 10, 20, 30, 40 ]

for index, _ in enumerate(alphas):
  print(index, alphas[index], nums[index])


# %% id="OH3t1QbxQNXi" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780947030396, "user_tz": 360, "elapsed": 168, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="93920b62-b677-4b8e-f8a1-8296e5d4a55b"
alpha_dict = dict(enumerate(alphas))
alpha_dict


# %% colab={"base_uri": "https://localhost:8080/"} id="Sk2jR5tBr6cz" executionInfo={"status": "ok", "timestamp": 1780947030486, "user_tz": 360, "elapsed": 85, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="27559e5b-1936-4267-ea1a-d1eea6074007"
alphas, alpha_dict

# %% colab={"base_uri": "https://localhost:8080/"} id="q895PpUWsD2i" executionInfo={"status": "ok", "timestamp": 1780947030503, "user_tz": 360, "elapsed": 13, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="b88746db-dfd9-4319-8515-8b816a15b217"
alphas[0], alpha_dict[0]

# %% colab={"base_uri": "https://localhost:8080/"} id="hcGdEaiwsDx5" executionInfo={"status": "ok", "timestamp": 1780947030526, "user_tz": 360, "elapsed": 20, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="c31ae361-8666-483c-cdaf-4b2e9b6c2117"
alpha_dict[-9] = "j"
alpha_dict

# %% colab={"base_uri": "https://localhost:8080/", "height": 35} id="7gxwGh8WsDto" executionInfo={"status": "ok", "timestamp": 1780947030540, "user_tz": 360, "elapsed": 10, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="0cc23ad2-403f-4cdc-9210-26e5b148dfe9"
alpha_dict[-9]

# %% colab={"base_uri": "https://localhost:8080/"} id="rm8Bf-CBtWI1" executionInfo={"status": "ok", "timestamp": 1780947033179, "user_tz": 360, "elapsed": 36, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="e499b5f7-9544-4e8f-9e1c-60f6671bd699"
sorted(alpha_dict.items())


# %% colab={"base_uri": "https://localhost:8080/", "height": 141} id="MdKAEm1jsZvy" executionInfo={"status": "error", "timestamp": 1780947043213, "user_tz": 360, "elapsed": 48, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="1697159f-9fbe-42bc-ed94-ea2d37cc8893"
alphas[-9] = "j"


# %% id="OT1ArHcIIbP5" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780947047040, "user_tz": 360, "elapsed": 43, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="dbdfd027-5edb-4dcc-c991-167f6e533f44"
list(enumerate(list("abcdefghijklmnopqrstuvwxyz"), start=-10 ))


# %% [markdown] id="YtT-3ykmyuMk"
# #### Your Turn
#
# 1. Create a list of everyone's name in the cohort and assign it to a variable called `students`.
# 2. Print out the index and name of each student in `students`.

# %% id="aEMxfEYyzEE0" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780947123861, "user_tz": 360, "elapsed": 69, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="6a614510-e586-4e87-ecd0-f847d34b4fc2"
# Solution 1
students = "John Paul George Ringo".split()
students


# %% id="7oUUBJ7GzF_v" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780947139658, "user_tz": 360, "elapsed": 46, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="023b2f46-8518-47ab-d4a4-04d1111b8335"
# Solution 2
list(enumerate(students))


# %% [markdown] id="3jANdmnmamby"
# ### Replicate elements

# %% [markdown] id="mIex8B3HIsk2"
# How a symbol works depends on context.

# %% id="1MQtxRKxaqhD" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780947668018, "user_tz": 360, "elapsed": 54, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="f1ceda6d-843a-479c-d57f-f20fcac59a6a"
1 * 5


# %% id="2m3RIP_m9tfY" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780947675046, "user_tz": 360, "elapsed": 14, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="63a943fc-bec7-49bd-c02a-2abb38b572a6"
1.0 * 5


# %% id="ly1RFLGPaleG" colab={"base_uri": "https://localhost:8080/", "height": 35} executionInfo={"status": "ok", "timestamp": 1780947691334, "user_tz": 360, "elapsed": 52, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="7afb84e1-41a3-41f5-dbd9-ea706eeee5d3"
"a" * 5


# %% id="Ipdrz_i5az37" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780947727527, "user_tz": 360, "elapsed": 56, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="af56c625-50e0-4b6b-bd8d-2f803298cb39"
[1] * 5


# %% id="fZiXzWcWJE0k" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780947739784, "user_tz": 360, "elapsed": 46, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="d40ebc62-ced1-4d2d-b438-c63e691e49a4"
[[1]] * 5


# %% id="pcVBbbb3a_0L" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780947777830, "user_tz": 360, "elapsed": 77, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="680fc521-9575-4c38-fea5-3503d244f54b"
even = ["even"] * 5
odd = ["odd"] * 5
( even, odd )


# %% id="37hdokxDTXfZ" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780947826994, "user_tz": 360, "elapsed": 57, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="20e5e088-9dec-4330-d111-4ce430feabd3"
list(zip(even,odd))

# %% id="cfu5uPE9bn47" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780947853445, "user_tz": 360, "elapsed": 61, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="9e6f1d2f-f396-47c3-f49d-0b92fe59d691"
["odd", "even"] * 5


# %% [markdown] id="WJU0XmG5KgoG"
# ### Slice assignment
#

# %% id="JK5hjdOFbMG1" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780947898906, "user_tz": 360, "elapsed": 89, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="3833cb7a-3b83-40f3-ca78-f4d48d1dd0a3"
odd_even = ["odd"] * 10
odd_even


# %% id="Nu3a9bTwst--" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780947903134, "user_tz": 360, "elapsed": 14, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="2a690907-d2a7-40ed-f169-559d8e3742d3"
even


# %% [markdown] id="gtMkEa8_P91l"
# Extended slice assignment
#

# %% id="PQaSWjmvsGt7" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780947932992, "user_tz": 360, "elapsed": 92, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="6531a2f6-a441-42a4-8c9a-a3da798b7ee4"
odd_even[1::2] = even
odd_even


# %% [markdown] id="XKR3h552ML9n"
# Slice and assignment lengths must be identical.
#

# %% id="VLgjpLhhuIxM" colab={"base_uri": "https://localhost:8080/", "height": 193} executionInfo={"status": "error", "timestamp": 1780948050220, "user_tz": 360, "elapsed": 97, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="52377b21-4396-4d23-cf1b-001a9777e482"
# does not work
even = ["even"] * 6
odd_even[1::2] = even
odd_even


# %% id="CSfQ6BaSL0iI" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780948099054, "user_tz": 360, "elapsed": 45, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="8a6e4712-9a80-4e74-8a4b-3c34648cb9b8"
# works
even = ["even"] * len(odd_even[1::2])
odd_even[1::2] = even
odd_even


# %% id="fSy-8AIvtLuw" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780948114760, "user_tz": 360, "elapsed": 72, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="173af356-eea4-4154-8152-a602a0243d67"
my_list = [ 1, 2, 3 ]
my_list


# %% id="uFxAzMqctbem" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780948120316, "user_tz": 360, "elapsed": 39, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="6cd3d3e2-2952-4278-d286-ac299351632e"
( my_list[0::2] ) =  ( 10, 20 )
my_list


# %% [markdown] id="4ZoLxusKKz_h"
# Iterable Unpacking, aka tuple unpacking or parallel assignment.

# %% id="RcBUTla7tFB-" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780948162896, "user_tz": 360, "elapsed": 55, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="f059b5c3-062a-4e66-c78f-9303e0eb0801"
( a, b, c ) = ( 1, 2, 3 )
[ a, b, c ]


# %% [markdown] id="r71IgWuELJgx"
# Extended Iterable Unpacking.
#

# %% id="ow-v0Gh3ToVg" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780948210472, "user_tz": 360, "elapsed": 80, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="a0b23d63-36a5-4ef7-91b7-149f21a5d2b1"
( a, b, *c ) = ( 1, 2, 3, 4, 5 )
[ a, b, c ]


# %% [markdown] id="-JIWmAxQOx8D"
# An implemenation of pop() using extended iterable unpacking.
#

# %% id="xDyzHYsEOxLP" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780948254687, "user_tz": 360, "elapsed": 80, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="7c3a4bf3-da48-4e69-c3dd-efc6ff471e22"
b = ( 1, 2, 3, 4, 5 )
( a, *b ) = b
( a, b )


# %% id="DkSSNTt-LSBF" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780948287694, "user_tz": 360, "elapsed": 133, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="ede7157c-a66e-4194-ab8b-447fd8e8ceaa"
( a, *b, c ) = ( 1, 2, 3, 4, 5 )
[ a, b, c ]


# %% [markdown] id="bhJG_SjtOBaI"
# Nested unpacking.
#

# %% id="NFGxOxufN_9s" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780948319432, "user_tz": 360, "elapsed": 68, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="ac8ff715-75c6-40f5-e0c6-1e221e09cf27"
(a, (b, c)) = [1, [2, 3]]
[a, b, c]


# %% [markdown] id="MDFH_9zibF31"
# ### Nested loops

# %% [markdown] id="HCC0037KPg-T"
# You can put loops inside of loops.  For example, to print out a multiplication table.
#

# %% id="WcNXT2PnVPqD" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780948474528, "user_tz": 360, "elapsed": 78, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="71eb8e0e-11c4-4105-fe4d-c25845665d28"
for x in range( 1, 6):
  for y in range( 1, 6):
    print(f'{x:2} * {y:2} = {x*y:2},', end = '\t')
  print()


# %% [markdown] id="VPMnrteGbfsJ"
# ### Iterating over a string

# %% [markdown] id="vmuQlT1AbbbQ"
# You can treat a string like a list.
#
# You can iterate over it.

# %% id="cegyvW2BbJKS" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780948576211, "user_tz": 360, "elapsed": 8997, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="a66f47d6-ca52-4249-c617-a4c3a1383d96"
cheer = "CNM Divers"
for letter in cheer:
  if letter != " ":
    print(f"Give me a '{letter}'")
    time.sleep(1)
print()
print(f"Go {cheer}!")


# %% [markdown] id="LmMb7MtJca8L"
# You can slice it.
#

# %% id="29Bay3KCWGJ3" colab={"base_uri": "https://localhost:8080/", "height": 35} executionInfo={"status": "ok", "timestamp": 1780948663145, "user_tz": 360, "elapsed": 50, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="ac3a4c1c-c307-453c-f1ba-cd9e24994129"
cheer[1:3]

# %% [markdown] id="rGb6uZn0zSlS"
# #### Your Turn
# 1. Create a counter variable `num_y` and set it equal to 0.
# 2. Create a for loop to loop through the letters in `happy birthday`. If the letter is a `y`, add `1` to your counter variable `num_y`.
# 3. Print out `num_y`.

# %% id="yucvnG1wzxlr" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780950277045, "user_tz": 360, "elapsed": 44, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="9b89bef1-df69-4621-f143-8c0df6db1ed7"
# Solution 1
num_y = 0
num_y


# %% id="w8_gE2QBzydf" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780950278793, "user_tz": 360, "elapsed": 12, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="43fed2aa-8234-47e8-cef4-ca7d98f8ab73"
# Solution 2
hb = "happy birthday"
for i in hb:
  if i == 'y':
    num_y = num_y + 1
num_y


# %% id="_xSuHHTOz0Jw" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780950222112, "user_tz": 360, "elapsed": 45, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="4956e408-a46d-4696-e1b4-70b7c3e70d26"
# Solution 3
print(num_y)


# %% colab={"base_uri": "https://localhost:8080/"} id="FBYZPknM3-ga" executionInfo={"status": "ok", "timestamp": 1780950117594, "user_tz": 360, "elapsed": 48, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="bd5cb1fb-79c5-4436-d3fa-50c0a7112bf4"
hb.count('y')


# %% [markdown] id="eE5rpxBEFbBP"
# ### Looping And Updating a List

# %% id="j8Eedsl3FfEl" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780950374809, "user_tz": 360, "elapsed": 75, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="ee70e1e7-46e9-4c22-81a1-6277b10e5fe0"
results = [] # Initialize the list
for i in range(11):
  results.append(i*2)
results


# %% id="WOuurOzyFxNZ" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780950460558, "user_tz": 360, "elapsed": 94, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="29ab0f05-48f2-402e-b4cc-4b36d646811d"
words = ['dog', 'cat', 'hello', 'wow!']
for index, word in enumerate(words):
  words[index] = word*2
words


# %% id="pQIYbJstcRsB" colab={"base_uri": "https://localhost:8080/", "height": 176} executionInfo={"status": "error", "timestamp": 1780950545633, "user_tz": 360, "elapsed": 55, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="9c14b10e-cf17-4cc4-c01d-945b3d844a01"
# Does not work - need to preassign
words = ['dog', 'cat', 'hello', 'wow!']
words_doubled = []
for index, word in enumerate(words):
  words_doubled[index] = word*2


# %% id="jEb6CWiL0mqq" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780950626198, "user_tz": 360, "elapsed": 67, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="1a41dcfe-2e50-4a58-f996-7413d90ad6e6"
# Works - need to preassign
words = ['dog', 'cat', 'hello', 'wow!']
words_doubled = [[]] * len(words)
words_doubled


# %% id="5d7JHG8KWtLJ" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780950668111, "user_tz": 360, "elapsed": 80, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="f3c45809-8c8c-47ef-e020-1ccfe5175937"
for index, word in enumerate(words):
  words_doubled[index] = word*2

words_doubled

# %% colab={"base_uri": "https://localhost:8080/"} id="X7qDC1hY7qVY" executionInfo={"status": "ok", "timestamp": 1780950679111, "user_tz": 360, "elapsed": 15, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="dd353210-b523-4683-fa6e-ea1f6eb03da4"
words

# %% [markdown] id="Lg7N9ow3GB9t"
# #### Your Turn
#
# 1. Create an empty list called `main_words`.
# 2. Create a second list called `small_words` that contains the words `'of', 'is', 'the', 'it' and 'a'`.
# 3. Create a variable called `sentence` and set it equal to the following string: `Data science is the best!`.
# 4. Loop through the *words* in your `sentence`. Note: you'll need to use the `split()` string method to loop through words instead of letters. If the word is **not in** `small_words` add it to your `main_words` list.

# %% colab={"base_uri": "https://localhost:8080/"} id="Wq8LeqYV8gZY" executionInfo={"status": "ok", "timestamp": 1780951243634, "user_tz": 360, "elapsed": 52, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="08a66827-ef6b-4c0b-f046-bb0bfd728c89"
# Solution 1
main_words = []
main_words


# %% colab={"base_uri": "https://localhost:8080/"} id="OiCMTf0j8gZZ" executionInfo={"status": "ok", "timestamp": 1780951252887, "user_tz": 360, "elapsed": 60, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="7989a1e8-a98c-47cc-9570-4fc66fddf954"
# Solution 2
small_words = ['of', 'is', 'the', 'it','a']
small_words


# %% colab={"base_uri": "https://localhost:8080/", "height": 35} id="RiGPMlPN8gZZ" executionInfo={"status": "ok", "timestamp": 1780951268795, "user_tz": 360, "elapsed": 13, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="03892592-a5b0-4ff9-8672-c86d1de184e3"
# Solution 3
sentence = "Data science is the best!"
sentence


# %% colab={"base_uri": "https://localhost:8080/"} id="3LsNwZ2i8gZZ" executionInfo={"status": "ok", "timestamp": 1780951298226, "user_tz": 360, "elapsed": 90, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="742f449c-d3aa-4b7d-c5ca-270058cec1d7"
# Solution 4
for word in sentence.split():
  if word not in small_words:
    main_words.append(word)

main_words


# %% [markdown] id="leOBfDBsP0Le"
# ### A Few More Examples

# %% [markdown] id="SvNXY6ijem1i"
# Count down from 10 to 1 and then Blast Off!!

# %% id="YutI79AaejXi" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780951862225, "user_tz": 360, "elapsed": 5004, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="e26a05c7-eeb5-4bf5-929e-c83f786f159f"
for i in range(5, 0, -1):
  print(i)
  time.sleep(1)

print('BLAST OFF!!')


# %% [markdown] id="HZtW8RJOzFG2"
# ### Calculating sum

# %% id="CLD0cFUIzEAn" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780951899557, "user_tz": 360, "elapsed": 50, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="6796fbf7-2dc2-4006-a2bb-a1c5d4b117eb"
numbers = list(range(0,100_000_001))
( numbers[:5], numbers[-5:] )


# %% id="ILmVge7D7CFI" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780951972302, "user_tz": 360, "elapsed": 7460, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="07e34b3a-3687-4ae8-9bf5-0c8f98fd8290"
sum1 = 0
for i in numbers:
  sum1 += i

sum1

# %% id="X2laWxOiXeCA" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780951998233, "user_tz": 360, "elapsed": 16, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="d6200d89-a85d-4034-f27e-f085c437ffc4"
sum(numbers)

# %% colab={"base_uri": "https://localhost:8080/"} id="pqrIy6i7BJM9" executionInfo={"status": "ok", "timestamp": 1780952113306, "user_tz": 360, "elapsed": 118, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="200f2427-02d3-4de8-a29e-dfbf678a6984"
help(len)

# %% id="fnm95RkWRx_C" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780952083487, "user_tz": 360, "elapsed": 59, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="0519d89f-367f-4c27-ed84-b020ee38daef"
# mean ( average )
sum1 / len(numbers)


# %% id="VYne8gC923JQ" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780952213761, "user_tz": 360, "elapsed": 51, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="ae5b293a-dfaa-4b4f-abeb-49a0cda98802"
# median ( midpoint value )
sorted(numbers)[len(numbers) // 2]


# %% [markdown] id="EHr3M608JE-d"
# ## While-loop

# %% [markdown] id="gSVk2e8nJJnf"
# Rarely use, but it does happen.  It's structure:
#
# ```python
# init = 0
# while condition:
#   do stuff
#   init += 1
# ```
#
# Variants:
# ```python
# init = 0
# while True:
#   do stuff
#   if condition: break
# ```
#
# ```python
# init = 0
# while True:
#   do stuff
#   if condition: break
#   do more stuff
# ```
#
# ```python
# init = 0
# while True:
#   if condition: break
#   do stuff
# ```
#

# %% id="D_v6NlK_JDci" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780952467043, "user_tz": 360, "elapsed": 84, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="82263f3d-0d6f-45f5-f7e3-6ffeed4b2538"
for init in range(10):
  print(init)


# %% id="QjmWqUm9JDtM" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780952484143, "user_tz": 360, "elapsed": 85, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="eadfedf9-3e7a-4ce8-a5f8-e86cbd1f796c"
# identical to previous for-loop
init = 0
while init < 10:
  print(init)
  init += 1


# %% [markdown] id="qamxYXB7YsqM"
# ## List comprehension

# %% [markdown] id="uZafXRzqNXrC"
# If you are going to create a list from an existing list, a list comprehension is a compact form of using `for-loops` to create lists.
#
# More generally, If you are going to create a collection from an existing collection, a list ( or other ) comprehension is a compact form of using `for-loops` to create collections.
#
#

# %% colab={"base_uri": "https://localhost:8080/", "height": 106} id="IE0AhSWbD2Ih" executionInfo={"status": "error", "timestamp": 1780952876463, "user_tz": 360, "elapsed": 149, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="f1ee7a03-16da-409a-b111-e0854fd7ab99"
foo = "
a
b
c
d
"
print(foo)

# %% colab={"base_uri": "https://localhost:8080/"} id="pcGhU_pBDhbm" executionInfo={"status": "ok", "timestamp": 1780952884517, "user_tz": 360, "elapsed": 61, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="1630c8cc-0a53-4875-f3b1-40320ffd10a2"
foo = '''
          a
          b
          c
          d
          e
          f
          g
          '''

print(foo)

# %% id="2hiGkiVgYyNt" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780952802841, "user_tz": 360, "elapsed": 59, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="9ae4ece9-f0b2-45e7-de51-703c0460c276"
letters = '''
          a
          b
          c
          d
          e
          f
          g
          '''.split()
letters


# %% id="achb1OEOaPF1" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780952917526, "user_tz": 360, "elapsed": 78, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="979c1e6f-3d05-48ec-8ea3-3e1e852f9d1f"
# for loop format to generate a list of double letters
doubles = []
for letter in letters:
  doubles.append(letter*2)
doubles


# %% id="mSlQ6xzrZ2Oz" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780952946972, "user_tz": 360, "elapsed": 52, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="cc1cf5e6-2e97-4231-e697-c5788646e001"
# list comprehension format to generate a list of double letters
doubles = [
  letter*2
    for letter in letters
]
doubles


# %% [markdown] id="miKIj29rN1lt"
# List comprehension is only used for generating lists.  Other operations, such as printing results, are generally not done with list comprehension.

# %% id="SpUz5velaiuA" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780953019300, "user_tz": 360, "elapsed": 61, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="c1cc3227-9dbd-463c-832e-f387378a4029"
# Correct way
for letter in letters:
  print("hello world: ", letter)


# %% id="zzzC2AjLV1o6" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780953029685, "user_tz": 360, "elapsed": 84, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="67093451-549c-4558-f299-8f02b0f6b5a0"
# Works, but generally not done
_ = [ print("hello world: ", letter) for letter in letters ]


# %% [markdown] id="aaQZyX52ODtx"
# List comprehension can also include conditionals.
#

# %% id="T8SWv_btbUq0" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780953069087, "user_tz": 360, "elapsed": 51, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="db310df1-2ac0-4283-de55-640fc4250c36"
# for loop format
beginning = []

for letter in letters:
  if letter in "aeiou":    # or list("aeiou")
    beginning.append(letter)

beginning


# %% id="UqQzeXZNbALn" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780953077172, "user_tz": 360, "elapsed": 50, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="206b6d8c-39c6-4e34-8861-c896aae34731"
# list comprehension format
beginning = [
  letter
    for letter in letters
      if letter in "aeiou"
]
beginning


# %% [markdown] id="4OtVQ9hFOT7q"
# One can also enumerate within a list comprehension.

# %% id="okWlvb-6bxuM" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780953122201, "user_tz": 360, "elapsed": 52, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="a5ecbdab-0912-4b23-f22b-bbbc56f56c38"
beginning = [
  ( i, x )
    for i, x in enumerate(letters)
      if x in "aeiou"
]

beginning


# %% id="MPm28gKef2IB"
