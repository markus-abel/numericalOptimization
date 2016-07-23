import numpy as np
import scipy.optimize as scopt

from numopt import newton, steepest_descent, shotgun_hillclimber
from numopt.functions import parabola, hills

fdict = parabola


if __name__ == "__main__":
    print("Newton:")
    x0 = 0.9
    x, n = newton(x0, fdict['f'], fdict['df'], fdict['ddf'], 0.00001, 1000)
    print("Found value: {}, \tNumber of Iterations: {}".format(x, n))
    print("Error: ", np.sqrt(2.)/2. - x)
    print("\nSteepest Descent:")
    x0 = 0.9
    x, n = steepest_descent(x0, fdict['f'], fdict['df'], 0.00001, 1000)
    print("Found value: {}, \tNumber of Iterations: {}".format(x, n))
    print("Error: ", np.sqrt(2.)/2. - x)
    print("\nSciPy Minimize:")
    print(scopt.minimize(fdict['f'], x0, jac=fdict['df'], tol=0.00001))
    print("\nShotgun Hill Climber:")
    x0 = np.array([-5., ]), np.array([10., ])
    x, n = shotgun_hillclimber(x0, hills['f'], 0.0001, 10000)
    print("Found value: {}, \tNumber of Iterations: {}".format(x, n))
    print("Error: ", 3.-x)
