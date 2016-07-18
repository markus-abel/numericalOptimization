import matplotlib.pyplot as plt
import numpy as np


def newton(x0, f, grad_f, hessian_f, stop_criterion, max_iter):
    x = x0
    del_x = 1
    iter = 0
    while del_x > stop_criterion and iter < max_iter:
        x_old = np.copy(x)
        direction = (-1)* np.dot(np.linalg.inv(hessian_f(x)), grad_f(x))
        x += direction
        iter += 1
        del_x = np.linalg.norm(x - x_old)
    return x, iter
