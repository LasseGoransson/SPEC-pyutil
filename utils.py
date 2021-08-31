from git import Repo
import os

# Check if working directory is a clean directory
path = os.system('pwd')
repo = Repo(path)
if repo.is_dirty():
    print("This repo is dirty! Do you want to continue ?")
    input()

