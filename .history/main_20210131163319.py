import sys
import os
# sys.path.append("../")
sys.path.append(os.path.abspath('../'))
from config import config

print(config.USERNAME)

import filename_without_py_extension