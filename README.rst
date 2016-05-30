nclcmaps
========

Duplicate all colortables in NCL 6.3.0 to matplotlib colormaps

Thanks for wqshen_'s help

Installation::

    git clone https://github.com/hhuangmeso/nclcmaps.git
    cd nclcmaps
    python setup.py install


Usage::

    import matplotlib.pyplot as plt
    import nclcmaps
    import numpy as np

    a=np.random.rand(100,100)
    plt.pcolormesh(a,cmap=nclcmaps.cmaps('BlueDarkOrange18'))
    plt.colorbar()
    plt.show()

.. _wqshen: https://github.com/wqshen/