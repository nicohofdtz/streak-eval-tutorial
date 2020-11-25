## Sharing your evaluation with coworkers

### Precondition
If you've worked through the streak evaluation tutorial and applied the methods and functions you've learned to your own data and want to share your progress with a colleague.
OR
You've encountered a problem while working on the tutorial and need help.

### Problem
You can not push your changes to the streak-eval-tutorial repository as that is read-only. It's also public and therefor inadequate for your unpublished scientific results.

### Solution approach
Create a branch and push this branch to a private repository. Then give read-only or write access to the coworker(s) that you want to share your progress with. 

### Background
Different from the well know file hosting services (e.g. Dropbox), your local copy of a git repository is not automatically synchronised with its remote (the copy repository that resides on a server of a git host e.g. GitHub).
Instead you trigger the sync progress manually with the push and pull commands.
A repository can have multiple branches. The first branch is called main (or master before mid 2020). A new branch can be created with
'''
git checkout -b name
''' 
The new branch is identical to the branch it is branched from (here main). Any changes to your local repository are now applied to the new branch.
You can *checkout* the main branch (or any other existing branch) by
'''
git checkout main
'''
Each branch can have a different remote. You can add your private repository as the remote newly created branch by
'''
git remote add name git@URL
'''
You can now push your changes to your private repository and share it with someone else.

### Detailed solution
####Step 1
Create a private repos
