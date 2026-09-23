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

# %% [markdown] id="AxQlsAQWMECU"
# **Python Data Structures**
# Python has several built-in data structures including:
# - lists
# - tuples
# - dictionaries
# - sets
#
# These are different structures for storing collections of data. We'll start by talking about lists.
#

# %% [markdown] id="swWfaKS7moHs"
# [CRUD]( https://en.wikipedia.org/wiki/Create,_read,_update_and_delete ) operations.  Wikipedia asserts that these are for persistent storage, but they are actually applicable to any kind of storage, including Python variables, especially collections.

# %% [markdown] id="k0LwK-ufGTj1"
# ## Lists

# %% [markdown] id="S8KhHhegG4iC"
# Lists in Python are ordered, mutable collections of objects.
#
# A list is created using ```[]``` and commas between the objects.  
#
# You could have a list of
# - numbers
# - strings
# - numbers and strings
# - lists
# - other objects
#

# %% [markdown] id="C-btC90kJ9GO"
# ## Example lists

# %% [markdown] id="j3-lHftCT1d2"
# Here is a list of integers.

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 170, "status": "ok", "timestamp": 1780431803793, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="NCaLUwY2GJtG" outputId="60ab79d5-1eb6-4061-d83d-8b1f2b730764"
some_integers = [5,7,2,2,5,7,9,114059]
print(some_integers)
print(type(some_integers))

# %% [markdown] id="ryVP4aoAT7Jv"
# Here is a list of strings.

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 146, "status": "ok", "timestamp": 1780431803954, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="PN3sY6GtJRfd" outputId="cc9d7682-554e-4b9c-f64d-49a3d00bf9a7"
lyrics = [
          "Happy birthday to you.  ",
          "Happy birthday to you.  ",
          "Happy birthday dear Suzy",
          "Happy birthday to you.",
          ]
print(lyrics)

# %% [markdown] id="sCCrPyXzUErW"
# Here is a list of numbers and strings.

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 34, "status": "ok", "timestamp": 1780431804011, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="7H3ytb7CJaLh" outputId="3e140a66-6cd4-410e-dc6d-f4a17d7b0e3b"
numbers_and_strings = [5.5, "Life is good.", 63, 7, "I like Python!"]
print(numbers_and_strings)

# %% [markdown] id="LkBJ84D2UIQM"
# We can also have lists of lists.

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 28, "status": "ok", "timestamp": 1780431804047, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="AtmH_UBmJh84" outputId="1261a789-b75f-4e97-92ac-749e6e62c230"
nested_list = [[4,5,6],[5,44],[34,7,88]]
print(nested_list)

# %% [markdown] id="lrskydrOzgQo"
# ### Your Turn
# 1. Create a list called `students` that has the first names of the other students in your cohort. Print out `students`.
# 2. Create a list of 3 integers called `my_ints`. Create a list of 3 floats called `my_floats`.
# 3. Create a nested list called `ints_and_floats` that contains your `my_ints` and `my_floats` lists. Print out `ints_and_floats`.

# %% id="ofTXJpWmSrJ2" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780431804140, "user_tz": 360, "elapsed": 35, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="bbb87a08-08c2-45b7-d21b-28d00e1a0b92"
# Solution 1
students = ['John', 'Paul', 'George', 'Ringo']
students


# %% id="uj5cF9Daz-ml" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780431804166, "user_tz": 360, "elapsed": 20, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="d506d945-cacb-425c-bcea-8b1d6e29364c"
# Solution 2
my_ints = [ 1, 2, 3 ]
my_floats = [ 1.1, 2.2, 3.3 ]

print(my_ints)
print(my_floats)


# %% id="M312AhIuz_SS" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780431804191, "user_tz": 360, "elapsed": 21, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="a6fcd05a-af00-4138-ff7b-e07768dac7e3"
# Solution 3
ints_and_floats = [ my_ints, my_floats]
ints_and_floats


# %% [markdown] id="AhmUcKN9Jp2c"
# ## Indexes and slices

# %% [markdown] id="Ugauxv7xKgtp"
# You can access items in a list by specifying the position, or index or offset, of the item you want to access. Lists in Python use zero indexing - that is the first element is refered to as element 0.

# %% [markdown] id="E0d8tk3ZVNnT"
# Refering to one element in a list:

# %% id="XGZ_n4gfKlyZ" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780432859036, "user_tz": 360, "elapsed": 146, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="1f56e768-6765-48e0-f69e-7a7b8a4ad78f"
prime_numbers = [1,2,3,5,7,9]
prime_numbers


# %% id="oHmKUhlcj7F9" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780432944347, "user_tz": 360, "elapsed": 106, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="563b7271-1357-4a88-accb-7008852dcc22"
prime_numbers[0]


# %% id="sUQdoa8KJKMQ" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780432960401, "user_tz": 360, "elapsed": 62, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="21c8a371-b1ac-4cb3-d167-d606d0c9e429"
prime_numbers[3]


# %% id="L-OghStQT6T_" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780432973722, "user_tz": 360, "elapsed": 105, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="6a1d44bb-6618-43bf-c62b-da50e8e75392"
prime_numbers[4]


# %% id="P--WY8hyZWsh" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780433010579, "user_tz": 360, "elapsed": 102, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="4512134d-6dfd-4c5a-b9b0-fad12d902501"
prime_numbers[-1]


# %% id="_YTnh5j9UEoj" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780433013518, "user_tz": 360, "elapsed": 125, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="7d6b916f-a180-4060-d444-0553217aeb4f"
prime_numbers[-2]

# %% id="3SWA-CNqUE-2" colab={"base_uri": "https://localhost:8080/", "height": 141} executionInfo={"status": "error", "timestamp": 1780433049443, "user_tz": 360, "elapsed": 186, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="6c9907ae-ea42-45a6-a5c1-c8f948b4190a"
prime_numbers[-540]


# %% id="xCLKFQD6kVHp" colab={"base_uri": "https://localhost:8080/", "height": 141} executionInfo={"status": "error", "timestamp": 1780433063256, "user_tz": 360, "elapsed": 65, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="1bb6255c-1760-48f3-dbc9-89aa14679af8"
prime_numbers[540]


# %% [markdown] id="nM8fwvnmVQD1"
# List slices:
# beginning number is inclusive, ending number is exclusive (not included). Note that the notation is `my_list[start:stop]`

# %% [markdown] id="YOwXR1wPUW48"
# [start,end)

# %% id="h1SWGm9dUVQf" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780433136431, "user_tz": 360, "elapsed": 94, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="f677bdaf-dc11-4124-f560-f554fa92e643"
prime_numbers

# %% id="qTTDRD-WVSTc" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780433159567, "user_tz": 360, "elapsed": 108, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="df7dbfc9-7392-4733-8924-506b5233f9d3"
prime_numbers[1:3]


# %% id="M6Id6pnZZ1iE" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780433170660, "user_tz": 360, "elapsed": 158, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="8819cb22-a618-4dbe-c10b-626def5720ed"
prime_numbers[3:4]


# %% id="MZCZrw-rlGHW" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780433251727, "user_tz": 360, "elapsed": 134, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="7b02bd59-7446-4981-af27-6ff3cb109b21"
type(prime_numbers[3:4])

# %% id="oNCMKEUgUqJx" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780433270779, "user_tz": 360, "elapsed": 118, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="33a9721b-d9e1-4ba7-cc95-477da850d522"
prime_numbers[3]

# %% id="EIoH97xDlI4m" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780433276346, "user_tz": 360, "elapsed": 203, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="b4ebbe7c-8bfb-4c8e-ee1b-b62677908930"
type(prime_numbers[3])

# %% id="cYJFZG2PZ6Cv" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780433444285, "user_tz": 360, "elapsed": 163, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="b657ebae-2397-4f0d-f8ed-053565a37696"
prime_numbers[:3]

# %% id="y21wVNJlZ8Mw" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780433455124, "user_tz": 360, "elapsed": 169, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="889eccf9-cdfe-4f70-ae7b-77112f3deab7"
prime_numbers[2:]

# %% id="M5nRHYH9Wa7Z" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780433498608, "user_tz": 360, "elapsed": 164, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="931a2077-a7a1-4ee4-bd02-3a6a94d39079"
prime_numbers[:]


# %% id="2T3Vyk3kRmc2" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780433564433, "user_tz": 360, "elapsed": 111, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="7d4bce53-2cf4-44ea-8c27-2478244c7140"
ab = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
ab


# %% id="sX8G5DaURwnE" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780433576854, "user_tz": 360, "elapsed": 128, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="c3b6002b-243d-4e28-e937-ab236ca3ca65"
ab[1:3]

# %% id="7qZa0YupRwja" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780433580290, "user_tz": 360, "elapsed": 26, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="8047a910-b8bb-40da-e717-016808282aeb"
ab[3:4]

# %% id="UOSxrFyhRwhM" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780433589747, "user_tz": 360, "elapsed": 48, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="0e119b61-0f7a-41aa-9b49-41794da18e5a"
ab[:3]

# %% id="XR-6XVLpRwfH" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780433596381, "user_tz": 360, "elapsed": 71, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="3255338f-fdc8-4af5-82ec-9f28415c1a57"
ab[2:]

# %% id="AGSUOe4bRwa4" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780433608155, "user_tz": 360, "elapsed": 167, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="5012ced1-d268-44c5-d10f-b2b04c321a9b"
ab[:]

# %% id="YR4XDCDnRwWP" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780433836026, "user_tz": 360, "elapsed": 90, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="efe603ce-8a4c-4971-9246-dd5797f7d0b3"
start = None
end = 10
ab[start:end]

# %% id="ztSHy5gxRwPZ" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780433897462, "user_tz": 360, "elapsed": 79, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="ecdf06ee-bd13-4cf7-a26f-8e07a5620021"
(
ab
  [:]
  [:2]
  [:]
  [:1]
)

# %% [markdown] id="gnlY9L7Ixkwj"
# Create a list with every second item from ``` prime_numbers```. Note that the notation is `my_list[start:stop:increment]`.
#

# %% id="6yupWEPUVA8M" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780434191269, "user_tz": 360, "elapsed": 134, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="d6c129af-c710-4a21-c6fb-90c8aeb2f131"
prime_numbers


# %% colab={"base_uri": "https://localhost:8080/"} id="Y9Z7kKHPJePh" executionInfo={"status": "ok", "timestamp": 1780434203824, "user_tz": 360, "elapsed": 44, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="139afe1a-12f8-46de-e92d-ecdf60e8a9fd"
prime_numbers[0:5]


# %% id="a3vol6wVPhhr" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780434228035, "user_tz": 360, "elapsed": 79, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="6fa1499a-dd0e-42cf-f72e-66c54c40fb51"
prime_numbers[0:5:2]


# %% [markdown] id="-GkCqg0eacVk"
# Create a list the numbers reversed

# %% colab={"base_uri": "https://localhost:8080/"} id="mok9RptyJzQa" executionInfo={"status": "ok", "timestamp": 1780434289752, "user_tz": 360, "elapsed": 63, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="23ce1007-4d0d-4c69-8496-45e1f8cf2d0e"
prime_numbers[3::]


# %% id="T-yH5WOaabGl" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780434297392, "user_tz": 360, "elapsed": 149, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="1e8560b1-66ac-4af7-f527-3e3ab77e544f"
prime_numbers[3::-1]


# %% id="1yI8ntKLnHVm" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780434317379, "user_tz": 360, "elapsed": 112, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="829c6873-5747-41a8-dcc8-e532c3bf7777"
prime_numbers[3:None:-1]


# %% id="eU3f_Qw-XD3U" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780434356822, "user_tz": 360, "elapsed": 123, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="8334dd30-179a-49ca-c619-7ba5c88a0e2d"
prime_numbers[::-1]


# %% id="0y61GvwYnJuy" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780434376133, "user_tz": 360, "elapsed": 146, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="eae3d5d7-1176-45df-89f9-575faa37f1ec"
prime_numbers[None:None:-1]


# %% id="p0wVtXVvXFwt" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780434392223, "user_tz": 360, "elapsed": 115, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="ca02adcc-fdf7-4459-ea88-f37fd3b3ed78"
prime_numbers[-1::-1]


# %% [markdown] id="MnJQ9OSHLhpX"
# Get the last n items

# %% id="anLgGJijX7Mv" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780434506611, "user_tz": 360, "elapsed": 94, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="40e2cdea-b99e-4a91-ea1b-e5464703fba4"
prime_numbers

# %% id="qclIljozLlLv" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780434518443, "user_tz": 360, "elapsed": 79, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="d00d55c1-89d8-42cd-d787-157e796ab624"
n = -3
prime_numbers[n:]

# %% id="W0gikti7nQl9" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780434530801, "user_tz": 360, "elapsed": 91, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="9f95b28b-49d3-49f1-f45c-2b2925d906cb"
n = -3
prime_numbers[n::1]

# %% id="Tidn6pF4ncoO" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780434541385, "user_tz": 360, "elapsed": 112, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="a84d6dfd-2240-4913-ee2e-174bc6fa541e"
n = -3
prime_numbers[n::-1]


# %% [markdown] id="tic-WiYB0DEV"
# ### Your Turn
# 1. Create a list called `tens` that contains the following integers: 10, 20, 30, 40, 50, 60, 70, 80, 90
# 2. Use indexing to access `30` from your list.
# 3. Use indexing to access `90` from your list.
# 4. Use indexing to access the numbers `30` through `60`, inclusive, from your list.
# 5. Use indexing to access every third item from your list.

# %% id="WfIrKO1W0oYs" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780435126957, "user_tz": 360, "elapsed": 104, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="021da22c-c95d-4472-8cd7-638531c7fd10"
# Solution 1
tens = [10, 20, 30, 40, 50, 60, 70, 80, 90]
tens


# %% id="w1UR2JnP0ptl" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780435138700, "user_tz": 360, "elapsed": 74, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="11ac885c-10c6-4eed-d969-b2b84b0775dd"
# Solution 2
tens[2]


# %% id="4NNm60970qWz" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780435146625, "user_tz": 360, "elapsed": 103, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="42287e4b-4fd7-46b0-ad29-c9559c3f6303"
# Solution 3
tens[8]


# %% colab={"base_uri": "https://localhost:8080/"} id="bmj5CqyRLSRj" executionInfo={"status": "ok", "timestamp": 1780435155894, "user_tz": 360, "elapsed": 96, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="c6b1aa97-469d-4556-9128-904790654f24"
tens[-1]


# %% id="y4Fh2LULLvo3" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780435200182, "user_tz": 360, "elapsed": 35, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="20d41335-ab55-4d87-e33d-8776678f066c"
# Solution 4
tens[2:-3]


# %% id="PilnXQNR0sMG" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780435231142, "user_tz": 360, "elapsed": 213, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="f905dd82-5a28-4ed7-83c2-fbfecea3c6b0"
# Solution 5
tens[::3]


# %% colab={"base_uri": "https://localhost:8080/"} id="8KfUWPvsLba4" executionInfo={"status": "ok", "timestamp": 1780435257286, "user_tz": 360, "elapsed": 95, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="93ed0a39-6b2f-440f-c5bf-d3ff0ce8e662"
tens[2::3]


# %% colab={"base_uri": "https://localhost:8080/"} id="Ozq3Y0RhNvh-" executionInfo={"status": "ok", "timestamp": 1780435324122, "user_tz": 360, "elapsed": 129, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="1b0c87b1-25a5-4d93-efda-1acee6f51532"
tens[::2]

# %% [markdown] id="VtwrAprrwoTh"
# ## List Methods

# %% [markdown] id="898UaP2DdiB6"
# ### Adding elements to a list

# %% [markdown] id="XDCqI_u6xe0q"
# Add an element to the end of a list
#

# %% id="oo9pDPreXel7" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780435419769, "user_tz": 360, "elapsed": 114, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="8e9f43ff-2283-4425-a638-c70c4fae7c64"
prime_numbers


# %% id="zRKTEfwRVwJZ" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780435425124, "user_tz": 360, "elapsed": 18, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="7105dca8-2c29-4ac1-967c-0b788716d092"
prime_numbers.append(11)
print(prime_numbers)


# %% [markdown] id="kNK-TWvtdpRO"
# Insert an element into a list

# %% id="zAGSmtNldsRY" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780435477365, "user_tz": 360, "elapsed": 100, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="9ad821f0-6dbf-4473-f330-5a2d552e5a1a"
prime_numbers.insert(1,5)
print(prime_numbers)


# %% [markdown] id="GfluUbdi09RS"
# #### Your Turn
# 1. Add 100 to the end of your `tens` list.
# 2. Add 0 to the beginning of your `tens` list.

# %% [markdown] id="SOPiAo9tyggd"
# ```python
# tens = [ 10, 20, 30, 40, 50, 60, 70, 80, 90, ]
# tens
# ```

# %% colab={"base_uri": "https://localhost:8080/"} id="7wgKL_dmOxIz" executionInfo={"status": "ok", "timestamp": 1780435733758, "user_tz": 360, "elapsed": 118, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="1d571a2e-c570-4e21-aa1e-222a51ce7cc7"
tens = [ 10, 20, 30, 40, 50, 60, 70, 80, 90, ]
tens


# %% id="jJ93zJaPmbOh" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780435744435, "user_tz": 360, "elapsed": 127, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="2d3cdb23-3bc4-45e5-95b5-34a27d41b867"
# Solution 1
tens.append(100)
tens


# %% id="jfC-UBbL1IHD" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780435770820, "user_tz": 360, "elapsed": 119, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="b4b7092c-aa10-493e-9f67-e2170f8507d1"
# Solution 2
tens.insert(0,0)
tens


# %% [markdown] id="2O8kRm-qeRyb"
# ### Removing elements from a list

# %% [markdown] id="6x77UXFyeWr9"
# Delete an element based on its index

# %% id="rhk8gsmNYycY" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780436066160, "user_tz": 360, "elapsed": 191, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="0895b12e-026c-40a1-c65c-a58835dd379a"
prime_numbers


# %% id="Nha5CR_GeZep" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780436093291, "user_tz": 360, "elapsed": 164, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="30119c64-ae08-4ab4-b509-5ece7680bc28"
del(prime_numbers[1])
print(prime_numbers)


# %% [markdown] id="1cqm2gTdedE8"
# Remove an element based on its value

# %% id="irybZQgKRAo8" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780436166511, "user_tz": 360, "elapsed": 175, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="da8c8323-5e61-4267-d569-b9ee09cc77b0"
prime_numbers.remove(9)
print(prime_numbers)


# %% colab={"base_uri": "https://localhost:8080/"} id="5ctHw4oaRK5X" executionInfo={"status": "ok", "timestamp": 1780436311416, "user_tz": 360, "elapsed": 876, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="c75fb27c-9e59-48ca-8ea7-d3b1e401885e"
foo = [ 1, 2, 3, 5, 5, 5, 3, 5, 5, ]
foo


# %% colab={"base_uri": "https://localhost:8080/"} id="nt5CQvyRRPRF" executionInfo={"status": "ok", "timestamp": 1780436311575, "user_tz": 360, "elapsed": 129, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="c9af346a-9df4-433b-a54f-96b9610a6527"
foo.remove(5)
foo


# %% [markdown] id="qKyWHNwvej57"
# Remove the last element from a list and use it after removing it

# %% id="wTG0AKjiRZXf" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780436355612, "user_tz": 360, "elapsed": 163, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="49a707a3-6c8c-4d66-94df-5f94cbc6a159"
last_prime = prime_numbers.pop()
print(last_prime)
print(prime_numbers)


# %% id="U-9pq-lJSWRK" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780436406274, "user_tz": 360, "elapsed": 116, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="74045b89-36f2-46a2-bd69-5e58f5de9a39"
prime_numbers.pop(0)
print(prime_numbers)


# %% [markdown] id="r10PBHeu1mfr"
# #### Your Turn
# 1. Remove the 0 from your `tens` list.
# 2. Remove the 100 from your `tens` list and save it to a variable called `removed_number`.
# 3. Use an f-string to write a message that says "I just removed `removed_number`", where `removed_number` is the 100 you removed from your `tens` list. Print our your f-string.

# %% [markdown] id="Kg0OGliiyn3J"
# ```python
# tens = [ 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, ]
# tens
# ```
#

# %% colab={"base_uri": "https://localhost:8080/"} id="fjMgBDFQS92_" executionInfo={"status": "ok", "timestamp": 1780437168631, "user_tz": 360, "elapsed": 212, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="9675fe0f-d148-4437-9c70-454f274b1c64"
tens = [ 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, ]
tens

# %% id="aPFxH2A11-Ni" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780437188606, "user_tz": 360, "elapsed": 103, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="2c59f256-1f0e-4850-b020-ab67dd19404a"
# Solution 1
del(tens[0])
tens


# %% id="mKgGNdFo1_Jw" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780437231362, "user_tz": 360, "elapsed": 96, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="2e0e9766-7340-4934-ff06-b418847205bd"
# Solution 2
removed_number = tens.pop()
removed_number


# %% colab={"base_uri": "https://localhost:8080/"} id="q2d28nmlVDh7" executionInfo={"status": "ok", "timestamp": 1780437238932, "user_tz": 360, "elapsed": 130, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="235a1934-7ffc-46ac-ded8-cabf47fa4e28"
tens


# %% id="wkLz3CfT1_z8" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780437287644, "user_tz": 360, "elapsed": 263, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="7f8fe471-4ab5-4849-b405-4416e05764ec"
# Solution 3
print(f"I just removed {removed_number}.")


# %% [markdown] id="ZFGSMEbaURX5"
# Alternate ...
#
#

# %% colab={"base_uri": "https://localhost:8080/"} id="-CuiRhxZTu23" executionInfo={"status": "ok", "timestamp": 1780437496540, "user_tz": 360, "elapsed": 98, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="429fa3a2-9ac5-4dd3-d8a0-0b3037b25221"
tens = [ 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, ]
tens


# %% colab={"base_uri": "https://localhost:8080/"} id="blUY-wQuTw5q" executionInfo={"status": "ok", "timestamp": 1780437507920, "user_tz": 360, "elapsed": 92, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="9cafe6df-cf9c-425f-debd-e65e2041b88b"
tens[1:]


# %% colab={"base_uri": "https://localhost:8080/"} id="gBXjWz17Tw0d" executionInfo={"status": "ok", "timestamp": 1780437550641, "user_tz": 360, "elapsed": 136, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="6829c3c2-0e48-4f05-b78e-eb53c285aa4d"
print(tens[-1])
print(tens[1:-1])


# %% colab={"base_uri": "https://localhost:8080/"} id="l1JyqWOaUAtr" executionInfo={"status": "ok", "timestamp": 1780437576105, "user_tz": 360, "elapsed": 188, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="12846fa5-17be-4786-e4bb-0cd1a819da49"
tens


# %% colab={"base_uri": "https://localhost:8080/"} id="omHsv9O1TwtN" executionInfo={"status": "ok", "timestamp": 1780437591727, "user_tz": 360, "elapsed": 163, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="d4b265e7-3ec8-436c-82de-a821b4c276b4"
tens = tens[1:-1]
tens


# %% [markdown] id="kLYmYgbrCj6I"
# ## Changing a List

# %% id="KJH-2s-UClkK" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780438310507, "user_tz": 360, "elapsed": 233, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="ee77776e-da89-4114-c119-42c32d15aafb"
# You can alter an element in a list using indexing
animals = ['dog', 'cat', 'rabbit', 'mouse']
animals


# %% id="5T4qjo6fR5It" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780438326521, "user_tz": 360, "elapsed": 154, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="b06096f4-dbae-4532-f4e9-f845f8d8ae14"
animals[0] = 'cow'
print(animals)


# %% id="dvjtZpFrp61T" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780438342066, "user_tz": 360, "elapsed": 172, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="98caf625-0ba4-43e9-9e42-67ef575c5776"
animals[2] = 'gerbil'
animals


# %% id="qo5ml9EBjvSi" colab={"base_uri": "https://localhost:8080/", "height": 159} executionInfo={"status": "error", "timestamp": 1780438362519, "user_tz": 360, "elapsed": 181, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="3c758547-20f2-4b38-bcd1-20105cd173dc"
animals[10] = "bird"
animals


# %% id="yv1JYnv4kP8M" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780438388543, "user_tz": 360, "elapsed": 178, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="5d0745c0-7c32-4378-8200-9c90d25978c3"
animals

# %% id="dyhWxJITj6V3" colab={"base_uri": "https://localhost:8080/", "height": 35} executionInfo={"status": "ok", "timestamp": 1780438392491, "user_tz": 360, "elapsed": 265, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="d8a94486-9455-4fea-f12e-8ca05b3b0bf2"
animals[1]

# %% id="bi_cGh97jkcm" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780438412436, "user_tz": 360, "elapsed": 147, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="272cd42e-6486-4b59-b400-99143771f841"
animals[1] = ["a", "b", "c"]
animals


# %% colab={"base_uri": "https://localhost:8080/"} id="oq1_pbGOaP2G" executionInfo={"status": "ok", "timestamp": 1780438716132, "user_tz": 360, "elapsed": 84, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="49a54620-a33f-4e6d-9618-09fc96410c06"
animals[1] = [ 1, 2, 3 ]
animals


# %% [markdown] id="z9fqacyAeyNg"
# ## Organizing a List

# %% id="06mjPfkqe0qt" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780438806496, "user_tz": 360, "elapsed": 169, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="54599e82-19ed-47ef-8c79-8b89c48bef00"
animals = ['dog', 'cat', 'rabbit', 'mouse']
animals.sort() # The sort method changes the list
print(animals)


# %% colab={"base_uri": "https://localhost:8080/"} id="K4XWipanbBB1" executionInfo={"status": "ok", "timestamp": 1780438808573, "user_tz": 360, "elapsed": 85, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="baa6c38c-a45b-4501-9b2a-f63ad8ad11ad"
animals[::-1]

# %% colab={"base_uri": "https://localhost:8080/"} id="K77Sqm5RbFKd" executionInfo={"status": "ok", "timestamp": 1780438818949, "user_tz": 360, "elapsed": 247, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="1112347f-10a2-4598-ffc8-bf9c30e4c386"
animals

# %% id="bQUwGS4ofNM7" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780438831140, "user_tz": 360, "elapsed": 150, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="3ddef059-9a25-4028-f04a-398adf58957f"
animals.sort(reverse = True) # Setting reverse = True will sort the in descending order
print(animals)


# %% id="mXZqgz8NfvqH" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780438872053, "user_tz": 360, "elapsed": 175, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="9d2a842d-0489-47ab-f7cd-c1e14244fabb"
animals = ['dog', 'cat', 'mouse', 'rabbit']
print(sorted(animals)) # The sorted() function wlil not alter the original list
print(animals)


# %% id="wFIppUZ-F3tv" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780438904266, "user_tz": 360, "elapsed": 162, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="b28adb3e-8f33-46ee-de0a-1d5e11254c1a"
animals = ['dog', 'cat', 'mouse', 'rabbit']
animals.reverse()
animals


# %% id="YdD_--btlOHq" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780438943681, "user_tz": 360, "elapsed": 163, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="98a8f009-f712-4ffd-e3f8-b4ff3aacbd7f"
animals = ['dog', 'cat', 'mouse', 'rabbit']
animals[::-1]


# %% id="Fvv2zdwVlUQk" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780438948965, "user_tz": 360, "elapsed": 138, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="cc7faa50-b10d-4435-d3a5-86476ed05536"
animals

# %% id="P-A-dVb1lim7" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780438952867, "user_tz": 360, "elapsed": 107, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="ab2629fe-b991-4363-83d4-a74de2d7f338"
sorted(animals)

# %% id="4GnRkfVCllTI" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780438954817, "user_tz": 360, "elapsed": 71, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="20a17b53-33f3-449a-edc4-f6e979ad9f3b"
animals

# %% id="0CkgNZaL5X4g" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780438969490, "user_tz": 360, "elapsed": 62, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="0e5ba07a-f9e8-47d6-a2f9-2d1224112191"
reversed(animals)


# %% id="PET7_lH-GDCF" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780438993110, "user_tz": 360, "elapsed": 91, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="ff6435f8-e914-4aee-b83b-0c199d42c0eb"
list(reversed(animals))


# %% id="OoQYth3pln_N" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780439004160, "user_tz": 360, "elapsed": 91, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="6570dc33-f52d-411c-a5aa-094a6a0d2fca"
animals


# %% [markdown] id="2ovqb_CeU3GM"
# ## Inplace as a Parameter in Python

# %% [markdown] id="vMZyYALwU41w"
# Many methods in Python have a parameter called `inplace`. This parameter determines whether or not you will overwrite the existing object. If `inplace = True`, the existing object will be overwritten. If `inplace = False`, the existing object will not be overwritten, and instead, a new updated object will be returned.  

# %% [markdown] id="XjiRVRYV2EOs"
# ### Your Turn
# Sort your `tens` list in descending order.

# %% [markdown] id="mhASB92P6MNZ"
# ```python
# tens = [ 10, 20, 30, 40, 50, 60, 70, 80, 90, ]
# tens
# ```

# %% colab={"base_uri": "https://localhost:8080/"} id="MhcqlKoRc4Qg" executionInfo={"status": "ok", "timestamp": 1780439455858, "user_tz": 360, "elapsed": 167, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="c1ed580e-8976-4086-8eab-46ea9ca1de90"
tens = [ 10, 20, 30, 40, 50, 60, 70, 80, 90, ]
tens


# %% id="v99leZeT2KVJ" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780439465368, "user_tz": 360, "elapsed": 151, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="1286ec35-9024-413a-a97b-f3d40de70ae7"
# Solution
tens.sort(reverse=True)
tens


# %% colab={"base_uri": "https://localhost:8080/"} id="KpBQbkh6dCtK" executionInfo={"status": "ok", "timestamp": 1780439479302, "user_tz": 360, "elapsed": 132, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="e274aa24-d500-45e8-e468-fbd87ded8904"
tens.sort()
tens[::-1]


# %% colab={"base_uri": "https://localhost:8080/"} id="2G8uThS2dJ4N" executionInfo={"status": "ok", "timestamp": 1780439495121, "user_tz": 360, "elapsed": 159, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="19bcb770-8148-469b-a9a0-0646210e71e5"
sorted(tens)[::-1]


# %% id="54jpp9xv72TQ" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780439510713, "user_tz": 360, "elapsed": 125, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="683e47a7-89c6-4786-e11a-019cbe0ba51d"
list(reversed(sorted(tens)))


# %% colab={"base_uri": "https://localhost:8080/"} id="EVtf2gFcddRq" executionInfo={"status": "ok", "timestamp": 1780439741062, "user_tz": 360, "elapsed": 692, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="a1243ff1-8bcf-41d4-e0ff-3bf84b0456ac"
sorted(tens, reverse=True)


# %% colab={"base_uri": "https://localhost:8080/"} id="Pq9LdyMKeGBS" executionInfo={"status": "ok", "timestamp": 1780439645524, "user_tz": 360, "elapsed": 515, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="2e8e0899-6c43-4a28-cad5-c7c7c33f7ddb"
tens

# %% id="xdJ15z1FePcy"
