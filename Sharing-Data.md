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
A repository can have multiple branches. The first branch is called main (or master before mid 2020). 
Each branch can have a different remote. A new branch is identical to the branch it is branched from (e.g. main).
(Refer to [What is Git - A Quick Introduction to the Git Version Control System](https://www.youtube.com/watch?v=OqmSzXDrJBk) for a brief introduction into branches.)
### Detailed solution
#### Step 1
Create a private repository on a git hoster (GitHub, Bitbucket) or your institutions Git Server. 
#### Step 2
Create a new branch with
```
git checkout -b name
``` 
From now on any changes to your local repository will be applied to the new branch.
You can *checkout* the main branch (or any other existing branch) by
```
git checkout main
```
#### Step 3
 Add your private repository as the remote newly created branch by
```
git remote add name git@URL
```
You can now push your changes to your private repository and share it with someone else.

