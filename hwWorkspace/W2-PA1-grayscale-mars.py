import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap

mars_gray = mpimg.imread('mars.png')

# https://matplotlib.org/3.1.0/tutorials/colors/colormap-manipulation.html


mars_colordict = {'red':   [(0.0,  0.0, 0.0),
                   (0.2,  0.0, 0.14),
                   (0.75,  1.0, 1.0),
                   (1.0, 0.7, 0.7)],

         'green': [(0.0,  0.0, 0.14),
                   (0.24, 0.14, .24),
                   (0.3, .7, .7),
                   (0.4, .3, 0),
                   (1.0,  0, 0)],

         'blue':  [(0.0, 1, 1),
                   (0.28, 0.0, 0.0),
                   (1.0,  0.0, 0.0)]}


mars_colormap = LinearSegmentedColormap('mars_colormap', segmentdata= mars_colordict)

mars_red = mars_colormap(mars_gray)[:,:,0,:]
