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

# %% [markdown] id="IcaWbwV0j9XY"
# #Conditionals
#

# %% [markdown] id="KFkU60DXl0MG"
# ## Why conditionals are important

# %% [markdown] id="oBa-MMfjl_Eq"
# Conditionals let us run code only under specific circumstances.  
#
# - For example, a website may want to show you certain content **if** you are logged in.  
#
# - As a data scientist, you may want to find the mean for a column of data **if** the column is filled with all numbers.  
#
#

# %% [markdown] id="T7xh4SRPp3gc"
# ## Vocabulary

# %% [markdown] id="7liIKj-np6jx"
#
# - **Conditions**: the thing we want to check before running the code
# - **If statement**: tell a program to execute different code depending if a condition is true.
#

# %% [markdown] id="cVoOq_P9j5ba"
# ##  True and False

# %% [markdown] id="E80jS4iomuWI"
# An if statement will run code if a particular condition is `True`.  So what is `True`?

# %% [markdown] id="J4mMsrgFkZ8B"
# Certain statements can be evaluated as `True` or `False`.  
# For example, `2 < 5` is `True`.  
# But ` 2 > 5` is `False`.  
#
# -  Statements of equality or inequality can be evaluated as True or False.  
# -  Variables can be set to equal True or False.
# -  Functions and methods can return values of True or False.  
# - 0 is False
# - "" is False
# - [] is False
#
#

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 30, "status": "ok", "timestamp": 1780591997544, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="GiUIJLZnWuVS" outputId="f4521b92-47c9-42d2-95e3-06fc0e4619b8"
2 == 5

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 48, "status": "ok", "timestamp": 1780592046340, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="CDc7CQ_ukOFe" outputId="51721ae8-836a-4440-d6c6-6d8c7cfce7bb"
# Statements of equality / comaprison
print(2 < 5)


# %% colab={"base_uri": "https://localhost:8080/"} id="Vh-SPevXjlFT" executionInfo={"status": "ok", "timestamp": 1780592052645, "user_tz": 360, "elapsed": 8, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="0cf584af-57fd-42ec-ae1f-74728336960b"
# To compare if two values are equal we use == instead of =.  (= assigns a variable)
print(2 == 5)


# %% colab={"base_uri": "https://localhost:8080/"} id="lAAWO7bAjlmM" executionInfo={"status": "ok", "timestamp": 1780592068352, "user_tz": 360, "elapsed": 32, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="487e345a-1ea3-4443-f3fa-b3c3a158ab0c"
# # ! negates a statement.  "Two is not equal to five."
print(2 != 5)


# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 35, "status": "ok", "timestamp": 1780592092903, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="6GE_wG9D3ZSM" outputId="d7f09fbc-d5bf-4992-cdbb-c2a06bd0040a"
x = 4
print(x<7)


# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 30, "status": "ok", "timestamp": 1780592195116, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="qw1CFvWukSUh" outputId="d3095cc7-d62c-4800-c526-022b2299910d"
x = True
print(x)


# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 31, "status": "ok", "timestamp": 1780592198698, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="cwAPo6UAn6c0" outputId="d0fa41b5-6525-4004-f4f0-b0b493565c53"
y = False
print(y)


# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 34, "status": "ok", "timestamp": 1780592203807, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="pXivOMbsXGj0" outputId="b53b8416-6636-43f8-8233-12ca7efd796e"
type(y)


# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 57, "status": "ok", "timestamp": 1780592232565, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="bJ3VVnsPoDDk" outputId="46924498-ca3b-445a-9574-db7964b8d99b"
mylist = ['a', 'b', 'c', 'd']
print('a' in mylist)
print('e' in mylist)


# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 27, "status": "ok", "timestamp": 1780592253734, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="M_GyCUq2ZTWl" outputId="f5335498-0e86-4705-efe9-893458530dc8"
# Locating a substring in a string works
"Mary".find("ry")

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 39, "status": "ok", "timestamp": 1780592275297, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="sbG39JYrGJfq" outputId="b74e91a8-0e83-4f4e-c8ae-69ca0183a301"
"Mary".find("c")

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 40, "status": "ok", "timestamp": 1780592286490, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="ioOqf836GJcr" outputId="266e7b6e-f82f-4c44-e4c0-43e095593a5f"
"Mary".find("M")

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 35, "status": "ok", "timestamp": 1780592404702, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="gpdyFcRJGJZd" outputId="370ce975-a8c9-43f9-86a6-56d898741acf"
"banana".find("a")

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 31, "status": "ok", "timestamp": 1780592437794, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="ONr6-cFNG_zx" outputId="3399db81-35c3-4fc0-de51-e97b8d8d1c35"
"Mary".find("cy")

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 45, "status": "ok", "timestamp": 1780592451737, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="rGmeP60XG_xg" outputId="bad00e3a-761e-4916-b532-84a7eab34b71"
"Mary".index("ry")

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 31, "status": "ok", "timestamp": 1780592456783, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="OJEZQ5j8G_vP" outputId="c0fe7d1d-1da6-4e4b-d0c0-999b42ac892c"
"banana".index("an")

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 36, "status": "ok", "timestamp": 1780592502359, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="U6jnXkafG_tQ" outputId="d30d43a1-61f0-49e4-bc4b-731adc6518d2"
"banana".count("a")


# %% colab={"base_uri": "https://localhost:8080/", "height": 141} executionInfo={"elapsed": 71, "status": "error", "timestamp": 1780592522000, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="Cgy0Y5tjG_qQ" outputId="ea16b3ac-629d-417d-9d75-64a78862f78e"
"Mary".index("c")


# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 31, "status": "ok", "timestamp": 1780592623503, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="3pVPVpoRGJXD" outputId="c10c58be-c795-42a9-afcb-bed47d3d37a6"
help(2.0.is_integer)


# %% colab={"base_uri": "https://localhost:8080/"} id="I4kvwbKtm5m9" executionInfo={"status": "ok", "timestamp": 1780592912451, "user_tz": 360, "elapsed": 18, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="626820a9-673d-49af-b813-1e58b0e35505"
type(2.1)

# %% colab={"base_uri": "https://localhost:8080/"} id="zh56hy8Hl7R2" executionInfo={"status": "ok", "timestamp": 1780592772254, "user_tz": 360, "elapsed": 34, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="3033e74e-9e5a-4935-d6a2-0ceb95026e7a"
(2.1).is_integer()


# %% colab={"base_uri": "https://localhost:8080/"} id="mE6Swhk5moPx" executionInfo={"status": "ok", "timestamp": 1780592971682, "user_tz": 360, "elapsed": 32, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="b8739845-0503-4761-b8bf-3361ac71848b"
int(2.1) == 2.1

# %% colab={"base_uri": "https://localhost:8080/"} id="HTne4Ni6mrAA" executionInfo={"status": "ok", "timestamp": 1780592852212, "user_tz": 360, "elapsed": 40, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="03faeece-42f0-48b6-dced-bae2fd9c6985"
type(2.0)

# %% colab={"base_uri": "https://localhost:8080/"} id="d5QGm6SvnOvF" executionInfo={"status": "ok", "timestamp": 1780593043540, "user_tz": 360, "elapsed": 34, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="eb5fbd42-1a4b-4065-959a-04b1438b2a2d"
a = 2.1
int(a) == a

# %% colab={"base_uri": "https://localhost:8080/"} id="ukUIhRiCmZuy" executionInfo={"status": "ok", "timestamp": 1780592783154, "user_tz": 360, "elapsed": 28, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="ffe443b6-20ed-42d2-9cb8-028d29d89ddb"
(2.0).is_integer()


# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 27, "status": "ok", "timestamp": 1780592790723, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="RqXzgr1XGJUH" outputId="74df7623-493f-42a7-c2c3-6ee8888eca18"
2==2.0

# %% colab={"base_uri": "https://localhost:8080/"} id="Mm0DuQeFn2I6" executionInfo={"status": "ok", "timestamp": 1780593159703, "user_tz": 360, "elapsed": 67, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="d6570295-6ae3-4521-eb78-b2c93e439d73"
mylist


# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 36, "status": "ok", "timestamp": 1780593150785, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="j-qMCxonXhrW" outputId="88df536e-dc61-44c7-cc43-5a6251a355c3"
# For a list, use .index()
mylist.index("c")


# %% colab={"base_uri": "https://localhost:8080/", "height": 141} executionInfo={"elapsed": 32, "status": "error", "timestamp": 1780593166572, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="dC8yUe8HJayj" outputId="061d6550-1d9b-4e56-800e-785cbd4ec8a3"
mylist.index("e")


# %% colab={"base_uri": "https://localhost:8080/", "height": 141} id="aIyVqgB7n51f" executionInfo={"status": "error", "timestamp": 1780593182266, "user_tz": 360, "elapsed": 158, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="ba4ca7e6-4da9-41ff-cea3-4c854b05f384"
mylist.find("c")


# %% [markdown] id="nlqtAHoR8Qzh"
# ### Your Turn
# Check to see if the following statements will return `True` or `False`:
# 1. `10 >= 5`
# 2. `10 >= 10`
# 3. `'dog' in ['cat', 'mouse', 'rabbit']`

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 33, "status": "ok", "timestamp": 1780594268946, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="untuOCjs8k6g" outputId="5c4dd93d-b027-4ba8-ef5d-b5cef4809195"
# Solution 1


# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 34, "status": "ok", "timestamp": 1780594289467, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="ZdZ6O18Y8lot" outputId="a4bee120-beda-4199-be43-00d9a3445a4a"
# Solution 2


# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 13, "status": "ok", "timestamp": 1780594296126, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="SRWHO_Hd8mcC" outputId="288ee1d2-aaf7-497c-87ad-1886ccad8bd5"
# Solution 3


# %% [markdown] id="jBjaOQ_rpmv9"
# ## If statements

# %% [markdown] id="K2F9uKeRpova"
# If statements execute code *if* a condition is true.  
#
# ```python
# # The format is
# if ( condition ):
#   code to run
# ```

# %% id="4mZmFRyhqvFb"
x = 2
y = 1
if (x < y):
  print('x is less than y')


# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 39, "status": "ok", "timestamp": 1780594467863, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="6WOOw2aOq4fO" outputId="68ca4316-0cb7-4647-b743-b50c0cb330fe"
x = 4
y = 5
if (x < y):
  print('x is less than y')


# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 45, "status": "ok", "timestamp": 1780594500060, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="x6H7Wr2dq9AN" outputId="82eeff99-bc28-4909-f28c-ffd93237f3db"
mypets = ['cat', 'rat', 'bat']
if ('cat' in mypets):
  print('I have a cat')


# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 69, "status": "ok", "timestamp": 1780594569265, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="MDqzYI70rUWF" outputId="142ed4e8-55ef-47a5-9e53-547692ed715d"
# example of idempotency
if ('goldfish' not in mypets):
  mypets.append('goldfish')

print(mypets)


# %% id="C23u6-2_Buks" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780594606158, "user_tz": 360, "elapsed": 9, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="f56e4d87-b35e-4fb4-8a5c-44e7a0318ed2"
x = [ 1 , 2, 3, 4 ]
2 in x

# %% [markdown] id="YweomZ1F88Da"
# ### Your Turn
# 1. Create a variable called `num_1` and assign it a value of 10. Create a variable called `num_2` and assign it a value of 20.
# 2. Write an if statement that will print out "Number 2 is larger" if `num_2` is greater than `num_1`. Run this code.
# 3. Create a list with 4 of your favorite foods and save it as `fave_foods`. Write an if statement that will print out `pizza` if it is in `fave_foods`.

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 37, "status": "ok", "timestamp": 1780595025386, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="gxCtj7oS9z4U" outputId="658f2810-17fe-47c6-cf8c-7d8cefde6922"
# Solution 1


# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 41, "status": "ok", "timestamp": 1780595061234, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="xm35lJBH90oK" outputId="dd7c6393-9a39-4def-e112-20c90bbb4a16"
# Solution 2


# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 28, "status": "ok", "timestamp": 1780595138615, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="keAsWOKY91co" outputId="52865129-b740-4d0a-d73b-837a2fdb1b39"
# Solution 3


# %% [markdown] id="HE6tp7b8seNu"
# ##  Indentation matters!

# %% [markdown] id="C43hFlQWshFX"
# Lines of code under an if statement will be run as part of the if statement *if* they are indented.  
#
# The first line of code that is NOT indented will NOT be included in the if statement.  
#

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 27, "status": "ok", "timestamp": 1780595614065, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="CjjYnuUTEzHB" outputId="21376df8-d107-486b-c4be-1700effeb4fa"
mypets

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 47, "status": "ok", "timestamp": 1780595697802, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="32KGvcvDre1l" outputId="f8bcef7c-1552-4ad4-c5ed-cd5cb06d083c"
# This will print mypets no matter what
if ( 'goldfish' not in mypets ):
  mypets.append('goldfish')
print(mypets)


# %% id="6mYeZvvys6Tw"
# This will print mypets only if 'goldfish' not in mypets
if ( 'goldfish' not in mypets ):
  mypets.append('goldfish')
  print(mypets)


# %% [markdown] id="9B0rngZFtJGQ"
# ## If else

# %% [markdown] id="gfPnl6qOtLdI"
# Sometimes we want to do one thing if a condtional is true and another thing if it's false.  
#

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 30, "status": "ok", "timestamp": 1780599823801, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="EvjIdGMdtGM9" outputId="d56cdbe2-2079-43b1-ffde-245218b370c1"
x = 4
y = 2

if (x < y):
  print('x is less than y')
else:
  print('x is not less than y')


# %% [markdown] id="_Rfm4W8996uE"
# ### Your Turn
# Write an if else statement that will print out `I love pizza` if `pizza` is in your `fave_foods` list; otherwise it will print out `I do not love pizza`.

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 31, "status": "ok", "timestamp": 1780600014371, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="vnnzzGwgNQlc" outputId="fe52678c-f1f3-45c2-f836-f87d2fbfacac"
fave_foods

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 54, "status": "ok", "timestamp": 1780600022478, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="Wx3XbRsJ-NdA" outputId="22b2b62d-b5d6-487b-feb4-6282736e6147"
# Solution 1


# %% [markdown] id="gDi9jRZwtg7R"
# ## Elif

# %% [markdown] id="G8Kn3YlOtize"
# elif - short for else if
#
# Used if we have multiple scenarios
#
# This example uses one elif, but you could have more than one

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 13, "status": "ok", "timestamp": 1780600407476, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="LkdsqgmQtdvD" outputId="5553722c-e187-4d57-a376-5c044cd854d8"
x = 6
y = 8

if (x < y):
  print('x is less than y')
elif (x == y):
  print('x equals y')
else:
  print('x is not less than y')


# %% [markdown] id="HDCIfHzp-UrE"
# ### Your Turn
# 1. Create a variable called `num_pets` that is equal to the number of pets you have.
# 2. Write an if-elif-else statement that does the following:
# - Prints out "I have a ton of pets!" if `num_pets` is larger than 5.
# - Prints out "I have a few pets" if `num_pets` is greater than 0 but less than or equal to 5.
# - Prints out "I have no pets" if `num_pets` is zero.
# Run your code using different values for `num_pets` to make sure it works as expected.

# %% colab={"base_uri": "https://localhost:8080/"} id="SMD7d_4NEJjD" executionInfo={"status": "ok", "timestamp": 1780600815793, "user_tz": 360, "elapsed": 32, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="29890d80-d8e7-4243-a9b7-420af42eeb71"
# Solution 1


# %% colab={"base_uri": "https://localhost:8080/"} id="8cAqs5WiEJjE" executionInfo={"status": "ok", "timestamp": 1780600816173, "user_tz": 360, "elapsed": 72, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="c7ec80ef-1ad0-4d11-b462-e1d62dfa0ca8"
# Solution 2


# %% [markdown] id="8piqK-1NSyTW"
# ## Match-case
#

# %% [markdown] id="3Bopc9pvS64s"
# It's like a cleaner if-elif-else under the right circumstances.
#

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 15, "status": "ok", "timestamp": 1780601637995, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="IlzhN3SKS0ra" outputId="6dee2ed7-8fd8-4e2a-f654-d8a40f81d501"
status_code = 200
message = ""

match status_code:
  case 200:
    message = "Success!"
  case 400 | 404:
    message = "Client Error"
  case 500:
    message = "Server Error"
  case _:
    message = "Unknown Status"

print(message)


# %% [markdown] id="64X9uN7eUBDk"
# Previous example of if-elif-else.
#
# ```python
# x = 6
# y = 6
#
# if (x < y):
#   print('x is less than y')
# elif (x == y):
#   print('x equals y')
# else:
#   print('x is not less than y')
# ```
#

# %% [markdown] id="35cTin_yUw5R"
# Using Guards, i.e. conditionals within the case statement.
#

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 37, "status": "ok", "timestamp": 1780601693381, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="iPsbDmBgS1O7" outputId="bc5486f4-c4c9-488a-ed3e-7f652b982169"
x = 6
y = 6

match (x, y):
  case (x, y) if x < y:
    print('x is less than y')
  case (x, y) if x == y:
    print('x equals y')
  case _:
    print('x is not less than y')


# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 48, "status": "ok", "timestamp": 1780601733321, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="0o4sIVEDS1J-" outputId="5cb7b6a5-4cc6-48cb-a586-313e02e4a830"
# Matching the result of a comparison directly
x = 4
y = 6

match (x > y, x < y):
  case (False, True):
    print('x is less than y')
  case (False, False):
    print('x equals y')
  case (True, False):
    print('x is not less than y')
  case _:
    print("How did I get here?")


# %% [markdown] id="MM6qmUYiun0I"
# ## Shorthand

# %% [markdown] id="-457nomnuq-X"
# If your if statement only has one line of code, you can put everything on one line.
#
#

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 65, "status": "ok", "timestamp": 1780601774152, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="IrFSU52bN430" outputId="db537dbe-f168-48b6-c028-80dceabb152a"
person = 2
if (person < 3):
  print('Person is a toddler!')

# %% [markdown] id="cxlsCPUtN9Q-"
# The same as a one-liner.

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 11, "status": "ok", "timestamp": 1780601780248, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="vAwwpf5tux2c" outputId="8404ccd7-27da-48fb-fa8e-8e891ed27ff4"
person = 2
if (person < 3): print('Person is a toddler!')

# %% [markdown] id="U8dBt_5IvG-B"
# if else statements can also go on one line

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 34, "status": "ok", "timestamp": 1780601817907, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="XPvFhdQ9NYII" outputId="9f8cb763-7b72-4748-e0fe-8dd69a373c38"
person = 4
if (person < 3) :
  print('Person is a toddler!')
else:
  print('Person is not a toddler!')

# %% [markdown] id="SbwcPKoNOBzw"
# The same as a one-liner.  Notice the placement of the code block of the "if" portion.  Also, notice there are no colons.

# %% id="MxHl14Gau--3" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780601842382, "user_tz": 360, "elapsed": 51, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="a48a3a5b-924e-4472-c78e-08b653a37855"
person = 4
print('Person is a toddler!') if (person < 3) else print('Person is not a toddler!')


# %% [markdown] id="KZq6YnF5TPmY"
# ### Using a one-liner as a ternary operator ( function )
#
#

# %% [markdown] id="Etr8BmJaTPmz"
# In most languages, a ternary function looks like this:
# ```
# ( condition ) ? value_if_true : value_if_false
# ```
#
# Excel and Google Sheets have the `=IF()` function, which does that same thing.
#
# ```
# =IF(condition, value_if_true, value_if_false)
# ```
#
# In Python, we can use the short-hand `if...else` statement as a ternary function, but move around the terms:
# ```
# value_if_true if ( condition ) else value_if_false
# ```
#

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 33, "status": "ok", "timestamp": 1780602100281, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="Y8TtZ2hLX_zS" outputId="2d6fed0d-c841-413f-cdfc-d713851113e6"
# traditional if-else
skies = "Cloudy"
skies = "Sunny"

if ( skies == "Sunny" ):
  weather = 5
else:
  weather = 2
weather


# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 17, "status": "ok", "timestamp": 1780602167706, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="hmZkPFmcTPm0" outputId="c7a8a75f-5edc-4c0d-c56b-d173e03b8ed1"
skies = "Cloudy"
skies = "Sunny"

weather = 5 if ( skies == "Sunny" ) else 2
weather


# %% [markdown] id="H2zm0NNk_wd1"
# ### Your Turn
# Write a one-line if statement of your choice.

# %% colab={"base_uri": "https://localhost:8080/", "height": 36} id="NkEyQdgrKh0F" executionInfo={"status": "ok", "timestamp": 1780602546501, "user_tz": 360, "elapsed": 46, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="ad8c9c95-0ed2-48c6-8321-f6ad2f29a57f"
# Solution




# %% [markdown] id="zJUEX-7yvo4P"
# ## `And` and `Or`

# %% [markdown] id="ZxbGjuaXvsYU"
# Conditions can be combined using `and` and `or`.  
#
# - For example, maybe a webpage wants to display certain content if you are a paying member and you're logged in.  
#
# - Or as a data scientist you want to classify a response as positive if it is 'good' or 'great'

# %% [markdown] id="O2rwGswzwHLe"
# A condition using `and` is true only if both sides are true.  
# A condition using `or` is true if at least one side is true or both sides are true.

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 15, "status": "ok", "timestamp": 1780604657487, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="JfGfpG-PvW82" outputId="9ed43707-5d50-42b8-8832-2afa8cd6b837"
member = True
logged_in = False

if ( ( member == True ) and ( logged_in == True ) ):
  print("Welcome member!")
else:
  print("Go Away!")


# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 53, "status": "ok", "timestamp": 1780604758798, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="L0dmlKBJP0l_" outputId="0cd4dbff-0957-4cec-a2a5-3185bbed8ef3"
member = True
logged_in = True

if ( ( member ) and ( logged_in ) ):
  print("Welcome member!")
else:
  print("Go Away!")

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 55, "status": "ok", "timestamp": 1780604810500, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="TVhOAdP9wj8W" outputId="c2a637dd-0e2e-4c46-bbb7-d904b9a3e720"
response = 'GoOd'
if ( (response.lower() == 'good') or (response == 'great') ):
  print('response was positive!')
else:
  print("Hmmm.  Bummer")

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 35, "status": "ok", "timestamp": 1780604847362, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="DexdtLSZWwPc" outputId="a2ce8f27-0306-40ab-f933-e1ab03370287"
response = 'great'
if ( (response.lower() == 'good') or (response == 'great') ):
  print('response was positive!')
else:
  print("Hmmm.  Bummer")


# %% [markdown] id="1U9-FsOY_9RZ"
# ### Your Turn
# 1. Create a variable called `cook` and set it equal to `True` if you like to cook and `False` if you do not. Create a variable called `clean` and set it equal to `True` if you like to clean dishes and `False` if you do not.
# 2. Write an if-elif-else statement that will do the following:
# - Print out "I like to cook & clean dishes!" if `cook` and `clean` are both `True`.
# - Print out "I like to cook!" if `cook` is `True` and `clean` is `False`.
# - Print out "I like to do dishes!" if `cook` is `False` and `clean` is `True`.
# - Print out "I'd rather order takeout." if `cook` is `False` and `clean` is `False`.
# Test out your code with different values for `cook` and `clean` to make sure it works as expected.
#

# %% colab={"base_uri": "https://localhost:8080/"} id="WiP1rQqRUyhe" executionInfo={"status": "ok", "timestamp": 1780605399627, "user_tz": 360, "elapsed": 54, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="7fee4e32-5af3-4e54-fba5-a3579e615a54"
# Solution 1


# %% colab={"base_uri": "https://localhost:8080/"} id="zUAxSpJSUyhf" executionInfo={"status": "ok", "timestamp": 1780605400962, "user_tz": 360, "elapsed": 35, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="f150d29a-5e58-4087-cfa1-c2ad71f6b6d5"
# Solution 2



# %% [markdown] id="48k5Du3g8JH_"
# ## Functions any() and all()

# %% [markdown] id="LNDhEkaQ8Oot"
# `any()`: Applies OR to a list of elements.  Only one element needs to evaluate to `True`.
#
# `all()`: Applies AND to a list of elements. All elements need to evaluate to `True`.

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 45, "status": "ok", "timestamp": 1780605524929, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="_pRApvk08kUr" outputId="50d177a9-7389-4cad-9714-3694b2a45a16"
values = [ True, False, False ]
any(values)


# %% colab={"base_uri": "https://localhost:8080/"} id="BHkrQcHwYbpZ" executionInfo={"status": "ok", "timestamp": 1780605970497, "user_tz": 360, "elapsed": 44, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="8fbff26c-8370-448b-ccfc-e7967b55f88a"
values = [ False, False, False, '', 1 ]
any(values)


# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 51, "status": "ok", "timestamp": 1780605547408, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="zol-hLmt8rgz" outputId="7a62fbd0-d5fe-4e27-a4cc-8a1456321fe3"
values = [ True, False, False ]
all(values)


# %% colab={"base_uri": "https://localhost:8080/"} id="idWZ-L4hXosf" executionInfo={"status": "ok", "timestamp": 1780605715154, "user_tz": 360, "elapsed": 34, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="4d9382c9-f134-4408-a6c9-307ce133ec8f"
values = [ 5<8, 6==6, 5>2]
all(values)


# %% colab={"base_uri": "https://localhost:8080/"} id="fc14oY1ZXoos" executionInfo={"status": "ok", "timestamp": 1780605792639, "user_tz": 360, "elapsed": 53, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="7e12a06a-bbf1-4f11-f585-67059afa3412"
a = ( 5<8 )
b = ( 6==6 )
c = ( 5>2 )
values = [ a, b, c ]
all(values)


# %% id="er4FGFZ5XolY"

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 43, "status": "ok", "timestamp": 1780606055759, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="k4cilKlEHivK" outputId="307825d7-7393-4386-c065-2f7c75af9d59"
cook = True
clean = True
conditions = ( cook, clean, )
print( conditions )

# Example from previous exercise
if ( all( conditions ) ):
  print("I like to cook & clean dishes!")
elif ( all( [ ( cook ), ( not clean ) ] ) ):
  print("I like to cook!")
elif ( ( not cook ) and ( clean ) ):
  print("I like to do dishes!")
elif ( not any( [ cook, clean ] ) ):
  print("I'd rather order takeout.")
else:
  print("And you may ask yourself, 'Well, how did I get here?'.")


# %% [markdown] id="_76gjap-c64M"
# # Boolean types
#
#

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 66, "status": "ok", "timestamp": 1780606257497, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="9t3YhZTVdCn_" outputId="210f7d5a-3855-4cc6-a335-a400d7eeba0e"
# boolean types can be converted to integers
True + 0


# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 50, "status": "ok", "timestamp": 1780606264163, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="nMnPjCspdClk" outputId="f5901f09-adc7-4584-cbdc-81bf23a19a2b"
False + 0

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 13, "status": "ok", "timestamp": 1780606275387, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="ksly6X8ExOVE" outputId="afc42703-06b2-4b18-c34b-b785e7c96e7a"
True * 1.0

# %% [markdown] id="d5lp8mPBYvZe"
# We can use a conditional as an index to a list of two elements.
#

# %% colab={"base_uri": "https://localhost:8080/", "height": 36} executionInfo={"elapsed": 68, "status": "ok", "timestamp": 1780606384019, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="mYOanROfdCi2" outputId="55d0d538-66f1-4d60-cdbd-ef866ab6f33a"
["hello", "good bye"][5 > 6]


# %% colab={"base_uri": "https://localhost:8080/", "height": 36} executionInfo={"elapsed": 88, "status": "ok", "timestamp": 1780606336874, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="By50TP2gdCgE" outputId="d929f141-4b1d-483f-adaa-72ddef1d240f"
["hello", "good bye"][5 < 6]


# %% [markdown] id="bHjEcdidRIbS"
# # DeMorgan's law

# %% [markdown] id="oz_wIvqiRKvk"
# [DeMorgan's Law]( https://en.wikipedia.org/wiki/De_Morgan%27s_laws )
#
# - not ( A and B ) <=> ( not A ) or ( not B )
# - not ( A or B ) <=> ( not A ) and ( not B )

# %% [markdown] id="djtbAfwTR7MA"
# ## Boolean Algebra and Truth Tables

# %% [markdown] id="Xp03XaiBR_Nb"
# [Boolean Algebra]( https://en.wikipedia.org/wiki/Boolean_algebra#Operations )
#
# [Truth Tables]( https://en.wikipedia.org/wiki/Truth_table )

# %% [markdown] id="QhEXXlMYtbgJ"
# ## Elaborating on help
#

# %% id="dLZzDE4qSMFr" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780929115313, "user_tz": 360, "elapsed": 38, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="4262365c-9106-4181-dbb9-4efbc85b6ab2"
foo = [1, 2, 3]
foo


# %% colab={"base_uri": "https://localhost:8080/"} id="lt-fpqMzpbN3" executionInfo={"status": "ok", "timestamp": 1780929119919, "user_tz": 360, "elapsed": 40, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="919b4c2e-0895-4e94-d455-6b8a3bf2c1a0"
help(foo)

# %% colab={"base_uri": "https://localhost:8080/"} id="TP-xK92BpcV-" executionInfo={"status": "ok", "timestamp": 1780929223487, "user_tz": 360, "elapsed": 46, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="8956f8de-a9be-4406-a8d6-3228baa6579a"
help(foo.clear)

# %% colab={"base_uri": "https://localhost:8080/"} id="pzgrdJz9p1n3" executionInfo={"status": "ok", "timestamp": 1780929458502, "user_tz": 360, "elapsed": 15313, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="ec8e8d18-678a-4dad-92ac-1ddebf546473"
help()

# %% colab={"base_uri": "https://localhost:8080/", "height": 35} id="ohfEgO_oqrQL" executionInfo={"status": "ok", "timestamp": 1780929618527, "user_tz": 360, "elapsed": 39, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="6fe883de-d9ad-451e-a89a-9f3732e0deb1"
str.removesuffix("goodbye", "bye")


# %% colab={"base_uri": "https://localhost:8080/", "height": 35} id="FXc3FYP8sblw" executionInfo={"status": "ok", "timestamp": 1780929919999, "user_tz": 360, "elapsed": 30, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="481f0db2-75a3-470e-f0cb-6828de6703b1"
"goodbye".removesuffix("bye")


# %% colab={"base_uri": "https://localhost:8080/"} id="dzrgKuJ2rCfN" executionInfo={"status": "ok", "timestamp": 1780929707378, "user_tz": 360, "elapsed": 52, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="8b756cec-d78c-4cab-bfe2-b792c7a76e06"
help("goodbye".removesuffix)

# %% colab={"base_uri": "https://localhost:8080/"} id="ncgRQJAArg1x" executionInfo={"status": "ok", "timestamp": 1780929801431, "user_tz": 360, "elapsed": 73, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="8dfd8186-178b-4bd8-c374-d9cb04cc1241"
help("goodbye".removesuffix)

# %% id="4QPHP610r1VK"
