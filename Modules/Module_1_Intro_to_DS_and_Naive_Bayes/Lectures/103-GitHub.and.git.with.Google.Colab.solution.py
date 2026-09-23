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

# %% [markdown] id="xkLcAZJwoHdv"
# # Github
#

# %% [markdown] id="TccfUl1agYhu"
# ## Create a Repo on Github
# 1. Go to your [GitHub Repositories](https://github.com/rwcitek?tab=repositories).
# 1. Click the New button on the top right.
# 1. Select an owner.
# 1. Create a name for your repo. You can make it public or private.
# 1. Check the box that says Add a README file.
# 1. Click Create repository.

# %% [markdown] id="CzwxwZ89ghAB"
# ## Edit README
#

# %% [markdown] id="sGM3QDoigi4g"
# 1. Click the pencil icon ( edit button )
# 1. Add a line saying "Line 1"
# 1. Click the green "Commit changes ..." button
# 1. Enter a message and/or description
# 1. Click the green "Commit changes" button
# 1. Repeat this process five more times, changing the text that you enter each time.
#
# You should now have a README with six lines at the bottom reading
#
# > Line 1<br />
# > Line 2<br />
# > Line 3<br />
# > Line 4<br />
# > Line 5<br />
# > Line 6<br />
#
#
#

# %% [markdown] id="k8XnpRbUBj9O"
# ## Branches

# %% [markdown] id="6Jne9jAeBpj6"
# ### Create a branch
#

# %% [markdown] id="VefXvp_akGTN"
# 1. Click on the Code tab
# 1. Click on the branch dropdown button.  It likely will say "main"
# 1. Type a new name called "my_branch"
# 1. Click Create Branch
# 1. Click Insights
# 1. Click Network to view the branches
# 1. Click on the Code tab
# 1. Click on the branch dropdown button.
# 1. Select my_branch
#
#

# %% [markdown] id="KNvYSm_xBpXm"
# ### Edit the README file
#

# %% [markdown] id="7p2rJXtzlC73"
# Repeat the edit process above to add two more lines so that at the bottome it looks like this:
#
# > Line 7<br />
# > Line 8<br />
#
#
#

# %% [markdown] id="rwMw_LA8lv-3"
# ### View the branches
#

# %% [markdown] id="W_p50yWwl2wk"
# 1. Click Insights
# 1. Click Network to view the branches
#
# Notice that my_branch is ahead of the main branch.

# %% [markdown] id="uGKAZl5LB05V"
# ### Delete Branch

# %% [markdown] id="tDyGZiLTl5uv"
# 1. Click the Code tab
# 1. Click the Branches button ( right next to the drop down )
# 1. Click the Trash button for my_branch.  Deletion is instant; no confirmation.
# 1. Click the Code tab
# 1. View the README file
# 1. View the branches
#

# %% [markdown] id="YXOXga8Ovvja"
# ## Revert back to a previous commit on GitHub
#
#

# %% [markdown] id="YeS_glFQwG7r"
# Unfortunately, there's no easy way to revert a commit within GitHub.  Instead, you have to use branching and then rename the branches.  These steps assume you want to revert a commit on the default branch ( i.e. main ).
#
#

# %% [markdown] id="AOxnBhFl3RUQ"
# ### On Default Branch
#
#

# %% [markdown] id="jhgRYhpT3T0h"
# #### Create a New Branch
# 1. Click on Insights
# 1. Click on Network
# 1. Click on the previous commit
# 1. Click Browse Files
# 1. Click the button to change branches
# 1. Enter a new name ( e.g. main-new )
# 1. Click Create Branch
#

# %% [markdown] id="YBuEQ2NI3U-w"
# #### Rename Old Branch
# 1. Click Settings
# 1. Scroll down to Default Branch
# 1. Click the double arrows change to other branch as default
# 1. From the dropdown, select main-new
# 1. Click Update
# 1. Click I understand ...
#
#
#
#

# %% [markdown] id="GhK6xv523gKc"
# #### Delete old branch, rename New Branch
# 1. Click Code
# 1. Click Branches
# 1. Click the trash icon for the main branch
# 1. Click the elipses for the main-new branch
# 1. Select Rename branch
# 1. Change name to main
# 1. Click Rename branch
# 1. Click the Code tab
# 1. Click I got it
#
# You have reverted to the previous commit in the main branch.
#
#

# %% [markdown] id="DQT1Onkp3e-G"
# ### On Non-Default Branch
#
#

# %% [markdown] id="MKoNZXWe3d1T"
# #### Create a Non-Default Branch ( if doesn't exist )
# 1. Click on the branch dropdown button.  It likely will say "main"
# 1. Type a new name called "my_branch"
# 1. Click Create Branch
#
#

# %% [markdown] id="lHM-EDfUWtdj"
#
# #### Rename Non-Default Branch
# 1. Click Branches
# 1. Click the elipses on the same line as the non-default branch
# 1. Click Rename Branch
#

# %% [markdown] id="kG5JIGfn3cqC"
# #### Create a new branch
# 1. Click on Insights
# 1. Click on Network
# 1. Click on the previous commit
# 1. Click Browse Files
# 1. Click the button to change branches
# 1. Enter a new name
# 1. Click Create Branch
#
#

# %% [markdown] id="KQoIiBMC3aca"
# #### Remove Old Branch
# 1. Click the trash can to remove the old branch
#
#
#
#
#
#
#
#
#

# %% [markdown] id="CJjRdNqG_adL"
# ## Fork an existing project in GitHub
#
#

# %% [markdown] id="hVqxmrLmAtyg"
# ### Fork a project
#
#
# https://github.com/rwcitek/job-sites-and-listings

# %% [markdown] id="6V7PR7qZA3kf"
# ### Make a change and commit
#
# Update the page with a job posting site or an employer site:
#
# `job-sites-and-listings/blob/main/posting.employer.sites/job.listings.sites.md`
#

# %% [markdown] id="Hi2HrH5wA4z8"
# ### Issue a Pull Request
#
# Send a Pull Request back to the repo that you forked.

# %% [markdown] id="HddZgNf-__AB"
# ## Git
# - Version Control System for text-based files
# - Keeps track of changes made by who and when
# - Repository
#

# %% [markdown] id="M2Emg137pDBT"
# ## Resources
#
# **Free Courses**
#
# - [Udacity - Version Control with Git](https://www.udacity.com/course/version-control-with-git--ud123)
#
# - LinkedIn Learning
#   - [Learning Git and GitHub]( https://www.linkedin.com/learning/learning-git-and-github-14213624/ )
#   - [Learning GitHub]( https://www.linkedin.com/learning/learning-github-18719601/ )
#   - [Git Essential Training]( https://www.linkedin.com/learning/git-essential-training-19417064/ )
#
#
# **Books**
# - [pro git from git website](https://git-scm.com/book/en/v2)
# - [Introducing GitHub, 2nd Edition](https://learning.oreilly.com/library/view/introducing-github-2nd/9781491981801/)
#
#
# **Videos**
# - [Git Tutorials - playlist](https://www.youtube.com/playlist?list=PL-osiE80TeTuRUfjRe54Eea17-YfnOOAx)
#
#
# **O'Reilly**
# - [GitHub](https://learning.oreilly.com/topics/github/)
#
#
# My presentations
# - [ GitHub demo]( https://rwcitek.github.io/gh-slides/slides/github-demo/#/1 )
#
#
#
#
