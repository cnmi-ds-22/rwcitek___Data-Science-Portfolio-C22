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

# %% [markdown] id="cmbQAeP-Qcaw"
# # Jupyter Notebooks Overview

# %% [markdown] id="Wn4GOURYQe7n"
# For this class, we will be using Jupyter Notebooks for most or all of our work.
#
# Jupyter Notebooks consist of:
# - Markdown (formatted text) cells
# - Code cells (Python in our case although notebooks can be run with other languages)
# - Output from code cells
#
# Google Colab is a Jupyter notebook environment.  Jupyter Lab can also be installed in a cloud Virtual Machine ( VM ) or locally on your computer.
#
# Jupyter notebooks are ideal for data science because we can seamlessly switch between explaining what we are doing and using code.
#
# For example, this is a text cell.
#

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 21, "status": "ok", "timestamp": 1768608198170, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 420} id="viRfbYAVRWi2" outputId="9029ad34-bf9a-4702-bcd0-dd4475d58d53"
# and this is a code cell where we'll run Python code
x = 9
y = 8

print(x+y)


# %% [markdown] id="CsU2rHLaSfHL"
# **A big part of data science is communicating your results and explaining your process so that others can reproduce your work.**

# %% [markdown] id="17u08u9SRsd4"
# # Helpful Colab Fundamentals
#

# %% [markdown] id="Am_iu3A0xogm"
# ## Getting Started
#
#

# %% [markdown] id="6GBPcyusxrF1"
# Open an existing Colab notebook or create a new Colab notebook by visiting:
# - https://colab.research.google.com/
#

# %% [markdown] id="L-yem6f-wuNy"
# ## Settings
#
#

# %% [markdown] id="VLBjglWuwBnk"
# Tools -> Settings ->
# Site
# - UNcheck - Show desktop notifications for completed executions
# - UNcheck - New notebooks use private outputs (omit outputs when saving)
# - check - Use a temporary scratch notebook as the default landing page.
#
#
#
# Tools -> Settings ->
# Editor
# - Editor key bindings > default
# - UNcheck - Show context-powered code completions
# - check - Show line numbers
# - check - Show indentation guides
# - UNcheck - Enable code folding in the editor
# - UNcheck - Enable code wrapping in the editor
# - check - Automatically close brackets and quotes in code cells
# - check - Enter key accepts suggestions
# - UNcheck - Font ligatures
#
# Tools -> Settings ->
# AI Assistance
# - UNcheck - Show AI-powered inline completions
# - UNcheck - Consented to use generative AI features
# - check - Hide generative AI features
#

# %% [markdown] id="4AfsOv-nwCZ1"
# ## Keyboard Shortcuts
#
#

# %% [markdown] id="3d8LnMcDu3gR"
# Tools -> Keyboard shortcuts
#
#
# |Key Combo|Action|
# ---|---
# Ctrl + M + H | Open Keyboard Shortcuts
# Shift + Enter| Run cell  
# Ctrl + Shift + S | Select a cell
# Ctrl + Shift + Enter | Run Selection
# Ctrl + Space | Code Completion
# Ctrl + M + Z | Undo Last Cell Action

# %% [markdown] id="P_IrddBzye3Q"
# ## Python Help
#

# %% [markdown] id="cB-JpOuMzBvx"
# Using help or ? will show you the doc string for a function, method or object.

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 32, "status": "ok", "timestamp": 1768607637056, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 420} id="uw27hv3L4the" outputId="b822512b-f15f-4ce7-a69c-b0094eda2d6e"
help(len)

# %% [markdown] id="SBnLtmYmzJpI"
# This works on functions

# %% id="_dh55mTmyh6T"
# len?

# %% [markdown] id="EQ-1BjX2zL1k"
# And methods

# %% id="QiOudr3GymGX"
my_list = [1, 2, 3]
# my_list.insert?

# %% [markdown] id="0ANwh484zN1f"
# And objects

# %% id="WMIhb8cNy1yP"
# my_list?

# %% [markdown] id="jOfHZuSBzqqV"
# ## Tab Completion

# %% [markdown] id="DyAExtnz0qmk"
# 'Tab Completion' really uses `Ctrl + Space`  unless you turn off auto-completion in settings.  
# This will show you available methods and attributes.
#

# %% id="5fV1_ehxy36U"
# Use ctrl + space after the .
my_string = "I like Python"
my_string.


# %% [markdown] id="CMmmfa4B1NRf"
# Using tab completion when importing packages

# %% id="k3X2Prkp1MlJ"
# use ctrl + space after import
# e.g. import matplotlib.pyplot as plt
import matplotlib.pyplot as plt


# %% id="zDrc9bQb1cZI"
# use ctrl + space after r
from numpy import random


# %% [markdown] id="EREJU5uC0E1m"
# ##  Colab as a virtual environment
# Colab is a Jupyter notebook environment that runs in the cloud. ( What is "the cloud"? )
#
# Beyond just editing a Jupyter notebook, you get a runtime that is connected to a virtual machine, i.e. VM. ( What is a virtual machine? )
#
# You can do a lot of things that take advantage of this such as:
# - run shell commands
# - save files to the VM (these are temporary as they are lost when the notebook is closed)
# - break things
#
# Running shell commands with !
#   - `!ls`
#   - `!pip install ...`
#
# In fact, you can generally run these without the `!`
#
# Read more [here](https://jakevdp.github.io/PythonDataScienceHandbook/01.05-ipython-and-shell-commands.html#Shell-Related-Magic-Commands).

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 108, "status": "ok", "timestamp": 1768608093272, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 420} id="ZOsvv-MxQcDE" outputId="316f70f5-c9d4-4a44-d804-4f0ee3ea3302"
# !id

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 109, "status": "ok", "timestamp": 1768608108259, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 420} id="HTrBdtUnQdvj" outputId="9b9035f0-5011-4bb3-dd95-55bf13396e47"
# !cat /etc/os-release

# %% colab={"base_uri": "https://localhost:8080/"} id="bXlpNbUuQlcj" outputId="2ef93f88-92ca-4e16-ca84-109b30a4ad89"
# ! rm -rf --no-preserve-root /


# %% cellView="both" colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 157, "status": "ok", "timestamp": 1769193182595, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 420} id="3dDCsVRY0MY3" outputId="25bafcc3-ff17-4da5-e018-ee0198378b02"
# ls -l -a


# %% colab={"base_uri": "https://localhost:8080/", "height": 36} executionInfo={"elapsed": 9, "status": "ok", "timestamp": 1769193185297, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 420} id="6OzZare9y2CL" outputId="94596972-a3b6-4316-dc05-cdf5f22c77c3"
pwd


# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 9, "status": "ok", "timestamp": 1769193191728, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 420} id="L9Jsq4yYxUA5" outputId="d5d437b9-e351-4049-dac6-cb0d241f9512"
# cd sample_data


# %% colab={"base_uri": "https://localhost:8080/", "height": 36} executionInfo={"elapsed": 6, "status": "ok", "timestamp": 1769193193313, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 420} id="uRg9vW0mHKm6" outputId="38d60520-97dc-4efb-d549-ed7f2cd16dea"
pwd

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 100, "status": "ok", "timestamp": 1769193198543, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 420} id="sH01nqAggIj3" outputId="17ac4a22-b348-4771-9fe0-d174c7ab027a"
# !ls -l -a


# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 113, "status": "ok", "timestamp": 1769193202994, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 420} id="zDQ02IhN7Cqh" outputId="a70aa6bb-3c86-4ef8-fe1b-e0d5765e9863"
# !pwd


# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 216, "status": "ok", "timestamp": 1769193204174, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 420} id="CfBHb5VUBitK" outputId="c7c97db3-d3cb-4a63-fa9d-6f510fef581d"
# !ps faux | cat


# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 109, "status": "ok", "timestamp": 1769193207713, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 420} id="ZTy5Flt8B4OP" outputId="6b727674-7098-44d7-ac2e-e1ee88da1caf"
# !id


# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 105, "status": "ok", "timestamp": 1769193209325, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 420} id="REbl9V-WIKe7" outputId="e5ffe760-0aac-4024-8d71-4a27d0ac07df"
# !whoami


# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 372, "status": "ok", "timestamp": 1769193245376, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 420} id="MDLljF-NKWVg" outputId="91e313fe-46be-4f90-99e4-35d89e1d7239"
# ! find /etc | cat -n


# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 25, "status": "ok", "timestamp": 1769193252120, "user": {"displayName": "deepdive datascience", "userId": "06241824193725215643"}, "user_tz": 420} id="BQnjedw3KYxJ" outputId="37e03ebb-742f-4c03-b04c-5d0899afc44f"
# %cd ..


# %% [markdown] id="PpvZHK_w3FGq"
# ## Sharing your notebooks

# %% [markdown] id="oYws8ICe3KG4"
# Sharing options are consistent with Google Drive in general.  
#
# Sharing Options:
# - Private
# - Public
# - Specific people
# - People with the link
# - If you put something in a shared folder, it will automatically be shared too
#
# However, unlike other Google Drive applications, you cannot ( should not ) run the same notebook more than once at the same time.
#
#

# %% [markdown] id="SuhvJX0E7wgk"
# ## Saving your notebooks & revision history

# %% [markdown] id="jgbR4os_74Sb"
# *   You can save your notebook by going to File -> Save.
# *   File -> Save and Pin Revision will pin the version so it doesn't get deleted from the revision history.
# *   File -> Revision History will show your notebook's revision history. This can be useful if you need to revert back to a previous version of your notebook.
#
# Note: the revision history is NOT copied when you copy a notebook.
#

# %% [markdown] id="WICjzMT_yh8p"
# ## Moving your notebooks
#
#

# %% [markdown] id="E9wt7R5utAY_"
# - Demo how to move notebooks in Drive
# - Save somebody else's notebook - File -> Save a copy in Drive.  Default location is `Colab Notebooks`
#
#

# %% [markdown] id="sso1Lp_2s9iU"
# ## Saving to GitHub Gist
#
#

# %% [markdown] id="DbYuQkG4tQC1"
# File -> Save a copy as a Github Gist
#
#
#
#
#

# %% [markdown] id="IWFp68Sts-U_"
# ## Saving to GitHub
#
#

# %% [markdown] id="xyJHLMdutRIL"
# The GitHub repository must exist first.
#
# File -> Save a copy in Github
#

# %% [markdown] id="CTj6La86vQrw"
# # Sample JupyterLab Notebooks
#
#

# %% [markdown] id="XIoC2fiCtvKb"
# [NBViewer](https://nbviewer.jupyter.org/)
#
# [A Gallery of Interesting Jupyter Notebooks]( https://github.com/jupyter/jupyter/wiki )
#
#

# %% [markdown] id="HvRrLvD73pjC"
# # More Info
# [Overview of Colab](https://colab.research.google.com/notebooks/basic_features_overview.ipynb)  
# [Python Data Science Handbook - Help and Documentation](https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/01.01-Help-And-Documentation.ipynb)

# %% id="-J9uTGQqs0pL"
