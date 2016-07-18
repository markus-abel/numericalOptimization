import numpy as np


def steepest_descent(x0,f,grad_f,stop_criterium,max_iter):

    x=x0
    # teste, ob delX > stopCriterium
    delX = 1
    iter=0
    alpha=0.1
    while delX > stop_criterium and iter< max_iter:
        xalt=x
        direction= - grad_f(x)/abs(f(x))
        #x^{n+1} = x^n + ..
        x = x + alpha*direction
        delX = np.linalg.norm(x-xalt)
        iter = iter + 1

    return x,iter
