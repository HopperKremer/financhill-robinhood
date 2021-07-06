import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
import holdings
sys.path.append(parentdir)
import config
# sys.path.append("../")
# sys.path.append(os.path.abspath('../'))
# from config import config
# import config
print(holdings)

print(config.USERNAME)
