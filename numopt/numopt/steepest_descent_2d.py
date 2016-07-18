import numpy as np

def steepest_descent(x0, f, grad_f, stop_criterion, max_iter):
    x = x0
    iter = 0
    del_x = 1
    while del_x > stop_criterion and iter < max_iter:
        x_old = np.copy(x)
        direction = (-1)*grad_f(x)/np.linalg.norm(grad_f(x))
        alpha = update_alpha(x, f, direction)
        x += alpha*direction
        del_x = abs(np.linalg.norm(x) - np.linalg.norm(x_old))
        iter += 1
    return x, iter

def update_alpha(x, f, direction):
    alpha = 1
    factor = 0.5
    while f(x + alpha*direction) >= f(x):
        alpha *= factor
    return alpha