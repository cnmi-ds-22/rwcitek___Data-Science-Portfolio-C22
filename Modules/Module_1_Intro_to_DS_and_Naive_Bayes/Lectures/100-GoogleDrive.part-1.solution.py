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

# %% [markdown] id="uM-L6K_tGVF6"
# # Getting set up in Google Drive

# %% [markdown] id="2ZLeqkYTEGoD"
# `NN` is your cohort number.
#
# - Navigate to `My Drive`
# - Create a folder called `ddds-cohort-NN.read-only` in your `My Drive`.
# - Navigate to `Shared with Me`
# - Add the `Admin` shortcut to the `ddds-cohort-NN.read-only` folder. ( Right click on `Admin` > Organize > Add shortcut )
# - Add the `Modules` shortcut to the `ddds-cohort-NN.read-only` folder. ( Right click on `Modules` > Organize > Add shortcut )
#
#

# %% [markdown] id="g8dFXKtxJU79"
# The following code will verify that everything works.
#

# %% id="ZpH8p2eN4ep2"
# %%capture
# %%bash
apt-get update
apt-get install -y tree jq vim


# %% id="Yl1kuY6ErmIp" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1780329499041, "user_tz": 360, "elapsed": 46271, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}} outputId="0779ef5e-05c7-48b3-a978-8c89d9744273"
from google.colab import drive
drive.mount('/content/drive')


# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 128, "status": "ok", "timestamp": 1780329524449, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="GcJU31AIsg3L" outputId="c3f17f3e-7ca9-46c8-ccad-76241afc1ef6"
# !ls -la /content/


# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 1400, "status": "ok", "timestamp": 1780329543063, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="86KSAVYtIGBX" outputId="46896300-ebc9-4996-9821-303b2b2bb024"
# !ls -la /content/drive/MyDrive/ddds-cohort-21.read-only/*/


# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 114, "status": "ok", "timestamp": 1780329566747, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="c3fKBHucJe-W" outputId="5fa93064-5bb1-4611-f0dc-c9f3a6f6adcd"
# !ls -la /content/drive/MyDrive/ddds-cohort-21/*/


# %% [markdown] id="FnJhUHmfJRAj"
# Create and share the `ddds-cohort-NN` with your private Gmail account.
#
# - Navigate to `My Drive`
# - Create a folder called `ddds-cohort-NN` in your `My Drive`.
# - Right click on `ddds-cohort-NN` > Share > Share
# - Enter your private Gmail account
# - Select Editor
# - Uncheck notify
# - Click Share
#

# %% [markdown] id="axJ44aZlP_MW"
# Copy over folder structure.

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 1288, "status": "ok", "timestamp": 1780329899417, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 360} id="5l4f3Zq7IHWs" outputId="c4715fb9-bf73-411d-e56c-fdc0f36b2d13" language="bash"
#
# rsync -vaR -f"+ */" -f"- *" --chmod=ugo=rwX \
#   /content/drive/MyDrive/ddds-cohort-21.read-only/./*/ \
#   /content/drive/MyDrive/ddds-cohort-21/
#

# %% id="AxlDRKmbEqK8"
