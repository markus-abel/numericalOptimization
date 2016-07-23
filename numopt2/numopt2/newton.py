import numpy as np


def newton(x0, f, grad_f, hesse, stop_criterium=0.001, max_iter=1000):
    x = x0
    iteration = 0
    alpha = 0.1
    delX = 1

    if not delX > stop_criterium:
        print('Stop Criterium > {}'.format(delX))

    while delX > stop_criterium and iteration < max_iter:
        xalt = x
        direction = - grad_f(x) * inverse_hesse(hesse(x))
        alpha = update_alpha(x, f, direction)
        # x^{n+1} = x^n + ..
        x = x + alpha*direction
        delX = np.linalg.norm(x-xalt)
        iteration += 1

    return x, iteration


def inverse_hesse(hesse):
    if type(hesse) == np.array:
        return np.linalg.inv(hesse)
    else:
        return 1. / hesse


def update_alpha(x, f, direction):
    alpha = 1
    factor = .5
    while f(x + alpha * direction) >= f(x):
        alpha = factor * alpha
    return alpha
