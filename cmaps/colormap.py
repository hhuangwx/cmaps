#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
from matplotlib import colors

class Colormap(colors.ListedColormap):
    def __init__(self, c, name='from_list', n=None):
        '''Initialization'''
        self._colors = c
        self._name = name
        if n is None:
            self._N = len(c)
        else:
            self._N = n

        # call parent __init__
        super(Colormap, self).__init__(self._colors, name=self._name, N=self._N)


    def __getitem__(self, item):
        return Colormap(self._colors[item], name='sliced_' + self._name)
    

    def __add__(self, o):
        ''' Adding two objects '''
        return Colormap(np.vstack([self.colors, o.colors]), self.name+'_' +o.name)
    

    def interp(self, lutsize:int):
        '''
        different from resampled of the new version of matplotlib (we interp colors here)
        '''
        r, g, b = self._colors[:, 0], self._colors[:, 1], self._colors[:, 2]
        x_n = np.linspace(0., 1., lutsize)
        x_o = np.linspace(0., 1., self._N)
        
        colors_new = np.hstack([np.interp(x_n, x_o, _).reshape(-1, 1) for _ in [r, g, b]]) 
        return Colormap(colors_new, name='interp_' + self._name)
    

    def to_seg(self, N=None):
        if N is None:
            N = len(self._colors)
        return colors.LinearSegmentedColormap.from_list('seg_' +self._name, self._colors, N=N)


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


    def to_plotly(self):
        cmap = list()
        for c in self._colors:
            r, g, b = c
            cmap.append('rgb({:.0f},{:.0f},{:.0f})'.format(r*255, g*255, b*255))
        return(cmap)


    @property
    def plotly(self):
        return self.to_plotly()
