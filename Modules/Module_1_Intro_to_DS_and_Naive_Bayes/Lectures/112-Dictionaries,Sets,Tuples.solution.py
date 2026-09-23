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

# %% [markdown] id="UM4IlHd41EfL"
# ## Types - built-in data structures - collections
# - Lists
#   - Mutable - You can change them!
#   - Indexed
#   - Ordered by index ( not by value )
#   - Values
#     - Can be anything: e.g. numbers, other lists
#     - Duplicates allowed
#   - [1, 2, 3]
# - Dictionaries
#   - Mutable
#   - Key-Value Pairs
#   - Unordered for older version of Python, Ordered for newer versions
#   - Keys
#     - Unique elements ( no duplicates )
#     - Numbers or Strings
#   - Values
#     - Anything
#   - {a:1, b:2, c:3}
#   - Use case: information for a user ( user id is key, info is value stored )
# - Sets
#   - Mutable
#   - Unordered
#   - Unique elements ( no duplicates )
#   - {1, 2, 3}
#   - Use case: determine if a particular value has been seen before
# - Tuples
#   - Unmutable - You can't change them!
#   - Ordered
#   - (1, 2, 3)
#   - Use case: returning values from a function
#

# %% [markdown] id="cw519oS5AWg2"
# For all of these collections, think [CRUD]( https://en.wikipedia.org/wiki/Create,_read,_update_and_delete ): Create, Read, Update, Delete.

# %% [markdown] id="iUQcYia-3ouT"
# ## Dictionaries

# %% [markdown] id="7UtPUmr1wGgi"
#
# - Unordered for older version of Python, Ordered for newer versions
# - Mutable - You can change what is stored in them
# - Key-Value Pairs
# - {a:1, b:2, c:3}
#

# %% [markdown] id="FpYk4THswqNP"
# Make a new dictionary

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 43, "status": "ok", "timestamp": 1780607854386, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="4m7W_rAC1B3K" outputId="36238b4d-a420-478e-8603-fe017e4314dd"
cohort_pets = {'dogs':14, 'cats': 1, 'snake': 1, 'goats': 5}
cohort_pets

# %% [markdown] id="UMEM_Pkswsa6"
# Access a value

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 47, "status": "ok", "timestamp": 1780607885038, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="JBFU5LAx3ZY2" outputId="9d8b3fa5-00b0-4fff-d51c-2ce5b810651a"
cohort_pets['dogs']

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 50, "status": "ok", "timestamp": 1780607889918, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="H4Uo9ekH3i1W" outputId="95278cb7-c408-4415-de7c-733e6d1ab6b0"
cohort_pets['cats']

# %% executionInfo={"elapsed": 3, "status": "ok", "timestamp": 1780607917358, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="q60Z-qOE3ltE"
pop_return = cohort_pets.pop('cats')

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 42, "status": "ok", "timestamp": 1780607918516, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="weWqyUoI3ymV" outputId="73a0eccd-cce8-4e0a-f2f6-4bf02f5d9355"
print(pop_return)
print(cohort_pets)

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 27, "status": "ok", "timestamp": 1780607977621, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="xC5id5ALFGHy" outputId="00c596fb-e4ea-49e2-9e19-55a471bbb0dd"
# Use .keys() to view dictionary keys
cohort_pets.keys()

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 16, "status": "ok", "timestamp": 1780608002151, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="KYPeBh-iFKYi" outputId="92aba909-0567-46b1-b5d3-0caa19ea13e5"
# Use .values() to view dictionary valus
cohort_pets.values()

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 11, "status": "ok", "timestamp": 1780608046343, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="TQrb6TaMFW3r" outputId="7e1e44ab-1e30-41a6-8942-9e666fe0c713"
# Add to your dictionary
cohort_pets['hamsters'] = 1
print(cohort_pets)

# %% [markdown] id="Pcsr-mTwc5-v"
#  You can also have nested dictionaries.  A use for a nested dictionary might be a user list with information about each user.

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 52, "status": "ok", "timestamp": 1780608158347, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="tCjosTf-dCLq" outputId="dd8111e6-5da2-4f50-8756-43d5406a5435"
users = {
    'kyla':{'first name': 'kyla', 'last name': 'bendt', 'city': 'tijeras'},
    'cliff':{'first name': 'cliff', 'last name': 'lewis', 'city': 'albuquerque'}}
users

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 28, "status": "ok", "timestamp": 1780608176557, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="i4UEW4tfpsdF" outputId="048044e1-2bff-4871-9426-1821531fe18e"
users['cliff']


# %% colab={"base_uri": "https://localhost:8080/", "height": 36} executionInfo={"elapsed": 85, "status": "ok", "timestamp": 1780608191324, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="_JPM696stZMf" outputId="f39561bc-31cd-4da0-85ae-401bec8b51fa"
users['cliff']['city']

# %% [markdown] id="gJlUjh9BDfsU"
# ### Your Turn
# Create a dictionary called `my_cohort` that uses the names of everyone in your cohort as the key and their favorite color as the value.

# %% colab={"base_uri": "https://localhost:8080/"} id="Hw7ABO5-hdPo" executionInfo={"status": "ok", "timestamp": 1780608511074, "user_tz": 360, "elapsed": 46, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="089a9a4b-3cc5-4314-f5f0-a33d74a512d0"
# Solution
my_cohort = {
  "John"   : "blue",
  "Paul"   : "yellow",
  "Ringo"  : "red",
  "George" : "violet",
}
my_cohort


# %% id="j2oPs5U7W6HE" colab={"base_uri": "https://localhost:8080/", "height": 36} executionInfo={"status": "ok", "timestamp": 1780609219350, "user_tz": 360, "elapsed": 18, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="ccd2268a-7b5b-47fb-d33b-5d0e5733af14"
names = " ".join(my_cohort.keys())
names


# %% id="5OOILu4OW7vC" colab={"base_uri": "https://localhost:8080/", "height": 36} executionInfo={"status": "ok", "timestamp": 1780609234799, "user_tz": 360, "elapsed": 51, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="4c5fff65-baa4-47bb-c7e3-d02a5422c38b"
colors = " ".join(my_cohort.values())
colors


# %% id="WxuMs5OpXayH" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780609273228, "user_tz": 360, "elapsed": 43, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="60d1dee7-f8c5-460a-c9fe-7ce1c332eea3"
zip(names.split(), colors.split())


# %% id="Oa2bXkFVW7sq" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780609290050, "user_tz": 360, "elapsed": 54, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="5e4e2270-d1ea-4e09-ab56-c4f67497fa8c"
list(zip(names.split(), colors.split()))


# %% id="Z_94aDbyW7pr" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780609323398, "user_tz": 360, "elapsed": 32, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="be9f027e-09bc-4a31-d7d8-9c2a1bf8b9ba"
dict(zip(names.split(), colors.split()))


# %% [markdown] id="GzPU8GcL4vcf"
# ## Sets

# %% [markdown] id="JrTgsl8aw841"
#   - Unordered
#   - Unique elements (no duplicates)
#   - Mutable
#   - {1, 2, 3}

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 78, "status": "ok", "timestamp": 1780609390463, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="VdLzNQ9Q4Uh8" outputId="adb2747b-3765-464d-f59f-ab3708a3a7d2"
divisible_numbers = {2,4,6,8,9,10,12,14,15,15,15,15,15}
print(divisible_numbers)


# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 44, "status": "ok", "timestamp": 1780609465313, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="VgC2O0kw5Kx9" outputId="fc2bc4c8-56a3-43ca-ae31-a4dc35adcaa6"
prime_numbers = {1,2,3,5,7,11, 'thirteen'}
print(prime_numbers)


# %% id="cErw95-XOC2h"
prime_numbers.

# %% [markdown] id="-uTiTQ6dxFCm"
# Sets are good for testing membership, overlap, etc.

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 47, "status": "ok", "timestamp": 1780609567525, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="rOkY0F3d5UYb" outputId="24ecdb9c-55c7-4f7d-f71a-9b99c84ff127"
all_numbers = prime_numbers.union(divisible_numbers)
print(all_numbers)


# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 31, "status": "ok", "timestamp": 1780609591422, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="ta5LdcgM6A1L" outputId="8e32758c-730f-4c4f-ba1b-87027b43fd5b"
all_numbers - prime_numbers


# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 45, "status": "ok", "timestamp": 1780609698785, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="LC_RS9WOuqeP" outputId="7f485a4d-a9d6-4ffa-ce87-6f47cb20bf40"
prime_numbers.issubset(all_numbers)

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 58, "status": "ok", "timestamp": 1780609744183, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="U3F0-H-58H4W" outputId="ec7732e0-8835-4e79-b7cb-6c6719c6bd81"
help(prime_numbers.issubset)

# %% [markdown] id="r9K8RYiUD2Nr"
# ### Your Turn
# 1. Create a set called `set_1` that includes the numbers: 5, 10, 15, 20, 25, 30.
# 2. Create a set called `set_2` that includes the numbers:
# 10, 20, 30, 40, 50, 60, 70, 80, 90.
# 3. Use a set **method** to return a set that includes the numbers that are in both `set_1` and `set_2`. That is, what numbers are common to both sets?<br />*Hint*: You may need to read the documentation for the set methods to figure out which one to use.  

# %% colab={"base_uri": "https://localhost:8080/"} id="WreYJyh6nfL9" executionInfo={"status": "ok", "timestamp": 1780610500608, "user_tz": 360, "elapsed": 77, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="5f65c383-04c5-40a6-9175-87d3340b6553"
# Solution 1
set_1 = { 5, 10, 15, 20, 25, 30 }
set_1


# %% colab={"base_uri": "https://localhost:8080/"} id="CilL56jDnfL-" executionInfo={"status": "ok", "timestamp": 1780610504400, "user_tz": 360, "elapsed": 13, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="778806f5-7447-43df-cc85-6f960a0118f2"
# Solution 2
set_2 = { 10, 20, 30, 40, 50, 60, 70, 80, 90 }
set_2


# %% colab={"base_uri": "https://localhost:8080/"} id="CAZ5UA0LnfL_" executionInfo={"status": "ok", "timestamp": 1780610513816, "user_tz": 360, "elapsed": 25, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="016d9d70-135a-4103-8db6-ed8ef7a509cb"
# Solution 3
set_1.intersection(set_2)


# %% id="9uxovf-F7rlx" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780610538035, "user_tz": 360, "elapsed": 49, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="953f7d38-5d47-4e18-ab98-574dd69aaecf"
set_1 - ( set_1 - set_2 )


# %% colab={"base_uri": "https://localhost:8080/"} id="Ue09xL61qQ1c" executionInfo={"status": "ok", "timestamp": 1780610601593, "user_tz": 360, "elapsed": 51, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="f0203ace-5280-49f6-a3cc-f18134fb9f0c"
set_1 & set_2


# %% [markdown] id="hmf6oBAK6gB8"
# ## Tuples
#

# %% [markdown] id="ADn-_ksKxL3P"
#   - Unmutable - You can't change them!
#   - Ordered
#   - (1, 2, 3)

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 45, "status": "ok", "timestamp": 1780611253101, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="8eRQHK6c6iov" outputId="1e3d87e9-6966-4d8c-8323-157d78ab8b59"
my_tuple = (5, 2, 3, 1, 1, 1, 4)
my_tuple


# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 55, "status": "ok", "timestamp": 1780611274878, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="m_WhpQaXzLbB" outputId="d87fd30c-309b-475c-c783-21d4b1865ed1"
my_tuple = 5, 2, 3, 1, 3, 1, 7
my_tuple


# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 34, "status": "ok", "timestamp": 1780611295574, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="zLXjWq8jQna-" outputId="89fb9eb2-0332-4af0-bf78-bd56ddc4a6ad"
my_tuple[0]


# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 32, "status": "ok", "timestamp": 1780611300219, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="bEeJ53Zm-QP0" outputId="9f7492aa-93df-4fbf-8315-8a99465990a2"
my_tuple[:3]

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 32, "status": "ok", "timestamp": 1780611329766, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="dphuWbUq-kQl" outputId="758ce646-fb8d-428f-d071-6cf5f57b8c22"
len(my_tuple)

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 44, "status": "ok", "timestamp": 1780611336508, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="Ko9UMW1r-nJ2" outputId="2c43a110-be89-4809-85b6-59c10f2a5fa3"
sorted(my_tuple)

# %% colab={"base_uri": "https://localhost:8080/", "height": 141} executionInfo={"elapsed": 41, "status": "error", "timestamp": 1780611352537, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="EOki1PEX-tuo" outputId="377ccdfa-0d81-4771-a702-6a518bd24cd1"
del(my_tuple[0])


# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 10, "status": "ok", "timestamp": 1780611362385, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="kEeUB_Ar6mTE" outputId="8b6b5771-6bfa-45b1-9c3b-f42005bace10"
my_tuple[1]

# %% id="DoM5dQsk-et-"
my_tuple.

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 39, "status": "ok", "timestamp": 1780611387197, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="k3RNGTCo6pTr" outputId="f771247b-f822-4cdd-e08f-129342423c04"
my_tuple.count(1)

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 7, "status": "ok", "timestamp": 1780611391501, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="GXi8MWee7suN" outputId="f4bea37e-051b-49bd-d8e3-2c92f500ff39"
my_tuple.index(2)

# %% executionInfo={"elapsed": 10, "status": "ok", "timestamp": 1780611409899, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="-i7XrZVUWCli"
# my_tuple.index?


# %% [markdown] id="DtQSjCw2AQ_B"
# ### Combining tuples

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 39, "status": "ok", "timestamp": 1780611424519, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="feVsaqAJ_YS-" outputId="6cb4c069-0bb7-488a-e6dc-9d77fd02f4c7"
t1 = ( 1, 2, 3 )
t2 = ( 4, 5, 6 )
t1 + t2


# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 12, "status": "ok", "timestamp": 1780611428771, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="_ognkQSD_yjn" outputId="194f9c51-2207-45a5-9e50-d8a3ed3dde23"
( t1, t2 )

# %% [markdown] id="TSU13TYAAI1e"
# ### Appending a single value to a tuple

# %% colab={"base_uri": "https://localhost:8080/", "height": 158} executionInfo={"elapsed": 35, "status": "error", "timestamp": 1780611468981, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="VqbspQgx_iq2" outputId="612ac505-7283-47f3-bc40-409f53abd6b3"
# Nope
t1 + 4

# %% colab={"base_uri": "https://localhost:8080/", "height": 158} executionInfo={"elapsed": 35, "status": "error", "timestamp": 1780611573588, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="wc_qs_fR_mSw" outputId="2f39b659-d056-4572-d4cb-3e40c8b3e3f8"
# Nope
t1 + (4)

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 48, "status": "ok", "timestamp": 1780611587144, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="stxlRzYk_tcM" outputId="0eef1b66-1f67-4384-eebc-1caac1e94b0e"
# Need a comma
t1 + (4,)

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 29, "status": "ok", "timestamp": 1780611596604, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="Zbn_LSiM83Rq" outputId="edd5a8e7-2835-4f0e-99f5-21b2537a7474"
t1

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 39, "status": "ok", "timestamp": 1780611620053, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="ZiSTUE9xW2S8" outputId="8af797b5-d8f4-4a9b-9684-16283a95ab92"
t1 = t1 + (4,)
t1

# %% id="OOcGQZQFiaQT"
t1.

# %% [markdown] id="vTrR4n5GaFfx"
# Tuples are often returned from functions/methods

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 16, "status": "ok", "timestamp": 1780611752402, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="xZF-8N1taIzs" outputId="265c7276-59ed-4b28-c0e5-962bf2659496"
x = 0.125
x.as_integer_ratio()


# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 53, "status": "ok", "timestamp": 1780611770759, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="etWX0iOg0G4I" outputId="56a3fe75-720e-4a9c-9f61-1a5f70cdb5a4"
ratio = x.as_integer_ratio()
print(ratio)
print(f"{ratio[0]}/{ratio[1]}")


# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 32, "status": "ok", "timestamp": 1780611811170, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="pbNOkTqW0HRb" outputId="0d8881f0-050b-4c1b-a724-f0bbcc69915d"
( numerator, denominator ) = x.as_integer_ratio()
print(f"{numerator}/{denominator}")


# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 66, "status": "ok", "timestamp": 1780611822829, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="iypmXxBaau52" outputId="da836f5c-030a-4649-96fd-4a7baffdae82"
print('numerator is ', numerator)


# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 36, "status": "ok", "timestamp": 1780611824393, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="hso63EvmRf85" outputId="da3a344f-e1f8-4bf2-c313-595cef033bb6"
denominator


# %% [markdown] id="ro-BYP34Eqwe"
# ### Your Turn
# 1. Create a tuple that contains the following numbers:
# 5, 10, 5, 20, 5, 30, 5, 40.
# 2. Use a tuple method to count the number of 5's in your tuple.

# %% colab={"base_uri": "https://localhost:8080/"} id="qwovrdZEwGU3" executionInfo={"status": "ok", "timestamp": 1780612115348, "user_tz": 360, "elapsed": 51, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="88738e67-cac8-4032-c06e-2ac81f1539f7"
# Solution 1
foo = (  5, 10, 5, 20, 5, 30, 5, 40 )
foo


# %% colab={"base_uri": "https://localhost:8080/"} id="oaViWGmtwGU4" executionInfo={"status": "ok", "timestamp": 1780612126514, "user_tz": 360, "elapsed": 45, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="c98f4827-5f72-4bc0-e869-36c61de84b9b"
# Solution 2
foo.count(5)


# %% [markdown] id="G6eACMjb9GFL"
# ## Further Reading:
# [WhirlwindTourOfPython - Built-In Data Structures](https://github.com/jakevdp/WhirlwindTourOfPython/blob/master/06-Built-in-Data-Structures.ipynb)
#
# For more information about lists look to the lists notebook.

# %% id="wipmytSxjBiU"
