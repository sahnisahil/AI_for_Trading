import numpy as np


####### Covariance Calculation start

x = np.array([[0, 2], [1, 1], [2, 0]]).T
np.cov(x)
# array([[ 1., -1.],
#        [-1.,  1.]])

m = np.arange(10, dtype=np.float64)
f = np.arange(10) * 2
a = np.arange(10) ** 2.
ddof = 1
w = f * a
v1 = np.sum(w)
v2 = np.sum(w * a)
m -= np.sum(m * w, axis=None, keepdims=True) / v1
cov = np.dot(m * w, m.T) * v1 / (v1**2 - ddof * v2)
np.cov(m)
x = [-2.1, -1,  4.3]
y = [3,  1.1,  0.12]
X = np.stack((x, y), axis=0)

np.cov(X)
np.cov(x, y)
np.cov(x)
####### Covariance Calculation end