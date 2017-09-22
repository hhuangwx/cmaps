cmaps
=========

Make it easier to use user defined colormaps in matplotlib. Default colormaps are from NCL_ website.

.. _NCL: http://www.ncl.ucar.edu/Document/Graphics/color_table_gallery.shtml

.. image:: examples/colormaps.png


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

List the colormaps using the code in the examples::

    import cmaps
    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib
    matplotlib.rc('text', usetex=False)
    a = np.outer(np.arange(0, 1, 0.001), np.ones(10))
    plt.figure(figsize=(20, 10))
    plt.subplots_adjust(top=0.95, bottom=0.05, left=0.01, right=0.99)
    cmap_d = cmaps.cmap_dict()
    ncmaps = len(cmap_d.keys())
    nrows = 4
    for i, k in enumerate(cmap_d.keys()):
        plt.subplot(nrows, ncmaps // nrows + 1, i + 1)
        plt.axis('off')
        plt.imshow(a, aspect='auto', cmap=cmap_d[k], origin='lower')
        plt.title(k, rotation=90, fontsize=10)
        plt.title(k, fontsize=10)
    plt.savefig('colormaps.png', dpi=300)
