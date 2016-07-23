import numpy as np


def f(x):
    return np.array(x**4-x**2)


def df(x):
    return np.array(4*x**3-2*x)


def ddf(x):
    return np.array(12*x**2-2)
