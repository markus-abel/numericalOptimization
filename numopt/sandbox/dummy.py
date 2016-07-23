import numpy as np

a = np.arange(15).reshape(3, 5)

print(
    a,
    a.shape,
    a.ndim,
    a.dtype.name,
    a.itemsize,
    a.size,
    type(a)
)

b = np.array([6, 7, 8])

print(b, type(b))
