import matplotlib.pyplot as plt
import cmaps
import numpy as np
import matplotlib

if __name__ == '__main__':
    x = y = np.arange(-3.0, 3.01, 0.05)
    X, Y = np.meshgrid(x, y)

    sigmax = sigmay = 1.0
    mux = muy = sigmaxy=0.0

    Xmu = X-mux
    Ymu = Y-muy

    rho = sigmaxy/(sigmax*sigmay)
    z = Xmu**2/sigmax**2 + Ymu**2/sigmay**2 - 2*rho*Xmu*Ymu/(sigmax*sigmay)
    denom = 2*np.pi*sigmax*sigmay*np.sqrt(1-rho**2)
    Z = np.exp(-z/(2*(1-rho**2))) / denom
    
    for i in range(2):
        fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(5, 4))
        im = ax.pcolormesh(X,Y,Z,cmap=(cmaps.WhiteBlueGreenYellowRed + cmaps.Carbone42+cmaps.MPL_spring ))
        plt.colorbar(im, ax=ax)
        ax.set_xlim(-3, 3)
        ax.set_ylim(-3, 3)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')

        plt.tight_layout()
        plt.savefig('{}.png'.format(i))
        plt.close()

    for i in range(2):
        fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(5, 4))
        im = ax.pcolormesh(X,Y,Z,cmap=(cmaps.WhiteBlueGreenYellowRed + cmaps.Carbone42.interp(200)))
        plt.colorbar(im, ax=ax)
        ax.set_xlim(-3, 3)
        ax.set_ylim(-3, 3)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')

        plt.tight_layout()
        plt.savefig('c{}.png'.format(i))
        plt.close()
        