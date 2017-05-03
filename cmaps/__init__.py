import numpy as np
import os
import glob
import re
from matplotlib import colors
import matplotlib.cm
from ._version import __version__

cmap_d = dict()

CMAPSFILE_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'colormaps')
USER_CMAPFILE_DIR = os.environ.get('CMAP_DIR')


def _listfname():
    cmapsflist = sorted(glob.glob(os.path.join(CMAPSFILE_DIR, '*.rgb')))
    if USER_CMAPFILE_DIR is not None:
        user_cmapsflist = sorted(
            glob.glob(os.path.join(USER_CMAPFILE_DIR, '*.rgb')))
        cmapsflist = cmapsflist + user_cmapsflist
    return cmapsflist


def _coltbl(cmap_file):
    pattern = re.compile(r'(\d\.?\d*)\s+(\d\.?\d*)\s+(\d\.?\d*)')
    with open(cmap_file) as cmap:
        cmap_buff = cmap.read()
    if re.search(r'\s*\d\.\d*', cmap_buff):
        return np.asarray(pattern.findall(cmap_buff), 'f4')
    else:
        return np.asarray(pattern.findall(cmap_buff), 'u1') / 255.


for cmap_file in _listfname():
    cname = os.path.basename(cmap_file).split('.rgb')[0]
    # start with the number will result illegal attribute
    if cname[0].isdigit():
        cname = 'N' + cname
    if '-' in cname:
        cname = cname.replace('-', '_')
    cmap = colors.ListedColormap(_coltbl(cmap_file), name=cname)
    matplotlib.cm.register_cmap(name=cname, cmap=cmap)
    cmap_d[cname] = cmap

locals().update(cmap_d)


def listcm():
    for ii in (cmap_d.keys()):
        print(ii)
