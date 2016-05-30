import numpy as np
import os
import glob
import re
from matplotlib import colors
import matplotlib.cm


CMAPSFILE_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'colormaps')

USER_CMAPFILE_DIR = os.environ.get('CMAP_DIR')


class Cmaps(object):

    """docstring for Cmaps"""

    def __init__(self):
        for cmap_file in self._listfname():
            cname = os.path.basename(cmap_file).strip('.rgb')
            cmap = colors.ListedColormap(self._coltbl(cmap_file), name=cname)
            matplotlib.cm.register_cmap(name=cname, cmap=cmap)
            object.__setattr__(self, cname, cmap)

    def _listfname(self):
        cmapsflist = sorted(glob.glob(os.path.join(CMAPSFILE_DIR, '*.rgb')))
        if USER_CMAPFILE_DIR is not None:
            user_cmapsflist = sorted(
                glob.glob(os.path.join(USER_CMAPFILE_DIR, '*.rgb')))
            cmapsflist = cmapsflist+user_cmapsflist
        return cmapsflist

    def _coltbl(self, cmap_file):
        pattern = re.compile(r'(\d\.?\d*)\s+(\d\.?\d*)\s+(\d\.?\d*)\r*\n')
        with open(cmap_file) as cmap:
            cmap_buff = cmap.read()
        if re.search(r'\s*\d\.\d*', cmap_buff):
            return np.asarray(pattern.findall(cmap_buff), 'f4')
        else:
            return np.asarray(pattern.findall(cmap_buff), 'u1')/255.
