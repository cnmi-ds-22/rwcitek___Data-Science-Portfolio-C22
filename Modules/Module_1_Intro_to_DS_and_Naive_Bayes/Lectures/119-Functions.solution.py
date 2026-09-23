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

# %% [markdown] id="dB8kRlVSsUHA"
# ## Why we need functions
# - Define code that only runs when you call the function
# - Allow you to run the same code multiple times without rewriting it
# - Help with DRY- Don't Repeat Yourself
# - Can create a 'black box' - you only have to know what arguments a function expects and what it gives back
#

# %% [markdown] id="v5eBC-CTVtYI"
# ### Template
#
# ```python
# def func_name ( arg1, arg2, ...):
#   ''' doc_string '''
#   { do some cool stuff }
#   return variable
# ```

# %% [markdown] id="TyCdjPZ_ttJ9"
# ## Naming conventions
#

# %% [markdown] id="2yYIHGGatw97"
# Function and argument names:
# - all lowercase
# - words shoud be seperated by underscores when needed to increase readablity  
# - describe what the function does or what the argument is
# - avoid abbreviations that would not be obvious to somebody else who knew nothing about your code
#
# **Examples:**    
# Function names: add_two_numbers, count_by_two  
# Arguments: integer1, integer2, person_name, data_frame, column_name
#
#

# %% [markdown] id="HVWifynh8AQp"
# ## Basic Function Syntax

# %% [markdown] id="7nGt0bAKspuv"
# A simple function with no arguments and no return

# %% colab={"base_uri": "https://localhost:8080/", "height": 104} executionInfo={"elapsed": 86, "status": "ok", "timestamp": 1781034128045, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="poyE65CTrb1u" outputId="2c0e8e40-8ea1-4513-f041-0eb50f566b83"
# This defines the function
def hello_world1():
  """Prints Hello world!"""
  print("Hello world!")

hello_world1

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 43, "status": "ok", "timestamp": 1781034199028, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="fdBDOKEWsJb1" outputId="6d8e3b60-c818-47bd-b79d-33dce775be57"
# This actually calls the code and runs the function
hello_world1()


# %% id="DNup1ND5XjPq" executionInfo={"status": "ok", "timestamp": 1781034214946, "user_tz": 360, "elapsed": 53, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}}
# hello_world1?

# %% id="ahovoWIZNNV4" executionInfo={"status": "ok", "timestamp": 1781034241806, "user_tz": 360, "elapsed": 35, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}}
# hello_world1??

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 45, "status": "ok", "timestamp": 1781034289456, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="hdtZmQMc9f2f" outputId="286c24b5-35ca-4ba8-84fa-0d367706c7b3"
help(hello_world1)


# %% id="ztfp5c9FNT0p" executionInfo={"status": "ok", "timestamp": 1781034300446, "user_tz": 360, "elapsed": 5, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}}
# len??

# %% [markdown] id="BOJp30QftAYm"
# A function that takes an argument

# %% colab={"base_uri": "https://localhost:8080/", "height": 104} executionInfo={"elapsed": 82, "status": "ok", "timestamp": 1781034415242, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="Amh2HLI0sL0j" outputId="24d1f2eb-963f-41da-f76b-47db8f370a03"
# This function takes the argument - name
def hello_person(name):
  """ Prints Hello name """
  print("Hello ", name)

hello_person

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 463, "status": "ok", "timestamp": 1781034476708, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="Wr9ChQp1tTSr" outputId="8b0b68fd-a960-4a7b-9ba1-b669edff6be0"
# Calling this function requires passing in a name argument
hello_person('world')
hello_person('Nicole')
hello_person('Marty')
hello_person(name = 'Dameon')

# %% id="cVo2NVahX69d" executionInfo={"status": "ok", "timestamp": 1781034531431, "user_tz": 360, "elapsed": 41, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}}
# hello_person?

# %% colab={"base_uri": "https://localhost:8080/", "height": 141} executionInfo={"elapsed": 84, "status": "error", "timestamp": 1781034552561, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="_UzDX7jDJ45e" outputId="e2c85741-00e8-489c-a76f-a48ea1c44a69"
hello_person(foo = 'Dameon')


# %% [markdown] id="KbxhUqyxtozA"
# A function that takes multiple arguments and returns something

# %% id="5n1X_-DCtfl7" executionInfo={"status": "ok", "timestamp": 1781034651675, "user_tz": 360, "elapsed": 126, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}}
# this function takes two arguments - number1 and number2
def add_two_numbers(number1, number2):
  """ Adds two numbers"""
  #then it returns the sum
  return number1+number2



# %% id="V2sSRKFqYUvg" executionInfo={"status": "ok", "timestamp": 1781034652593, "user_tz": 360, "elapsed": 24, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}}
# add_two_numbers?

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 59, "status": "ok", "timestamp": 1781034687761, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="-sTvs-uA_h_6" outputId="83d1b838-1348-4241-8542-718e6a5f0d7b"
my_sum = add_two_numbers(4, 3)
print(my_sum)

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 35, "status": "ok", "timestamp": 1781034703869, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="edmYBThut348" outputId="7c96d017-c0be-4976-f556-4bfeb4177641"
my_sum = add_two_numbers(4, number2 = 3)
print(my_sum)


# %% [markdown] id="R6RczNgeow6u"
# ### Your Turn
# Write a function called `celsius_to_fahrenheit` that takes one argument : `celsius`. Return the temperature in fahrenheit.  Be sure to include a doc_string.  Test your function with different values to verify that it works.  Hint: 0 C == 32 F.
#
#
# Note: $F = \frac{9}{5} \times C + 32$

# %% id="kklSPN2tpMfJ" executionInfo={"status": "ok", "timestamp": 1781035374780, "user_tz": 360, "elapsed": 78, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}}
# Solution
def celsius_to_fahrenheit( celsius ):
  '''Given temperature in Celsius, returns the temperature in Fahrenheit.'''
  fahrenheit = 9/5 * celsius + 32
  return fahrenheit



# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 62, "status": "ok", "timestamp": 1781035398206, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="YiRjPWrQvNOm" outputId="fb219374-7d86-4662-e8bb-2b3687e70c49"
# Solution
for c in [ -40, 0, 100 ]:
  print( c, celsius_to_fahrenheit( c ) )


# %% [markdown] id="pn7CZd3aD-_m"
# ## Doc blocks or docstrings and function help

# %% id="WZyq9iV8EQiE" executionInfo={"status": "ok", "timestamp": 1781035908802, "user_tz": 360, "elapsed": 41, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}}
def do_nothing():
  # The three double quotes denote that this is the function doc block
  """This
  function
  does
  nothing
  """


# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 36, "status": "ok", "timestamp": 1781035911899, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="e71fb2SXEckA" outputId="d84ce791-9a1b-4233-ea8c-4aba9d2ea618"
#Calling the help function on our function will return the doc block
help(do_nothing)


# %% id="2K1silxpFWBI" executionInfo={"status": "ok", "timestamp": 1781035936489, "user_tz": 360, "elapsed": 43, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}}
# Opens help for jupyter lab
# do_nothing?

# %% [markdown] id="9SIk882Y8t2v"
# ## Argument options

# %% [markdown] id="Fj6SKVypAFg5"
# ### Positional Arguments and Named Arguments
#

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 43, "status": "ok", "timestamp": 1781036535272, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="5joE0FIdIeQk" outputId="e01ae104-fda3-494e-de28-9cd6ff30e09e"
def print_inputs(input1, input2):
# Here it matches up the arguments passed by position
# The first argument will be assigned to input1
# The second argument will be assigned to input2
  print("input1 = " , input1)
  print("input2 = " , input2)


print_inputs(8,9)


# %% id="IeMZIpC9UiD7" executionInfo={"status": "ok", "timestamp": 1781036538123, "user_tz": 360, "elapsed": 28, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}}
# print_inputs?

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 47, "status": "ok", "timestamp": 1781036574737, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="LRLmTMT2c9_9" outputId="d05c5740-739a-4635-c0cd-53154da8466f"
print_inputs(input1 = 8, input2 = 9)

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 12, "status": "ok", "timestamp": 1781036604117, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="t-5nOsvtdEoi" outputId="73d137bb-a402-4dce-c11c-084b1b989fc1"
print_inputs(input2 = 9, input1 = 8 )

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 57, "status": "ok", "timestamp": 1781036624966, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="xXIh416ZUXtg" outputId="b02bef98-9b1c-408e-e8e1-af31d2fb333e"
print_inputs("Bye",input2 = "Hi")

# %% colab={"base_uri": "https://localhost:8080/"} id="-6umaJ4cEDfs" executionInfo={"status": "ok", "timestamp": 1781036768256, "user_tz": 360, "elapsed": 70, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="a552e8a5-0ae2-410b-d56f-b9442afb8c7b"
print_inputs("Bye", "Hi")


# %% colab={"base_uri": "https://localhost:8080/", "height": 106} executionInfo={"elapsed": 37, "status": "error", "timestamp": 1781036636712, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="i6OAopwElR0z" outputId="35b4a9e7-003a-4a03-e9fc-40e665ff423d"
print_inputs(input2 = "Hi","Bye")

# %% colab={"base_uri": "https://localhost:8080/", "height": 106} executionInfo={"elapsed": 37, "status": "error", "timestamp": 1781036670068, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="7mSczVWWlXK2" outputId="a9244bc8-204e-4432-fb8b-e1ef65bc4c5f"
print_inputs(input1 = "Bye","Hi")

# %% colab={"base_uri": "https://localhost:8080/", "height": 141} executionInfo={"elapsed": 39, "status": "error", "timestamp": 1781036678610, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="oVwICRVpXSaH" outputId="a46780f1-bac0-43e3-9108-7d26bcd9e518"
print_inputs(input1 = "Bye")


# %% [markdown] id="0AKyMVxAJRmK"
# ### Optional Parameters (Arguments)

# %% id="buJc0AHIJVmn" executionInfo={"status": "ok", "timestamp": 1781036854695, "user_tz": 360, "elapsed": 17, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}}
# Optional parameters have default values
# that will be used if no values is given
def greet_person(name, greeting="hi", day="Monday"):
  """
  Args:
    name:   Someone's name
    greeting: A salutation, by default "hi"
    day:     The day, by default "Monday"
  """
  print(greeting, name,  "it's", day)


# %% id="DvrhOqnSXl5Z" executionInfo={"status": "ok", "timestamp": 1781036858465, "user_tz": 360, "elapsed": 53, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}}
# greet_person?

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 38, "status": "ok", "timestamp": 1781036882748, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="84YKnJQJPkdO" outputId="35d11f46-4c1a-4dea-aa43-1a406254ed1c"
greet_person("Joe")

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 34, "status": "ok", "timestamp": 1781036914461, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="_-v7pqEg49Mv" outputId="d80ced4f-e33a-42cf-821d-27e2c662f206"
greet_person("Lewis", day="Tuesday", greeting='hola')

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 65, "status": "ok", "timestamp": 1781036934212, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="BWCpG4ZhLVPt" outputId="b4a9dac9-c74c-4c1e-99c2-ea1b8392d242"
greet_person('Bob', 'bye', 'Wednesday')

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 46, "status": "ok", "timestamp": 1781036954451, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="Rgb9f5NGbs12" outputId="7d3f0cb3-b68d-4b78-e552-eb236c1b2373"
greet_person(day="Tuesday", greeting='hola', name = "Lewis" )


# %% [markdown] id="VKLbmETMpaBq"
# ### Your Turn
# 1. Write a function called `play_tennis` that takes the following arguments:
# - `sunny` (required)
# -  `weekend` (required)
# -  `friend` (optional - give a default value of `True`)
#
# Return `True` if `sunny`, `weekend`, and `friend` are all `True`. Return `False` otherwise. Make sure to include a docstring.
#
# 2. Test your code by running the following:
# - `play_tennis(False, False, True)` (should return `False`)
# - `play_tennis(True, True)` (should return `True`)
#
#

# %% id="_Nzl2DHYFWvV" executionInfo={"status": "ok", "timestamp": 1781037358267, "user_tz": 360, "elapsed": 46, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}}
# Solution
def play_tennis( sunny, weekend, friend = True ):
  '''Want to play a nice game of tennis?'''
  if ( (sunny == True) and (weekend == True) and (friend == True) ):
    return True
  else:
    return False


# %% id="S_BrzZZuSoE6" executionInfo={"status": "ok", "timestamp": 1781037363904, "user_tz": 360, "elapsed": 37, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}}
# play_tennis??


# %% colab={"base_uri": "https://localhost:8080/"} id="4RaJl-zvFWvX" executionInfo={"status": "ok", "timestamp": 1781037385693, "user_tz": 360, "elapsed": 51, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="c73c21f7-0e59-48c6-9654-2f23e81f03da"
# Solution
play_tennis(False, False, True)

# %% colab={"base_uri": "https://localhost:8080/"} id="rLTinrKlFWvX" executionInfo={"status": "ok", "timestamp": 1781037402323, "user_tz": 360, "elapsed": 68, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="5b39ab0a-c669-4fe5-8ee9-57214641edee"
# Solution
play_tennis(True, True)


# %% id="gN12zpQ3S116" executionInfo={"status": "ok", "timestamp": 1781037497173, "user_tz": 360, "elapsed": 29, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}}
#  Alternative using all
# all?

# %% id="7Ar3qMIcFWvX" executionInfo={"status": "ok", "timestamp": 1781037567940, "user_tz": 360, "elapsed": 10, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}}
# Solution
def play_tennis( sunny, weekend, friend =  True ):
  '''Want to play a nice game of tennis?'''
  return all([ sunny, weekend, friend])


# %% executionInfo={"status": "ok", "timestamp": 1781037569672, "user_tz": 360, "elapsed": 58, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} id="k1u0kAugFwlG"
# play_tennis??


# %% colab={"base_uri": "https://localhost:8080/"} id="ZyDPeklZFWvX" executionInfo={"status": "ok", "timestamp": 1781037579068, "user_tz": 360, "elapsed": 50, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="1ac88a03-09df-418b-a849-d6abc41a5313"
# Solution
play_tennis(False, False, True)

# %% colab={"base_uri": "https://localhost:8080/"} id="9kRfggVxFWvX" executionInfo={"status": "ok", "timestamp": 1781037586602, "user_tz": 360, "elapsed": 39, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="bb83cff2-f04c-47cf-fcbc-89f029e78934"
# Solution
play_tennis(True, True)


# %% [markdown] id="vx7w8jKX9PPJ"
# ## Return options

# %% [markdown] id="afvxKXKy6I9S"
#  - `return` exits the function
#  - `return` also optionally returns a value or list, etc. (any type of object)
#  - `return` can also be used to exit the function early if certain conditions are met
#  - you can have multiple returns in a function (only the first one executed will be hit because `return` exits the function)
#  - `return` will return `None` if nothing else is specified

# %% [markdown] id="EiRbp1F09Zpx"
# ### Return early, aka short circuit
#
#

# %% id="neTTFFaX6SRm" executionInfo={"status": "ok", "timestamp": 1781037866532, "user_tz": 360, "elapsed": 29, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}}
def add_two_integers(number1, number2):
  #check if the inputs are integers
  if not ( isinstance(number1, int) and isinstance(number2, int) ):
    #return from the function if they are not integers
    return "Not a number"
    print("exiting early")
  #otherwise return the sum of the integers
  print("hello")
  return number1 + number2



# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 77, "status": "ok", "timestamp": 1781037869789, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="HNEjrXsl6gD_" outputId="7578e8d0-9830-47c9-8510-29817995de56"
print(add_two_integers("a",5))
print(add_two_integers(4,5))

results = add_two_integers(6,7)
print(results)


# %% id="fMHXcpy7LYN9" executionInfo={"status": "ok", "timestamp": 1781037933393, "user_tz": 360, "elapsed": 26, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}}
def add_two_integers(number1, number2):
  #check if the inputs are integers
  if ( isinstance(number1, int) and isinstance(number2, int) ):
    #otherwise return the sum of the integers
    return number1 + number2
    print("hello")
  #return from the function if they are not integers
  return "Not a number"



# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 48, "status": "ok", "timestamp": 1781037934328, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="l1u9jLsrddwG" outputId="e6c35751-b325-4cc5-e4c1-d1bd17d25fe4"
print(add_two_integers("a",5))
print(add_two_integers(4,5))

results = add_two_integers(6,7)
print(results)

# %% colab={"base_uri": "https://localhost:8080/"} id="OX0v89jJJEpw" executionInfo={"status": "ok", "timestamp": 1781038119493, "user_tz": 360, "elapsed": 79, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="809716fd-333a-47c3-fae5-1ff744a7cac6"
input1 = 4
input2 = 5
add_two_integers(input1, input2)

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 3446, "status": "ok", "timestamp": 1781038175046, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="PEA3LQo_gUwq" outputId="9015417f-8bd9-4e33-ac7d-76afc8522bb2"
input1 = input("Enter an integer: ")
input2 = input("Enter an integer, again: ")
print("Combined: " , add_two_integers(input1, input2))


# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 79, "status": "ok", "timestamp": 1781038183688, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="WmdwWyMFLNYN" outputId="97919733-56f0-446b-a047-70d56eb4d850"
type(input1), input1

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 4789, "status": "ok", "timestamp": 1781038283678, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="KOL0EEgKdkf3" outputId="8fdb0b92-9031-4b77-dcf0-26f7c1313cf3"
input1 = input("Enter an integer: ")
input2 = input("Enter an integer, again: ")
if input1.isdecimal() and input2.isdecimal():
  print("Combined: " , add_two_integers(int(input1), int(input2)))
else:
  print("Enter only integers")


# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 5295, "status": "ok", "timestamp": 1781038305456, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="1GSqWjXTVcE_" outputId="d90bbc5b-3bc7-4674-dcc4-3cd552690fee"
input1 = input("Enter an integer: ")
input2 = input("Enter an integer, again: ")
if input1.isnumeric() and input2.isnumeric():
  print("Combined: " , add_two_integers(int(input1), int(input2)))
else:
  print("Enter only integers")


# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 37, "status": "ok", "timestamp": 1781038382683, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="mGKHph62s1jV" outputId="cfc11647-dd43-4ffc-a849-d7c9a579e7e5"
x = print("hello")

# %% id="vgtDpIjGtLrw" executionInfo={"status": "ok", "timestamp": 1781038402703, "user_tz": 360, "elapsed": 42, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}}
x

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 45, "status": "ok", "timestamp": 1781038406662, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="L_i62otgefFH" outputId="4ae8b459-a3ab-48cb-ee18-0e0936464f34"
print(x)


# %% [markdown] id="wM9ewnTR_frq"
# ## Examples

# %% [markdown] id="DUjncql768Vm"
# ### Pig Latin

# %% [markdown] id="HFJ4gJfK7A4z"
# pig latin translator
# sentence -> pig latin
#
# first letter -> end of word add ay
#
# unless it's a vowel -> add way

# %% id="vjR6ILbr6-Pl" executionInfo={"status": "ok", "timestamp": 1781038480372, "user_tz": 360, "elapsed": 28, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}}
def pig_latin(sentence):
  """Takes a sentence and translates it to pig latin"""
  if not isinstance(sentence, str):
    return "not a string"
  words = sentence.lower().split()
  new_sentence = ""
  vowels = ["a", "e", "i", "o", "u"]
  for word in words:
    if word[0] in vowels:
      new_sentence += word + 'way '
    else:
      new_sentence += word[1:] + word[0] + 'ay '
  return new_sentence


# %% colab={"base_uri": "https://localhost:8080/", "height": 104} executionInfo={"elapsed": 49, "status": "ok", "timestamp": 1781038481426, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="O7_FQCLRenmI" outputId="6f3a0a8f-6d61-466b-ebec-8ab7c2df5457"
pig_latin

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 33, "status": "ok", "timestamp": 1781038490944, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="iz_boS6jokM1" outputId="e73a38ac-8afe-4497-b099-752f6b8e0b65"
sentence1 = "Today is Friday"
print(pig_latin(sentence1))


# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 41, "status": "ok", "timestamp": 1781038526290, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="J74PG5kqyHwP" outputId="6d3e61f8-d61b-448e-d7b7-d30d0026b56c"
print(pig_latin("Fridays are the very best day of the week"))
print(pig_latin("No, Saturdays are"))


# %% id="C7X_EspwhBj_"
