import cmaps
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rc('text', usetex=False)
if __name__ == '__main__':
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
    # plt.tight_layout()
    plt.savefig('colormaps.png', dpi=300)
