import numopt2.util as u
import numpy as np
import numopt2.steepest_descent as s
import numopt2.newton as new


def main():
    x0=0.9
    x,n = s.steepest_descent(x0,u.f,u.df)
    print (x,n)
    print (np.sqrt(2.)/2. - x)
    x, n = new.newton(x0,u.f,u.df,u.ddf)
    print(x, n)
    print(np.sqrt(2.) / 2. - x)

    return 1

if __name__ == "__main__":
    main()
