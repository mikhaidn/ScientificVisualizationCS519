import numpy as np
import numpy.linalg as la

# Given:
#  csrgb (numpy array length 3) - RGB color

# Output: (define only)
#  cxyz - product of Msrgb^-1 and csrgb

# hardcoded msrgb values are from:
#  https://www.coursera.org/learn/cs-519/lecture/Omhsq/the-srgb-color-space
#  ~6:05
minv= np.array([[.412391,.357584,.180481],
                [.212639,.715169,.072192],
                [0.019331,.119195,.950532]])

cxyz = np.matmul(minv,csrgb)
