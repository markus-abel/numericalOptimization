import numopt2.util as u
import numpy as np
import numopt2.steepest_descent as s
import numopt2.newton as new
import scipy.optimize as scopt


def main():
    print("Newton:")
    x0 = 0.9
    x, n = new.newton(x0, u.f, u.df, u.ddf, 0.00000001, 10000)
    print(x, n)
    print(np.sqrt(2.)/2. - x)
    print("Steepest Descent:")
    x0 = 0.9
    x, n = s.steepest_descent(x0, u.f, u.df, 0.00000001, 10000)
    print(x, n)
    print(np.sqrt(2.)/2. - x)
    print("scipy minimize:")
    print(scopt.minimize(u.f, x0, jac=u.df, tol=0.001))
    return 1


if __name__ == "__main__":
    main()
