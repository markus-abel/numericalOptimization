import numpy as np
import scipy.optimize as scopt

from numopt import newton, steepest_descent
from numopt.functions import parabola


if __name__ == "__main__":
    print("Newton:")
    x0 = 0.9
    x, n = newton(x0, parabola['f'], parabola['df'], parabola['ddf'], 0.00000001, 10000)
    print(x, n)
    print(np.sqrt(2.)/2. - x)
    print("\nSteepest Descent:")
    x0 = 0.9
    x, n = steepest_descent(x0, parabola['f'], parabola['df'], 0.00000001, 10000)
    print(x, n)
    print(np.sqrt(2.)/2. - x)
    print("\nSciPy Minimize:")
    print(scopt.minimize(parabola['f'], x0, jac=parabola['df'], tol=0.001))
