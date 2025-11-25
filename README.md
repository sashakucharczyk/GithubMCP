# GithubMCP
Test to use Github as a micro-MCP for coding agents from the major LLM providers. 

# Design
Creating a folder structure to see if tools and/or repeated actions can be added to Github that a coding agent can follow. Each folder should have its own relevant:

* Summary that covers what the folder is for
* Instructions on how to interact with each tool and/or file in the folder
* All relevant information/data that might be wanted for the file/folder

# Intended Use

1 - Generic parent branch. Parent has some folders, generic tools, and a descriptor/summary file.
2 - Branch parent for targeted use.
3 - Add relevant additional details/files in the branch.
4 - Run a coding agent (Ex: Codex), with specific instructions, targeting the branch

# Why
Setting up a whole agent environment can be time and resource consuming. Further, it takes extra skillsets that not everyone has. If this works, it should allow for repeated activities to be done via simple agents.