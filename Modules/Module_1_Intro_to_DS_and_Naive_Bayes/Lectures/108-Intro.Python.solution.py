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

# %% [markdown] id="Z0DMy7qk__u9"
# # Intro to Python

# %% [markdown] id="jNVwzG7DRULc"
# This notebook covers some Python fundamentals including:
# - Math operations with Python (-,+,*,/, etc.)
# - Assigning variables
# - Variable naming conventions
# - Data types
# - Integers & floats
# - The print function
# - The type function
# - Strings & string methods

# %% [markdown] id="-ONw38cgKJ1c"
# ## Python as a calculator

# %% [markdown] id="DDiUwg1uKPZ4"
# Addition, subtraction, multiplication, division, exponents

# %% id="MG5kXDmbKFW2" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780416112753, "user_tz": 360, "elapsed": 45, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="c4499a3f-4389-4b39-d070-bd86cb95b68e"
2+5


# %% id="8q-OuZl4KT2Q" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780416112775, "user_tz": 360, "elapsed": 18, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="85fb24cf-8e63-4616-ef47-58dc8834febf"
168-97


# %% id="gCqaxxBOKW1D" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780416112779, "user_tz": 360, "elapsed": 13, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="8d229403-54e0-4425-9382-68d87a038f64"
5*5


# %% id="zZ2VmJPWKYYK" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780416112794, "user_tz": 360, "elapsed": 18, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="fa98f2ed-7f35-42bb-e016-67e7ef6c0c8b"
10/2


# %% id="whkn7LtQKZNJ" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780416112813, "user_tz": 360, "elapsed": 18, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="62fafcd2-4220-4419-808a-b554930295b1"
# not 5^2
5**2


# %% [markdown] id="cJ9HIBgwWGVz"
# The modulo operator gives the remainder for a division operator.  
#

# %% id="k1VQWLdaWB3K" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780416112828, "user_tz": 360, "elapsed": 13, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="df3b23db-658a-419d-b096-65d99f15a045"
5 % 2


# %% id="z4apfHYsBf6U" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780416112834, "user_tz": 360, "elapsed": 9, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="63d295b8-9149-4680-e8c2-a5fcbfbf110d"
5.5 % 2

# %% [markdown] id="Hl9Or6NqshjY"
# ### Your Turn
# What is $12.2 * 4^3$?

# %% id="cUNi5TJIsvnD" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780416112918, "user_tz": 360, "elapsed": 39, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="64604368-2ecc-42c8-e025-d3d8c73b7b7b"
# Solution
12.2 * 4**3


# %% colab={"base_uri": "https://localhost:8080/"} id="3GQlH5rsB0lC" executionInfo={"status": "ok", "timestamp": 1780416112920, "user_tz": 360, "elapsed": 29, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="f26ab311-6a61-4a30-d87e-a32e719dec5c"
(12.2) * (4**3)

# %% colab={"base_uri": "https://localhost:8080/"} id="TowwWcZ2B0hK" executionInfo={"status": "ok", "timestamp": 1780416112924, "user_tz": 360, "elapsed": 25, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="28ab61bf-b6bd-4325-b43c-992dd401f6c8"
(12.2 * 4)**3

# %% [markdown] id="1ZYtPgsdKr2z"
# ## Assigning Variables

# %% [markdown] id="UsRpGZuILwx9"
# `a = 5` assigns the value 5 to a

# %% id="RW72W_hlKpiq" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780416112925, "user_tz": 360, "elapsed": 16, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="6d701ecb-c9e4-474a-8bf5-9d6185bd957e"
a = 5
print(a)


# %% id="2_RaTzKvK4kK" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780416112933, "user_tz": 360, "elapsed": 12, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="f7fc50b1-7477-4cb8-864a-a37b8c72a831"
b = 10
print(a + b)


# %% id="jXn8bhIWC2vd" executionInfo={"status": "ok", "timestamp": 1780416116975, "user_tz": 360, "elapsed": 55, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}}
a = 8


# %% colab={"base_uri": "https://localhost:8080/"} id="F7uMqDlyEw9B" executionInfo={"status": "ok", "timestamp": 1780416310485, "user_tz": 360, "elapsed": 35, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="86c5dbb7-9227-48ba-8667-973e49b3f1a7"
print(a)


# %% colab={"base_uri": "https://localhost:8080/", "height": 106} id="CY-k0p-FFnJV" executionInfo={"status": "error", "timestamp": 1780416414089, "user_tz": 360, "elapsed": 41, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="7201f236-e123-430a-93fa-70156a81bc37"
5 = 8

# %% [markdown] id="348qhGnLLASL"
# ### Naming conventions for variables
#
# Based on [PEP8]( https://peps.python.org/pep-0008/ )
#
# - **Use descriptive, concise names for your variables**  
# - All lowercase
# - Separate words with underscores
#
# |Bad Variable Names|Good Variable Names|
# |---|---|
# |a|height|
# |UserName|user_name|
# |mystring|product_description|
# |f|fahrenheit|
#

# %% [markdown] id="HDwh5EZ-s5E8"
# ### Your Turn
# 1. Create a variable called `fahrenheit` and assign it a value of `97`.
# 2. Create a variable called `celsius` and set it equal to `(fahrenheit - 32)*(5/9)`.
# 3. Print out `celsius`.   

# %% id="SmRPBe1dtLlq" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780417381549, "user_tz": 360, "elapsed": 41, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="a4813fa7-2c97-49c5-87fc-1a4e55d5adc6"
# Solution 1
fahrenheit = 97
fahrenheit


# %% id="jNaQsowXtMTw" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780417437744, "user_tz": 360, "elapsed": 48, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="c7a57a52-082d-4f3f-fa20-6adc98f98094"
# Solution 2
celsius = ( fahrenheit - 32 ) * ( 5/9 )
celsius


# %% [markdown] id="A874kiS7XnlR"
# Be sure to run code cells in order.

# %% id="BShAJmoStNAr" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780417474132, "user_tz": 360, "elapsed": 37, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="d4000220-fc64-4499-f4c0-bb944b9365ce"
# Solution 3
fahrenheit
print( celsius )



# %% [markdown] id="yBCAiAj1NEpZ"
# ## Common Data Types

# %% [markdown] id="4b1oUzE0NHXB"
# Below is a list of the most commonly used data types in Python.
#
# Data Type | Notation    | Example
# ----------|-------------|--------
# String    | ```str```   | ```'dog'```
# Integer   |```int```    | ```4```
# Float     |```float```  |```3.14```

# %% [markdown] id="4M3oqrd8Nvg4"
# ## Strings

# %% id="R1_FCfNQNyIJ" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780417818966, "user_tz": 360, "elapsed": 63, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="088d75c1-bbf8-4573-8efb-2219b0a9c6bb"
# We can use single or double quotes when creating a string
pam = 'Pamela Beesly'
jim = "Jim Halpert"

# Composing messages can be done in multiple ways
how_sweet = pam + " <3 " + jim
print(how_sweet)


# %% id="S4V6qQNBesFB" colab={"base_uri": "https://localhost:8080/", "height": 35} executionInfo={"status": "ok", "timestamp": 1780417870847, "user_tz": 360, "elapsed": 61, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="bb90c22f-8553-4f26-a334-32cc5a969d64"
how_sweet


# %% id="ri_uNZcaeNuB" colab={"base_uri": "https://localhost:8080/", "height": 35} executionInfo={"status": "ok", "timestamp": 1780417919018, "user_tz": 360, "elapsed": 113, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="f7ab4fb8-c4e6-451a-fdb3-79f0207a2798"
how_sweet2 = f"{pam} <3 {jim}" # this is called an f-string
how_sweet2


# %% [markdown] id="6GBA9rxcPHjz"
# ## Print Function

# %% id="8L3YIxm6OBgD" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780418266731, "user_tz": 360, "elapsed": 57, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="17b58378-2096-4139-e955-caf5cc0e8403"
print( how_sweet )
print(how_sweet2)


# %% [markdown] id="hvcVaH6EtXhs"
# ### Your Turn
# 1. Create a variable called `my_name` and assign to it a string containing your name.
# 2. Create a variable called `my_class` and assign to it  the string `Data Science`.
# 3. Use an f-string to print out a statement that includes `my_name` and `my_class`.

# %% id="zeVpSYdYuLxV" colab={"base_uri": "https://localhost:8080/", "height": 35} executionInfo={"status": "ok", "timestamp": 1780418434014, "user_tz": 360, "elapsed": 43, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="d5970131-8e57-49b2-9aac-724ca8b1d548"
# Solution 1
my_name = "Robert"
my_name


# %% id="XAm-k5XruM5H" colab={"base_uri": "https://localhost:8080/", "height": 35} executionInfo={"status": "ok", "timestamp": 1780418446109, "user_tz": 360, "elapsed": 34, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="eed401ff-3cd1-4568-9408-9a66665d9695"
# Solution 2
my_class = "Data Science"
my_class


# %% id="dxUaMRU4uNh5" colab={"base_uri": "https://localhost:8080/", "height": 35} executionInfo={"status": "ok", "timestamp": 1780418452597, "user_tz": 360, "elapsed": 46, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="1ab07670-ae7f-469b-aa84-7e02385a40a6"
# Solution 3
f"{my_name} is taking the {my_class} boot camp."


# %% [markdown] id="s-1iLFRwPN9g"
# ## Integers and Floats

# %% id="LJP9VqRtPXor" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780418488250, "user_tz": 360, "elapsed": 43, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="5aeb6d98-fe2a-45da-de4a-026b5d532fa5"
# Arithmetic using two floats will return a float
2.0 + 5.0


# %% id="7zPMMI_yPcJA" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780418501805, "user_tz": 360, "elapsed": 36, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="543e25fa-021b-4550-d89c-9dbbe8a5b383"
# Arithmetic using one float and one integer will return a float
2.0 + 5


# %% id="QowxLO-pPeP6" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780418526606, "user_tz": 360, "elapsed": 56, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="42420854-136d-4573-a3e3-c539f6e1a31d"
# Division of two integers will return a float (even if the division results in a whole number)
6/3


# %% id="XXgb3qy-6mYK" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780418548070, "user_tz": 360, "elapsed": 37, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="eed454f2-ed53-4ce9-dbae-68fdb4087d88"
# Integer division, but only if terms are integers
6//3


# %% colab={"base_uri": "https://localhost:8080/"} id="JL2GQgP_N189" executionInfo={"status": "ok", "timestamp": 1780418571649, "user_tz": 360, "elapsed": 109, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="a4622c40-3e0e-4d7b-b7c2-043e28786df8"
6//4

# %% id="bsGMfT0-Fy-V" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780418575414, "user_tz": 360, "elapsed": 125, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="53bf45b9-c468-470a-fa34-3aad4ad43759"
6//4.0


# %% colab={"base_uri": "https://localhost:8080/"} id="29mbzLm7N8iS" executionInfo={"status": "ok", "timestamp": 1780418599343, "user_tz": 360, "elapsed": 184, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="bbe9aac9-ce30-42be-9fa7-faa79248b090"
6%4

# %% colab={"base_uri": "https://localhost:8080/", "height": 35} id="xgufEIxTOAR7" executionInfo={"status": "ok", "timestamp": 1780418690634, "user_tz": 360, "elapsed": 61, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="d081439c-aef7-443b-8fa6-bffcbd00fc29"
a = 6
b = 4
f"{a//b}r{a%b}"

# %% [markdown] id="2jKCOo9JPQoN"
# ## Type()

# %% id="5RGR5T2AOEr5" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780418731360, "user_tz": 360, "elapsed": 43, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="5566e971-9899-474b-c907-e55e4150bc2c"
type(how_sweet)


# %% id="Ybw5ZxN0PUT5" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780418747830, "user_tz": 360, "elapsed": 61, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="c6762f7e-7def-421f-e34d-2d5747065cdf"
type(5)


# %% id="KlL8dUowPYb7" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780418754444, "user_tz": 360, "elapsed": 41, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="654ae163-73a1-405d-c326-f43ccea858c4"
type(5.5)


# %% id="E9Ur_ztcSqK8" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780418768824, "user_tz": 360, "elapsed": 77, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="f40bde22-bfd4-4906-f55f-a23f08091588"
type(5.0)


# %% id="0qjhnMLs7JFY" executionInfo={"status": "ok", "timestamp": 1780418802679, "user_tz": 360, "elapsed": 25, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}}
whatis = type


# %% id="gOdxRzYr7Lm2" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780418805812, "user_tz": 360, "elapsed": 66, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="f362816d-7737-4df8-96ea-dafc3f5b2991"
whatis(5.0)


# %% [markdown] id="orFEPd5AHyuH"
# a = print
#
#

# %% [markdown] id="fhHcyi-wH19b"
# print = a
#

# %% colab={"base_uri": "https://localhost:8080/"} id="X8eHxJk-PlwN" executionInfo={"status": "ok", "timestamp": 1780419033589, "user_tz": 360, "elapsed": 35, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="d44fc521-45bf-448c-9d55-c857c09aab60"
a = 6
a


# %% id="Ssobi3GWH8nM" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780419038066, "user_tz": 360, "elapsed": 47, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="f9fcef64-efe7-4068-da6d-e21ede115c41"
print = a
print

# %% id="gGSktM-mH-2e" colab={"base_uri": "https://localhost:8080/", "height": 141} executionInfo={"status": "error", "timestamp": 1780419042680, "user_tz": 360, "elapsed": 75, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="e3bd3ad2-c1ae-4c9f-be77-ccc569fddf4b"
print("hello")

# %% id="v8CL5-uLIF2s" executionInfo={"status": "ok", "timestamp": 1780419050616, "user_tz": 360, "elapsed": 42, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}}
del a


# %% id="gIwJoEquIJNk" colab={"base_uri": "https://localhost:8080/", "height": 141} executionInfo={"status": "error", "timestamp": 1780419051892, "user_tz": 360, "elapsed": 84, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="c6a36269-85f3-4562-86d9-6927843ca8ee"
a


# %% colab={"base_uri": "https://localhost:8080/", "height": 141} id="9O6dsTIIPuc9" executionInfo={"status": "error", "timestamp": 1780419063927, "user_tz": 360, "elapsed": 46, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="bdf3b3ce-a065-4479-c37f-4ad258617092"
print("hello")


# %% colab={"base_uri": "https://localhost:8080/"} id="s7MVFx03PvzG" executionInfo={"status": "ok", "timestamp": 1780419119715, "user_tz": 360, "elapsed": 42, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="8f13bc55-346a-44df-ed9e-996076f4ebf7"
print

# %% id="VK_6c5JCIPmV" executionInfo={"status": "ok", "timestamp": 1780419120931, "user_tz": 360, "elapsed": 26, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}}
del print


# %% id="HE_5GbgXIQ03" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780419124774, "user_tz": 360, "elapsed": 68, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="e5e8b81f-2260-46f7-f8ab-a29137ce6621"
print("hello")

# %% id="vNq9-AIt03DC"
# 1.234 => 1.2

# 12 exp -1

# %% id="3rubqKnL1NlV" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780418948364, "user_tz": 360, "elapsed": 64, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="f083e8a0-7ba0-4292-a987-7cc94d23b137"
5.22 % 1.22

# %% id="SQxJHzWX2qjX" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780418951981, "user_tz": 360, "elapsed": 36, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="486b68fc-f5a0-449f-8b33-4d4774ab5b22"
(522 % 122)/100

# %% [markdown] id="CAkrmYGPTIoN"
# ## Conversions

# %% [markdown] id="M6PwvpvGTNWc"
# We can convert between different data types. Be careful because sometimes a conversion may not produce the intended result!

# %% id="YxNnfbf_TS6N" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780419185229, "user_tz": 360, "elapsed": 63, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="8b1960c6-9ace-480d-9c2d-4c2a8fc56ce3"
int(5.3)


# %% id="HU5fKZnqTXC_" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780419331852, "user_tz": 360, "elapsed": 47, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="341d5e33-509f-42ac-ef78-6ce532e69c10"
int(5.7)


# %% id="c6v-Rhq4592G" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780419381186, "user_tz": 360, "elapsed": 34, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="0c193174-b5ea-41df-b288-7af396a81ccc"
int(-5.7)


# %% id="tFpyGEE8TZI1" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780419574475, "user_tz": 360, "elapsed": 38, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="69c94a1c-6316-4cc6-bc61-eb9e98c7c256"
float(10)


# %% id="_E3zeJL4Tafq" colab={"base_uri": "https://localhost:8080/", "height": 35} executionInfo={"status": "ok", "timestamp": 1780419584313, "user_tz": 360, "elapsed": 33, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="74f4a1fb-5fa7-4677-b1a6-fe7f58c6158b"
str(10.2)


# %% id="JqIL_TtdzFim" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780419729902, "user_tz": 360, "elapsed": 62, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="62bd9923-7048-483d-8c55-b8e460002ed9"
float(str(10.2) + str(5))


# %% id="mg4DY-GC8Mwm" colab={"base_uri": "https://localhost:8080/", "height": 35} executionInfo={"status": "ok", "timestamp": 1780419771070, "user_tz": 360, "elapsed": 66, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="59939b2f-9c2f-40d9-a88b-db8de0591adf"
(str(10.2) + str(5))


# %% id="aLclbkaK8Mky" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780419793594, "user_tz": 360, "elapsed": 42, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="e26cf20c-1761-4863-8752-2d8c820783e8"
str(10.2), str(5)


# %% id="jXVIci_98MVQ" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780419839313, "user_tz": 360, "elapsed": 43, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="9d78c9ae-4610-4fe6-959c-074c3c3dca7a"
str(10.2), 5


# %% id="aVVog_xX8MPv" colab={"base_uri": "https://localhost:8080/", "height": 141} executionInfo={"status": "error", "timestamp": 1780419865558, "user_tz": 360, "elapsed": 59, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="df150eb3-a778-4b35-892c-ddb52ff67155"
float(str(10.2) + str(5.5))


# %% colab={"base_uri": "https://localhost:8080/", "height": 35} id="tR81OPKoS4_V" executionInfo={"status": "ok", "timestamp": 1780419908064, "user_tz": 360, "elapsed": 36, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="91f2aa28-cbb6-4879-c4e9-62784618dd7d"
str(10.2) + str(5.5)

# %% id="-QX4JQh8HU3w" colab={"base_uri": "https://localhost:8080/", "height": 141} executionInfo={"status": "error", "timestamp": 1780419948391, "user_tz": 360, "elapsed": 65, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="9e8e8c52-637b-4219-9476-0698401ab6e2"
float(str(10.2) + 5)


# %% colab={"base_uri": "https://localhost:8080/", "height": 141} id="dL9JfurPTI-L" executionInfo={"status": "error", "timestamp": 1780419959508, "user_tz": 360, "elapsed": 36, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="d7072642-e845-400a-abee-6d92b07c993d"
str(10.2) + 5

# %% colab={"base_uri": "https://localhost:8080/"} id="aOY3zaohTK44" executionInfo={"status": "ok", "timestamp": 1780419969788, "user_tz": 360, "elapsed": 49, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="2f63cba2-0dd5-4ee1-f1f8-5ad6ad55684c"
str(10.2), 5

# %% [markdown] id="kIDKuU0LWSB1"
# ## Methods in Python
# Methods are functions that only run on objects of a certain type. Different object types have different methods. For example, strings have certain methods (such as `.upper()` and `.lower()` - see below) that can only be used on strings. Other object types in Python (such as lists, data frames, etc.) have their own corresponding methods.
#
# The format to call a method is `object_name.method_name()`. Arguments to the method are passed in the parentheses. The method acts on the object itself, and therefore, some methods do not take any additional arguments (such as `.upper()`).

# %% [markdown] id="_M7WpCqeQeI4"
# ## String Methods
#

# %% [markdown] id="seynWZ9AUkm2"
# **Tab Completion**
# We can explore the string methods by using tab completion and the help documentation.  
#
# Tip: Tools- Settings - Editor - Uncheck Automatically Trigger Code Completion.  
# This will make it so that when you hit 'Tab' it offers code completion suggestions or displays a method's or function's doc string.  

# %% id="csm7IM9aFM08" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780420178703, "user_tz": 360, "elapsed": 45, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="edd85d70-8114-47ab-c16a-d189520cb63e"
print(how_sweet)


# %% id="WHmTWFEdPZwK" colab={"base_uri": "https://localhost:8080/", "height": 35} executionInfo={"status": "ok", "timestamp": 1780420191353, "user_tz": 360, "elapsed": 66, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="a97b8ed3-2f71-4135-d43e-72a413b5c596"
# swapcase method
how_sweet.swapcase()


# %% id="7qknGH7vJgvx" colab={"base_uri": "https://localhost:8080/", "height": 35} executionInfo={"status": "ok", "timestamp": 1780420213828, "user_tz": 360, "elapsed": 35, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="c9ab0601-73bc-4361-b693-cbdf7b441960"
"hello".capitalize()


# %% id="r3s99V3C-NNn" colab={"base_uri": "https://localhost:8080/", "height": 141} executionInfo={"status": "error", "timestamp": 1780420227879, "user_tz": 360, "elapsed": 31, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="4a1234e8-3591-4839-dfe0-ea9fbf9ed375"
how_sweet.count()


# %% id="MzpWfp-d5VkN" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780420238300, "user_tz": 360, "elapsed": 44, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="6f63d9c4-a9c4-4965-bdd0-b07472a36b4b"
how_sweet.count("e")


# %% id="rlcNE38r-d-Q" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780420257015, "user_tz": 360, "elapsed": 55, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="ab1e43db-3749-414d-a9a4-7733586ea40a"
how_sweet.count("p")


# %% colab={"base_uri": "https://localhost:8080/", "height": 35} id="OXkLuWGtUeXd" executionInfo={"status": "ok", "timestamp": 1780420362365, "user_tz": 360, "elapsed": 61, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="dbb1aef8-2cad-4741-fe8d-91a2441a5e35"
str.capitalize("hello")


# %% colab={"base_uri": "https://localhost:8080/", "height": 35} id="UPFnaSX4UeT9" executionInfo={"status": "ok", "timestamp": 1780420432564, "user_tz": 360, "elapsed": 41, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="3e68722a-54a5-451a-bd85-0fa87a4a6d3f"
"HELLO".capitalize()


# %% [markdown] id="ojswLdVbXdq8"
# Putting your cursor inside the parenthesies and hitting Tab will give you information about what a method does.

# %% [markdown] id="kMddP2Igqv7A"
# For more info and details see ...
# - https://docs.python.org/3/library/stdtypes.html#string-methods
# - https://www.w3schools.com/python/python_strings_methods.asp

# %% id="UyERk1bjQoWn" colab={"base_uri": "https://localhost:8080/", "height": 35} executionInfo={"status": "ok", "timestamp": 1780421107118, "user_tz": 360, "elapsed": 79, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="64b23a9e-c772-4d08-ec16-a55bb99e35de"
how_sweet.upper()


# %% id="FWNnmaweVlFK" colab={"base_uri": "https://localhost:8080/", "height": 35} executionInfo={"status": "ok", "timestamp": 1780421111845, "user_tz": 360, "elapsed": 35, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="71fc29b3-980f-4831-e905-9a0545843974"
how_sweet.lower()


# %% colab={"base_uri": "https://localhost:8080/", "height": 35} id="VDV7nOkNXrMD" executionInfo={"status": "ok", "timestamp": 1780421150835, "user_tz": 360, "elapsed": 35, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="e714d814-9c47-4eb0-8b99-77f6297f8771"
how_sweet


# %% id="uxWk_SWlUq2B" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780421125588, "user_tz": 360, "elapsed": 63, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="e4a2decf-78f4-4cbe-a17d-8436ee398c9f"
type(how_sweet.swapcase())


# %% id="wCRixbL2_zEw" colab={"base_uri": "https://localhost:8080/", "height": 35} executionInfo={"status": "ok", "timestamp": 1780421249888, "user_tz": 360, "elapsed": 72, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="73d8575f-74c1-4a04-9c15-299a01e616e2"
how_sweet.swapcase().swapcase().title().upper().capitalize().title()


# %% id="Ei7aZaR_AVoo" colab={"base_uri": "https://localhost:8080/", "height": 35} executionInfo={"status": "ok", "timestamp": 1780421503802, "user_tz": 360, "elapsed": 40, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="e0eafd98-279e-404d-a840-b13c7a4f282d"
(
  how_sweet
  .swapcase()
  .swapcase()
  # .title()
  # .upper()
  # .capitalize()
  # .title()
)



# %% [markdown] id="BVPY_hPwvhqS"
# ### Your Turn
#
# Try out the `.capitalize()` method on the `how_sweet` string. What does it do?
#
# ```python
# how_sweet = pam + " <3 " + jim
# how_sweet
# ```

# %% colab={"base_uri": "https://localhost:8080/", "height": 35} id="g1fkHHoqZTT_" executionInfo={"status": "ok", "timestamp": 1780421771098, "user_tz": 360, "elapsed": 38, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="06176a66-6f1b-4dff-e5fe-956013032eb0"
how_sweet = pam + " <3 " + jim
how_sweet


# %% id="lAYnLzf7wJsJ" colab={"base_uri": "https://localhost:8080/", "height": 35} executionInfo={"status": "ok", "timestamp": 1780421777455, "user_tz": 360, "elapsed": 54, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="6d205cb6-9cdb-4b32-cec5-257e90ad0e11"
# Solution
how_sweet.capitalize()


# %% colab={"base_uri": "https://localhost:8080/", "height": 35} id="QolBz0bUaHdi" executionInfo={"status": "ok", "timestamp": 1780421802794, "user_tz": 360, "elapsed": 68, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="4edb62a8-b6fd-4945-ebc8-34a71f86963b"
# Solution
how_sweet.upper().lower().capitalize()


# %% id="I9TwTP8AZZig"
# how_sweet.capitalize?


# %% colab={"base_uri": "https://localhost:8080/"} id="Fdwiwu1_af4H" executionInfo={"status": "ok", "timestamp": 1780421906452, "user_tz": 360, "elapsed": 56, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="9155de27-1992-4bc7-f0b1-e2593cec1138"
how_sweet.upper().count("E")



# %% [markdown] id="1D1yPSZWwNom"
# ## Help

# %% id="pyp66ABwOxLM" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780422153882, "user_tz": 360, "elapsed": 22, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="1f56c01e-25b5-4b7f-a022-9adb9b8879f6"
# The help() function will print out the documentation for a function
help(len)


# %% colab={"base_uri": "https://localhost:8080/", "height": 35} id="nw9fV6d5cL4j" executionInfo={"status": "ok", "timestamp": 1780422330310, "user_tz": 360, "elapsed": 53, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="85fc3a95-afe0-48f6-ddf8-7ea9882bcee1"
pam


# %% id="D1SLBeoQs_Do" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780422177936, "user_tz": 360, "elapsed": 82, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="51c2a9ef-64d6-41e2-bc7b-1f3d2b887f9e"
help(pam)


# %% id="cmhtqJ5lDIX6" executionInfo={"status": "ok", "timestamp": 1780422190018, "user_tz": 360, "elapsed": 41, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}}
# pam?


# %% id="A8QSl5S6P_aV" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780422223946, "user_tz": 360, "elapsed": 52, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="6dc0f33f-7853-4882-e3f4-507bef9e6445"
len(pam)


# %% id="FdXXlmEPQLhV" executionInfo={"status": "ok", "timestamp": 1780422251257, "user_tz": 360, "elapsed": 74, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}}
# You can also put a question mark after the function name
# len?


# %% id="eMQT0zg_QO3n" executionInfo={"status": "ok", "timestamp": 1780422262276, "user_tz": 360, "elapsed": 46, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}}
# Question marks can also be used after a method to see the method's documentation
# pam.find?


# %% id="g0TzT6UxOGvi" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780422305884, "user_tz": 360, "elapsed": 51, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="f08fe846-3c7d-4473-de1e-69b8945f920c"
pam.find("B")

# %% id="eoSK7ff9EMVx" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780422311311, "user_tz": 360, "elapsed": 46, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="81b65c73-a45b-48d0-bfbe-b498443994e0"
pam.find("p")


# %% id="UxE4BT1KO2BT" colab={"base_uri": "https://localhost:8080/", "height": 141} executionInfo={"status": "error", "timestamp": 1780422348087, "user_tz": 360, "elapsed": 90, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="06c8161a-9144-4d3e-84e4-419fa45eddc9"
help(find)

# %% id="rPK7jQihOgAa" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780422363619, "user_tz": 360, "elapsed": 46, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="7c632031-c4d7-4850-f4ad-db7fcc90d56f"
help(''.find)

# %% id="JXX0Md6cD2NJ" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780422384043, "user_tz": 360, "elapsed": 50, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="a0dba265-be60-418b-a397-3d534f616e06"
help(str.find)


# %% id="Ia_Jfh-zPSJT" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780422390021, "user_tz": 360, "elapsed": 43, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="3e7e655b-00db-48eb-8d99-a9a73086fccd"
help("")

# %% id="n5NZ1M0hEjmS" colab={"base_uri": "https://localhost:8080/", "height": 106} executionInfo={"status": "error", "timestamp": 1780422421828, "user_tz": 360, "elapsed": 38, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="130dea82-ee60-4da8-a67e-9d07a9cc2bae"
# int.%?

# %% id="Tv7C5-JTFPfb" colab={"base_uri": "https://localhost:8080/", "height": 106} executionInfo={"status": "error", "timestamp": 1780422426962, "user_tz": 360, "elapsed": 41, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="d1a2de59-6054-487f-80e5-4a3affa4f859"
help(int.%)

# %% id="f7mfaHO-FUlq" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780422433336, "user_tz": 360, "elapsed": 46, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="3839ef25-e033-426c-955e-075deb8d4939"
help('%')

# %% [markdown] id="EQp-b-fowis8"
# ### Your Turn
# 1. Look up the documentation for the `.lstrip` method.
# 2. Use `.lstrip` to remove the first letter of the `how_sweet` string. *Hint*: You'll need to specify the `chars` argument in the `.lstrip` method.
#
# ```python
# how_sweet = pam + " <3 " + jim
# how_sweet
# ```
#

# %% colab={"base_uri": "https://localhost:8080/", "height": 35} id="w7jnHCuWdFup" executionInfo={"status": "ok", "timestamp": 1780423048611, "user_tz": 360, "elapsed": 32, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="e235218b-81bd-4387-a5a7-32ba8b684325"
how_sweet = pam + " <3 " + jim
how_sweet


# %% id="B2hzidOJwrJL" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780423068608, "user_tz": 360, "elapsed": 58, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="4fc8e72e-aaca-4e93-bd6d-d6dd499e4fb5"
# Solution 1
help(how_sweet.lstrip)


# %% id="tP4qCd2rwsCv" colab={"base_uri": "https://localhost:8080/", "height": 35} executionInfo={"status": "ok", "timestamp": 1780423130713, "user_tz": 360, "elapsed": 66, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="92bf4da6-451d-4da1-dcef-0a69541bf1db"
# Solution 2
how_sweet.lstrip("P")


# %% id="zIJevJZOOl5Q"

# %% id="WDmwt0EFkeKP"
