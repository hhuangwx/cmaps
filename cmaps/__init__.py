from ._version import __version__
from .cmaps import Cmaps
import sys
sys.modules[__name__] = Cmaps()