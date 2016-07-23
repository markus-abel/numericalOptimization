import numpy as np

parabola = {
    'f': lambda x: np.array(x**4 - x**2),
    'df': lambda x: np.array(4*x**3 - 2*x),
    'ddf': lambda x: np.array(12*x**2 - 2)
}

hills = {
    'f': lambda x: np.array((-1/6)*x**6 + (3/5)*x**5 + (5/4)*x**4 - (15/3)*x**3 - (4/2)*x**2 + 12*x),
    'df': lambda x: np.array(-x**5 + 3*x**4 + 5*x**3 - 15*x**2 - 4*x + 12),
    'ddf': lambda x: np.array((-5)*x**4 + 12*x**3 + 15*x**2 - 30*x - 4)
}

reversed_hills = {
    'f': lambda x: np.array((1/6)*x**6 - (3/5)*x**5 - (5/4)*x**4 + (15/3)*x**3 + (4/2)*x**2 - 12*x),
    'df': lambda x: np.array(x**5 - 3*x**4 - 5*x**3 + 15*x**2 + 4*x - 12),
    'ddf': lambda x: np.array(5*x**4 - 12*x**3 - 15*x**2 + 30*x + 4)
}
