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

# %% [markdown] id="89WN4pi7oQvg"
# # Probability
#
#

# %% [markdown] id="EmtvEvpmpVoz"
# A is an event. We read P(A) as “the probability of event A” or “the probability of A”. Note that the probability of a single event is called a **marginal probability**.
# <br />
# <br />
#
# $
# P(A) = \dfrac{\text{# of ways A can happen}}{\text{total number of outcomes}}
# $

# %% [markdown] id="poT1Nn3ioS1j"
# ## Example 1
#
#

# %% [markdown] id="xdwfEaeXoUof"
# What is the probability of pulling out a blue marble from a bag that contains 3 yellow marbles, 4 green marbles, and 2 blue marbles?
#

# %% id="-WSCTTNdjLfL" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1781025262112, "user_tz": 360, "elapsed": 35, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="cd60a629-549c-43b5-bf0d-16acac8dae46"
# Create a bag of marbles
bag = ["yellow"]*3 + ["green"]*4 + ["blue"]*2
bag


# %% id="CDwy5TO5sWZO" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1781025410225, "user_tz": 360, "elapsed": 37, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="2142d136-21cf-46bf-c4fe-08b6c674c37c"
# How many marbles in the bag?
len(bag)


# %% id="KCjNZPN-omV7" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1781025465117, "user_tz": 360, "elapsed": 15, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="3c291129-01f8-40ec-cd8b-2e0967f616ab"
sample = [ x for x in bag if x == "blue" ]
sample


# %% id="SQOT6iQesaeb" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1781025468509, "user_tz": 360, "elapsed": 9, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="52dda0ec-1d4f-4d61-f63e-c4b4d33635f2"
# How many marbles are blue?
len(sample)


# %% id="-17z5IjBofgb" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1781025483039, "user_tz": 360, "elapsed": 46, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="2e76754a-4c39-46d8-e34d-88053d1085d0"
# What is the probability of pulling out a blue marble from the bag
print(f"{len(sample)}/{len(bag)}")


# %% [markdown] id="Te6aU-1qsqAi"
# ## Example 2
#
#

# %% [markdown] id="Y9luU5xBsr7b"
# What is the probability of pulling out a non-blue marble from a bag that contains 3 yellow marbles, 4 green marbles, and 2 blue marbles?
#

# %% id="o92o0Wqjs1yt" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1781025498378, "user_tz": 360, "elapsed": 12, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="6bddd875-539d-469e-f439-85ca86e17f0d"
# Create a bag of marbles
bag = ["yellow"]*3 + ["green"]*4 + ["blue"]*2
bag


# %% id="Alz_XFZQs1yy" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1781025501111, "user_tz": 360, "elapsed": 12, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="e514d13f-9382-4343-9472-d2405a8ea613"
# How many marbles in the bag?
len(bag)


# %% id="u426piKus1yz" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1781025508708, "user_tz": 360, "elapsed": 9, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="4804ec4c-e40c-45f7-ecce-9a29dc42ac3b"
sample = [ x for x in bag if x != "blue" ]
sample


# %% id="_iUwpxf_s1y0" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1781025512557, "user_tz": 360, "elapsed": 40, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="33b74167-0c49-497c-8192-631e33a5619a"
# How many marbles are not blue?
len(sample)


# %% id="F0LNWLGFs1y1" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1781025515005, "user_tz": 360, "elapsed": 9, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="cfadf227-717f-407c-ea9a-5779aa2d47ac"
# What is the probability of pulling out a non-blue marble from the bag
print(f"{len(sample)}/{len(bag)}")


# %% [markdown] id="d-pgDKyntFvJ"
# ## Example 3
#
#

# %% [markdown] id="22eeKEUMtHdP"
# What is the probability of rolling doubles on two six-sided die?
#

# %% id="uhyz_kz1tA9n" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1781025538653, "user_tz": 360, "elapsed": 48, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="3a5f0673-5b88-4dab-d79b-a8f99e9078ca"
die_1 = list(range(1,7))
die_1


# %% id="cdRN55gntSSF" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1781025553840, "user_tz": 360, "elapsed": 31, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="6687ac09-da19-486b-ab91-aa5cf4043543"
die_2 = list(range(1,7))
die_2


# %% id="dRHSC0attfSW" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1781025582346, "user_tz": 360, "elapsed": 14, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="38e1d751-4794-47c3-d71b-9005d8472620"
# All possible rolls of two die
die_pairs = [
  (d1, d2)
    for d1 in die_1
      for d2 in die_2
]
die_pairs


# %% id="y4tPdGoftz8e" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1781025604652, "user_tz": 360, "elapsed": 56, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="8b0cee72-dc35-4e8a-9867-edea47c8d578"
# Number of possible pairs
len(die_pairs)


# %% id="GJpNNvhruBvS" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1781025633196, "user_tz": 360, "elapsed": 16, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="e0dff36a-5399-4055-961e-c706c4f2bf31"
# Doubles
doubles = [ x for x in die_pairs if x[0] == x[1] ]
doubles


# %% id="0UfB-VJouKAB" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1781025639651, "user_tz": 360, "elapsed": 24, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="4bb90d6e-2c88-4797-a7b3-edce9642b283"
# Number of doubles
len(doubles)


# %% id="X581pIUxuRx3" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1781025645954, "user_tz": 360, "elapsed": 50, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="3cb978f1-2fc4-4eb1-c55f-049f11da9969"
# What is the probability of rolling doubles on two six-sided die?
print(f"{len(doubles)}/{len(die_pairs)}")


# %% [markdown] id="sUiB1GxTuyQQ"
# ## Example 4
#
#

# %% [markdown] id="GkBrT0HSuz4C"
# What is the probability of pulling out a blue marble OR a yellow marble from a bag that contains 3 yellow marbles, 4 green marbles, and 2 blue marbles?
#

# %% id="97_ek2ZUu6C_" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1781025712929, "user_tz": 360, "elapsed": 50, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="c84c0501-258f-45aa-fb0a-7178b831de01"
# Create a bag of marbles
bag = ["yellow"]*3 + ["green"]*4 + ["blue"]*2
bag


# %% id="hOP7Zgtku6DB" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1781025718593, "user_tz": 360, "elapsed": 33, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="5eea55c1-712f-49f6-f516-c0d54d43c92b"
# How many marbles in the bag?
len(bag)


# %% id="5IjhWTt0u6DE" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1781025742151, "user_tz": 360, "elapsed": 43, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="6f4614d8-30d4-4c05-b912-44ef9ed4de01"
sample = [ x for x in bag if x == "blue" or x == "yellow" ]
sample


# %% id="H1b5Dg_Bu6DF" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1781025746086, "user_tz": 360, "elapsed": 34, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="99927de8-d012-400c-87a6-d2c1e3c42381"
# How many marbles are not blue?
len(sample)


# %% id="c03PJQrhu6DF" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1781025756665, "user_tz": 360, "elapsed": 15, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="426487b4-12f2-4cdb-8a70-620fffcf8371"
# What is the probability of pulling out a blue or yellow marble from the bag
print(f"{len(sample)}/{len(bag)}")


# %% [markdown] id="zNksW420vOFZ"
# ## Example 5
#
#

# %% [markdown] id="Qm-upJHovQh4"
# If you draw a single card from a deck of cards, what is the probability the card is either a diamond OR an ace?
#
#

# %% id="AEfPo2TSvI7p" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1781025793228, "user_tz": 360, "elapsed": 50, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="d5b0cf84-4996-4ee2-8326-0adffcb376f2"
# Create a deck
suits = "heart club diamond spade".split()
ranks = "ace 2 3 4 5 6 7 8 9 10 jack queen king".split()
deck = [
  ( rank, suit )
    for suit in suits
      for rank in ranks
]
deck


# %% colab={"base_uri": "https://localhost:8080/"} id="fLINn95OcL4m" executionInfo={"status": "ok", "timestamp": 1781026838945, "user_tz": 360, "elapsed": 22, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="f6ba2834-2100-4a1d-b564-492f4f96d74f"
deck2 = []
print("deck2:", deck2)

for x in deck[:28]:
  print(x, x[1])
  if x[1] == "diamond":
    deck2.append(x)

print("deck2:", deck2)


# %% colab={"base_uri": "https://localhost:8080/"} id="TSsL_sm9eUxZ" executionInfo={"status": "ok", "timestamp": 1781026928875, "user_tz": 360, "elapsed": 46, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="fc4c3917-c683-43a0-91ef-869cf996e3a2"
deck2 = [
  x
    for x in deck[:28]
      if x[1] == "diamond"
]

print("deck2:", deck2)


# %% colab={"base_uri": "https://localhost:8080/"} id="UDLBQoe7dqPu" executionInfo={"status": "ok", "timestamp": 1781026726493, "user_tz": 360, "elapsed": 53, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="21180189-ab2b-40a0-8aaa-bc74c8f64eaa"
for x in deck2:
  print(x)

# %% id="Uou-6MfccJXN"
[ x for x in deck ]

# %% id="jGIM8YD9vse_" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1781025804567, "user_tz": 360, "elapsed": 46, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="0f74e607-db79-401e-9707-f530661780e0"
# Total number of cards in the deck
len(deck)


# %% id="D8HPM6AfwuF6" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1781025821740, "user_tz": 360, "elapsed": 52, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="0fbc89b2-c657-4b0a-bd7b-806ab3bad8df"
# Diamonds in a deck
diamonds = [ x for x in deck if x[1] == "diamond"]
diamonds


# %% id="EsbtRBYfw4LX" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1781025829066, "user_tz": 360, "elapsed": 13, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="dfe18af8-cc91-46e3-c378-862f27089453"
# Total number of diamonds in a deck
len(diamonds)


# %% id="o-3kqpYWxF3G" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1781025838590, "user_tz": 360, "elapsed": 47, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="0c76fa5e-88f7-4e83-8531-58ed3f6b82b2"
# Aces in a deck
aces = [ x for x in deck if x[0] == "ace"]
aces


# %% id="trHGdrZqxNwG" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1781025844438, "user_tz": 360, "elapsed": 8, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="31af4020-3958-4bd2-b27c-90ddaa7bb652"
# Total number of aces in a deck
len(aces)


# %% id="ay-6oPkAxQ22" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1781025856228, "user_tz": 360, "elapsed": 27, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="a95f0ea5-394a-4546-f41f-8b7a4d6f6507"
# Cards that are both aces and diamonds
both = [ x for x in deck if x[0] == "ace" and x[1] == "diamond"]
both


# %% id="XfqAcPutxdIQ" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1781025859052, "user_tz": 360, "elapsed": 41, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="e96b648d-d582-4397-eb86-17d34c9b8f6b"
# Total number of cards that are both aces and diamonds
len(both)


# %% id="uhlRBWw8xlIk" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1781025894372, "user_tz": 360, "elapsed": 90, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="e9c87573-32a5-4425-cd99-d526385531b8"
# P(diamonds) + P(aces) - P(both)
# = len(diamonds)/len(deck) + len(aces)/len(deck) - len(both)/len(deck)
# = ( len(diamonds) + len(aces) - len(both) )/len(deck)
print (f"{( len(diamonds) + len(aces) - len(both) )}/{len(deck)}")

# %% [markdown] id="79NWUENlyiwl"
# ## Example 6
#
#

# %% [markdown] id="ZdGVWlLmynCe"
# If you roll two six-sided die, what is the probability that you roll two 5s?  
#
#

# %% id="4eIj8oV1zqDB" executionInfo={"status": "ok", "timestamp": 1781027095222, "user_tz": 360, "elapsed": 44, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}}
import itertools


# %% id="rw7Wlq2mytMv" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1781027096950, "user_tz": 360, "elapsed": 48, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="626f68f0-25d7-4e66-d069-862b12a58903"
die_1 = list(range(1,7))
die_1


# %% id="s408uNM9ytNA" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1781027099165, "user_tz": 360, "elapsed": 12, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="80bea53c-4b52-42db-930e-9449de824808"
die_2 = list(range(1,7))
die_2


# %% id="Oh5PYTJrytNB" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1781027124232, "user_tz": 360, "elapsed": 33, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="5cbf8f60-7ecd-46f0-8d9c-f32db0c5282c"
# All possible rolls of two die
die_pairs = list(itertools.product(die_1, die_2))
die_pairs


# %% id="bAh3cwvYytNB" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1781027162461, "user_tz": 360, "elapsed": 58, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="b77b9cb4-8fc4-4a4d-b91b-36fe1a0e5cce"
# Number of possible pairs
len(die_pairs)


# %% id="_X96QSKPytNC" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1781027219559, "user_tz": 360, "elapsed": 58, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="65388f07-7a27-418b-ed0f-d9a09512dae6"
# Doubles
doubles = [ x for x in die_pairs if x[0] == x[1] == 5 ]
doubles


# %% id="pBERp-rHytND" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1781027222088, "user_tz": 360, "elapsed": 32, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="c6da470f-4622-4d79-cd47-d5c7a879bfc0"
# Number of doubles
len(doubles)


# %% id="-tdAhPsjytNE" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1781027224963, "user_tz": 360, "elapsed": 43, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="055d3035-6adc-4a3b-e102-c68c8cc12508"
# What is the probability of rolling doubles on two six-sided die?
print(f"{len(doubles)}/{len(die_pairs)}")


# %% [markdown] id="IOIhSM3c0DrU"
# ## Example 7
#
#

# %% [markdown] id="oaRJdQGr0PxE"
#  A bag contains 2 orange, 3 purple and 2 yellow balls. Two of the balls are randomly drawn ***with replacement***. What is the probability that none of the balls drawn is yellow?
#

# %% id="MVhx2L6kzAmD" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1781027265798, "user_tz": 360, "elapsed": 33, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="6157ae38-f236-434a-ab2a-87269aadcd6c"
# Create a bag of balls
bag = ["orange"]*2 + ["purple"]*3 + ["yellow"]*2
bag


# %% id="OIYpPmzL0jXr" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1781027268251, "user_tz": 360, "elapsed": 61, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="bf65a4ac-db34-4975-bc8f-a781ec060ba8"
len(bag)


# %% id="Q7d86PjE0pyt" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1781027276124, "user_tz": 360, "elapsed": 59, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="d2db8819-04c2-468c-80e7-729d1e1aa963"
# Non-yellow balls
non_yellow = [ x for x in bag if x != "yellow"]
non_yellow


# %% id="bTCC914A0zr8" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1781027278751, "user_tz": 360, "elapsed": 69, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="558c7f34-61dc-46a3-cddb-2d28cb1c23b7"
len(non_yellow)


# %% id="LeMEN9Rt02Qx" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1781027305286, "user_tz": 360, "elapsed": 31, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="ccfe2d79-2975-4df3-9d73-c6d8a6d4c7bf"
# What is the probability that none of the balls drawn is yellow?
# P(non_yellow) * P(non_yellow)
# = len(non_yellow)/len(bag) * len(non_yellow)/len(bag)
# = len(non_yellow)**2/len(bag)**2
print(f"{len(non_yellow)**2}/{len(bag)**2}")

# %% id="2OCK2NXy1jNZ"
