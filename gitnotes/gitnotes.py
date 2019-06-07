import os
import re
import git
import datetime

class GitNotes:

    def __init__(self, args):
        self.repo = self.getRepoHead(args.path)
        self.active_branch = self.getActiveBranch()
        self.getCommitNotes(args.key, args.c_count)

    def getRepoHead(self, path):
        return git.Repo(path)

    def getActiveBranch(self):
        return self.repo.head.reference

    def getCommitNotes(self, key, count):
        if count is None:
            count = 100
        n_commits = list(self.repo.iter_commits(self.active_branch.name, max_count=count))
        commit_flag = 0
        for commit in n_commits: 
            commit_match = re.search( r'^'+key+'', commit.message, re.M|re.I)
            if commit_match:
                print(commit.summary)
                commit_flag +=1
        
        if commit_flag == 0:
            print("No commits with this story/Project Id found...!")