import numpy as np

def f(x):
    return x**4 - x**2


def deriv_f(x):
    return 4*x**3 - 2*x

def deriv_2_f(x):
    return 12*x**2 - 2

def g(x):
    return np.sum(np.power(x, 2))

def grad_g(x):
    return 2*x

def hessian_g(x):
    return np.array([[2., 0], [0, 2.]])
