import numpy as np


def newton(x0,f,grad_f,hesse,stop_criterium=0.001,max_iter=1000):

    x=x0
    # teste, ob delX > stopCriterium
    delX = 1
    iter=0
    alpha=0.1
    while delX > stop_criterium and iter< max_iter:
        xalt=x

        direction= - grad_f(x)*inverse(hesse(x))
        alpha = update_alpha(x,f,direction)
        #x^{n+1} = x^n + ..
        x = x + alpha*direction
        delX = np.linalg.norm(x-xalt)
        iter = iter + 1

    return x,iter


def inverse(hesse):
    if type(hesse) == np.array:
        return np.inv(hesse)
    else:
        return 1. / hesse


def update_alpha(x,f,direction):
    alpha = 1
    factor = 0.5
    while f(x+alpha*direction) >= f(x):
        alpha=factor*alpha
    return alpha

