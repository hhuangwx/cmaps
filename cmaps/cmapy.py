import numpy as np
from matplotlib import colors


class Cmapy(colors.ListedColormap):
    def __init__(self, colors, name='from_list', N=None):
        '''Initialization'''
        self._colors = colors
        self._name = name
        self._N = N

        # call parent __init__
        super(Cmapy, self).__init__(self._colors, name=self._name, N=self._N)

    def __getitem__(self, item):
        return Cmapy(self._colors[item], name='sliced_' + self._name)

    def show(self):
        import matplotlib.pyplot as plt
        a = np.outer(np.ones(10), np.arange(0, 1, 0.001))
        plt.figure(figsize=(2.5, 0.5))
        plt.subplots_adjust(top=0.95, bottom=0.05, left=0.01, right=0.99)
        plt.subplot(111)
        plt.axis('off')
        plt.imshow(a, aspect='auto', cmap=self, origin='lower')
        plt.text(0.5, 0.5, self._name,
                 verticalalignment='center', horizontalalignment='center',
                 fontsize=12, transform=plt.gca().transAxes)
        plt.show()
