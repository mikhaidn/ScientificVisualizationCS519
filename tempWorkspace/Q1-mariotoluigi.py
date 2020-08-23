import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as la
import matplotlib.image as mpimg

mario = mpimg.imread("mario_big.png")
luigi = mario.copy()

size = np.shape(mario)
for x in range(size[0]):
    for y in range(size[1]):
        if luigi[x,y][0] == 1 and luigi[x,y][1] + luigi[x,y][2] <.1:
            luigi[x,y] = np.array([0,1,0,1])
        