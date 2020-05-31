import numpy as np
lst = [1,5,7,10]
np.cumsum(lst)

lst = [1,5,7,10]
np.cumprod(lst)

## Covariance
x = np.array([[0, 2], [1, 1], [2, 0]]).T
np.cov(x)
# array([[ 1., -1.],
#        [-1.,  1.]])