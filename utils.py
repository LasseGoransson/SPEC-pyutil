from git import Repo
import os

# Check if working directory is a clean directory
repo = Repo(os.system('pwd'))
assert not repo.is_dirty()
