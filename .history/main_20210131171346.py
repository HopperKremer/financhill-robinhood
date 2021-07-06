import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
 
from common import a
from git import config
# sys.path.append("../")
# sys.path.append(os.path.abspath('../'))
# from config import config
# import config
import holdings
print(holdings)

print(config.USERNAME)
