from git import Repo
import os

# Check if working directory is a clean directory
path = os.system('pwd')
repo = Repo(path)
assert not repo.is_dirty()
