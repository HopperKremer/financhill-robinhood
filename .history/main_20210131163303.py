import sys
import os
sys.path.append("../")
from config import config

print(config.USERNAME)

sys.path.append(os.path.abspath('../other_sub_dir'))
import filename_without_py_extension