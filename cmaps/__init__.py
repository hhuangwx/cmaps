from .cmaps import Cmaps
import sys

# Create Cmaps instance and use it as module
sys.modules[__name__] = Cmaps()
