from git import Repo
import os

# Check if working directory is a clean directory
path = os.system('pwd')
repo = Repo(path)
print(repo.is_dirty())
assert not repo.is_dirty()

