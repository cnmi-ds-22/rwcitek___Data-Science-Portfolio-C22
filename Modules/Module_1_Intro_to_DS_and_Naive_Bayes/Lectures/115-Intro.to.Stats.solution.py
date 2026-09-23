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

# %% [markdown] id="2ZuQyhMRBVND"
# ## Example from stats lecture

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 40, "status": "ok", "timestamp": 1780957044444, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="2cAsO8xp-jFR" outputId="98f1718b-c31f-4f53-cda9-51f71b2b892b"
samples = [85, 90, 92, 73, 95, 60, 89, 78, 99, 90]
samples


# %% [markdown] id="BVnMx7l-Brx0"
# Sum ( add up )

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 52, "status": "ok", "timestamp": 1780957069041, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="WrCTpVea-lvi" outputId="1f790e9d-5201-472b-a7dd-8befa7b92c43"
summation = 0
for value in samples:
  summation += value

summation

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 22, "status": "ok", "timestamp": 1780957080781, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="M4eEeQQlb2v9" outputId="0689c4a2-56c6-4b72-b877-561f6718e909"
sum(samples)

# %% [markdown] id="lg7nhiU4Blwy"
# Count ( len of data set )

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 8, "status": "ok", "timestamp": 1780957101338, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="t-fS0CL3-6wC" outputId="c428c66a-9861-44ec-d83f-dc2c00af8902"
len(samples)

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 34, "status": "ok", "timestamp": 1780957119431, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="sqy-rAwub6Y8" outputId="25ecc385-21a8-4ba1-9902-b55ec6935232"
count = len
count(samples)

# %% [markdown] id="lAUuP_2rBiXk"
# Mean ( average )

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 41, "status": "ok", "timestamp": 1780957138049, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="ffh6dVoCmSEk" outputId="757b86e5-956c-42c6-bf6e-54b7b34fd855"
summation/len(samples)

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 7, "status": "ok", "timestamp": 1780957145788, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="3k5q1B3X-tpn" outputId="a3411333-96e7-4476-e54c-5a2d917c266e"
summation/count(samples)

# %% [markdown] id="PTLjOD6CB28L"
# Median ( mid-point )

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 24, "status": "ok", "timestamp": 1780957160201, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="I-gq_sN3mp2m" outputId="3cfd411f-fc39-4e98-f386-87a5645e122c"
sorted(samples)

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 64, "status": "ok", "timestamp": 1780957199898, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="idLfbTHK-xZg" outputId="73532eea-82a8-4d7d-b4d9-23ff6cc23f6e"
sum(sorted(samples)[4:6])/2


# %% [markdown] id="rbs8YqvAB6tB"
# Range

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 9, "status": "ok", "timestamp": 1780957347697, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="3PIAT4YU-3j2" outputId="84aad80d-a8b9-4b30-f148-bab740e36095"
{
"min": sorted(samples)[0],
"max": sorted(samples)[-1]
}

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 47, "status": "ok", "timestamp": 1780957449817, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="8aadHNZL_KX0" outputId="90f7a7a6-4b66-4f18-fa73-ec9c9e1817df"
sorted(samples)[3:8]

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 25, "status": "ok", "timestamp": 1780957469206, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="I05GZhrefeIz" outputId="0529f7eb-8de8-4a61-b60b-98c4ccb28b54"
min(samples), max(samples)


# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 64, "status": "ok", "timestamp": 1780957488488, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="ZtjBWe5wyCks" outputId="fa0f0cef-ba9f-4d8d-eb9d-4de612590ca1"
max(samples) - min(samples)


# %% executionInfo={"elapsed": 5, "status": "ok", "timestamp": 1780957503808, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="yp7JIR4Jn6ip"
import numpy as np


# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 28, "status": "ok", "timestamp": 1780957504928, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="rUea5aFvn7lQ" outputId="4c058dd7-ecde-4b9a-94a9-08acf2bb5e30"
np.median(samples)

# %% id="gTkBm-8Nn9Gi"
