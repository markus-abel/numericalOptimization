import numpy as np

def fibonacci(n):
    a=1
    b=1
    for i in range(n):
        a,b = b,a+b
    return a,b


def test():
    print ("hallo")
    for i in (1,2,'hallo'):
        print (i)
    return


if __name__=='__main__':
    a,b = fibonacci(10)
    print ( np.asarray(a) )
    test()
