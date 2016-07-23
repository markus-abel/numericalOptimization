import numpy as np


def steepest_descent(x0, f, grad_f, stop_criterium=0.001, max_iter=1000):
    x = x0
    delX = 1
    iteration = 0
    alpha = 0.1

    if not delX > stop_criterium:
        print('Stop Criterium > {}'.format(delX))

    while delX > stop_criterium and iteration < max_iter:
        xalt = x
        direction = - grad_f(x)/abs(f(x))
        # x^{n+1} = x^n + ..
        x = x + update_alpha(x, f, direction)*direction
        delX = np.linalg.norm(x-xalt)
        iteration += 1

    return x, iteration


def update_alpha(x, f, direction):
    alpha = 1
    factor = .5
    while f(x + alpha * direction) >= f(x):
        alpha = factor * alpha
    return alpha
