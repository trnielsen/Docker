import sys
import os

sys.path.append(os.path.abspath(
                os.path.join(os.path.split(__file__)[0], '..')))

# this line needed to fix python3 import problem
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# this is needed to adapt to the changes in Python 3.8 on Windows regarding dll loading
# see https://docs.python.org/3/whatsnew/3.8.html#ctypes
if sys.version_info >= (3, 8, 0) and sys.platform == 'win32':
    if "PATH" in os.environ:
        for p in os.environ['PATH'].split(';'):
            if p and os.path.exists(p):
                os.add_dll_directory(os.path.abspath(p))

from libBornAgainBase import *
from libBornAgainFit import *
from libBornAgainParam import *
from libBornAgainCore import *


# To prevent inclusion of plotting tools during functional tests:
if not "NOPLOT" in os.environ:
    from .plot_utils import *
