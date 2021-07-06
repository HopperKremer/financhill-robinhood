import sys
import os

from git import config
# sys.path.append("../")
sys.path.append(os.path.abspath('../'))
# from config import config
import config
import holdings
print(holdings)

print(config.USERNAME)
