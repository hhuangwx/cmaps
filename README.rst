cmaps
=========

Make it easier to use user defined colormaps in matplotlib.

Users can define a environmental variable CMAP_DIR pointing to the folder containing the self-defined rgb files.


Installation::

    git clone https://github.com/hhuangwx/cmaps.git
    cd cmaps
    python setup.py install


Usage::

    import matplotlib.pyplot as plt
    import cmaps
    import numpy as np

    x = y = np.arange(-3.0, 3.01, 0.05)
    X, Y = np.meshgrid(x, y)
    Z1 = plt.mlab.bivariate_normal(X, Y, 1.0, 1.0, 0.0, 0.0)
    plt.pcolormesh(X,Y,Z1,cmap=cmaps.WhiteBlueGreenYellowRed)
    plt.colorbar()
    plt.show()
