import numopt2.util as u
import numpy as np
import numopt2.steepest_descent as s


def main():
    x0=0.9
    x,n = s.steepest_descent(x0,u.f,u.df,0.00000001,10000)
    print (x,n)
    print (np.sqrt(2.)/2. - x)
    return 1

if __name__ == "__main__":
    main()
