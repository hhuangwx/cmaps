import cmaps
import numpy as np
import inspect

import matplotlib.pyplot as plt
import matplotlib
matplotlib.rc('text', usetex=False)


def list_cmaps():
    attributes = inspect.getmembers(cmaps, lambda _: not (inspect.isroutine(_)))
    colors = [_[0] for _ in attributes if
              not (_[0].startswith('__') and _[0].endswith('__'))]
    return colors


if __name__ == '__main__':
    color = list_cmaps()

    a = np.outer(np.arange(0, 1, 0.001), np.ones(10))
    plt.figure(figsize=(20, 20))
    plt.subplots_adjust(top=0.95, bottom=0.05, left=0.01, right=0.99)
    ncmaps = len(color)
    nrows = 8
    for i, k in enumerate(color):
        plt.subplot(nrows, ncmaps // nrows + 1, i + 1)
        plt.axis('off')
        plt.imshow(a, aspect='auto', cmap=getattr(cmaps, k), origin='lower')
        plt.title(k, rotation=90, fontsize=10)
        plt.title(k, fontsize=10)
    plt.savefig('colormaps.png', dpi=300)
