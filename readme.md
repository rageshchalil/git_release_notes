
# Reference: 
    https://gitpython.readthedocs.io/en/stable/tutorial.html#the-commit-object

# Installation: 
  
```
pip install gitpython
```
 
https://gitpython.readthedocs.io/en/stable/intro.html

# Prerequisites: 
   The commit title should follow the structure as below:

	<Ticket number>: <subject of commit>
  	eg: ABCD-1: Title of git commit

# Usage: 
 python git_notes.py
 
# Options:
	Retrive Git commit as release notes.
	optional arguments:
  		-h, --help            show this help message and exit
  		-p PATH, --path PATH  The path of the repository)
  		-k KEY, --key KEY     The Story/Project id/key from Jira)
  		-c C_COUNT, --c_count The count of commits to search for)
