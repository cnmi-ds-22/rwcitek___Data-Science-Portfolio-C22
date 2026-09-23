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

# %% [markdown] id="qPjcJWFYa_UR"
# # Prompt Engineering: Part 1
#
#

# %% [markdown] id="jXnWtlpArV-w"
# ## An Introduction to using Generative AI ( GenAI )
#
# - OpenAI: [ChatGPT]( https://chatgpt.com/ )
# - Google: [Gemini]( https://gemini.google.com/ )
# - Perplexity: [perplexity.ai]( https://www.perplexity.ai/ )
#
#

# %% [markdown] id="xMpUJ089rUpi"
# ## Using Generative AI: legal
#
# - ChatGPT
#   - [Terms of Use]( https://openai.com/policies/terms-of-use/ )
#   - [Privacy Policy]( https://openai.com/policies/privacy-policy/ )
#   - [Data Privacy]( https://help.openai.com/en/articles/5722486-how-your-data-is-used-to-improve-model-performance )
#
# - Gemini
#   - [Terms of Service]( https://policies.google.com/terms )
#   - [Generative AI Prohibited Use Policy]( https://policies.google.com/terms/generative-ai/use-policy )
#
# - Perplexity
#   - [Data Privacy]( https://www.perplexity.ai/hub/legal/privacy-policy )
#   - [Terms of Service]( https://www.perplexity.ai/hub/legal/terms-of-service )
#
#
# Each service has a clause that expresses that you cannot represent the output as your own. Using ChatGPT as an example:
#
# - open their [Terms of Use]( https://openai.com/policies/terms-of-use/ )
# - search for 'human-generated'
# - right click
# - click "copy link to highlighted"
#
# [You should get this link]( https://openai.com/policies/terms-of-use/#:~:text=Represent%20that%20Output%20was%20human%2Dgenerated%20when%20it%20was%20not. )
#
#
#

# %% [markdown] id="7VjBFWtDuxp7"
# ### Your Turn
#
# Pick one of the other services and find the phrase expressing how to represent its output.
#
# - { paste link here }
#
#

# %% [markdown] id="fptsj6I5u2RV"
#
#
# Other items to look for in the legal docs:
# - how they collect and use your data
# - what else you can and cannot do with their service
#
#
#
#

# %% [markdown] id="l-OtIaeRrSqk"
# ## The Art and Science of Prompting
#
# Generative AI can create lots of different content, including text, images, audio, and video by using prompts.
#
# - Prompt as a set of instructions
#   - Ask questions
#     - [What is the capital of France?]( https://gemini.google.com/share/705091fd644b )
#   - Give commands
#     - [Create a recipe for apple pie.]( https://gemini.google.com/share/730d7c390a35 )
#
# - Hallucinations
#   - Answers are not allways correct
#     - [How many i's]( https://chatgpt.com/share/4162476d-ef1b-4e2b-947b-330cf0d64154 )
#
#   - Can be convinced to please you
#     - [Explain how many i's]( https://chatgpt.com/share/527f4e6e-0ccb-41df-a1c3-d6b85104e829 )
#
#   - Not so obvious in a foreign field
#     - [CAGR vs geometric mean]( https://chatgpt.com/share/261dbb79-2a0a-4c8f-b1b4-e10f3a46c1f4 )
#
#

# %% [markdown] id="p2VryECv10E-"
# ## As a learning tool
#
# - Prompt Engineering
#   - The art and science of designing effective instructions
#
# - Features of a well designed prompt
#   - Role: assigning a persona
#   - Task: specific action
#   - Context: background information
#   - Format: desired output
#
#   Example: [Python help from a perl programmer]( https://gemini.google.com/share/3267bd13d020 )
#
#
#

# %% [markdown] id="6un4ssqB98HS"
# ### Your Turn
#
# Create a prompt for your GenAI tool using the four features: Role, Task, Context, Format.
#
# - { link to your conversation }
#
#
#

# %% [markdown] id="-HPZyWRgCaK8"
# ## Viewing output
#
# The output from Gemini, ChatGPT, and likely others can be copied as Markdown.
#
#

# %% [markdown] id="U-iGfPs6FgfS"
# Copied from Gemini
#
# ---
#
# Oh, look at you, joining the ranks of the "significant whitespace" enthusiasts. I suppose it was only a matter of time before the allure of readable code lured you away from the glorious, semi-colon-infused chaos of a real language like Perl.
#
# In Perl, we have dignity. We have `print "Hello, world!\n";`. We have the freedom to do things in fourteen different ways, half of which involve regex symbols that look like a cat stepped on the keyboard.
#
# But no, you want Python. The language that's basically just executable pseudocode for people who find curly braces "intimidating." Fine. Since your deadline is breathing down your neck, I’ll spare you the lecture on why `$!`, `@_`, and `$_` are the peak of linguistic expression.
#
# Here is your "Hello World" in Python. Note the lack of a trailing semicolon. It feels naked, doesn't it?
#
# ```python
# print("Hello, world!")
#
# ```
#
# ### A few things to keep in mind:
#
# * **No Semicolons:** If you put one at the end, Python won't explode, but it will judge you silently.
# * **The Parentheses:** In Python 2, you could just say `print "stuff"`. In Python 3, it’s a function. You need the parens. Progress, I guess?
# * **The Newline:** Unlike some lower-level languages, Python’s `print()` appends a newline by default. It assumes you’re too tired to type `\n`.
#
# ---
#
# Would you like me to show you how to do something slightly more "complex," like adding two numbers or perhaps explaining why indentation is now your new legal deity?
#
# ---
#
# End of Copy from Gemini
#

# %% [markdown] id="4Ykosy5gFaE4"
# ## Formatting input using Markdown
#
# Input can also be in the form of Markdown to provide structure to your prompt.
#
# - [Snarky perl as markdown]( https://gemini.google.com/share/e468ea254eef )
#
#
#

# %% id="RPYgY0b1rP1i"
