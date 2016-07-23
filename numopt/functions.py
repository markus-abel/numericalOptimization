import numpy as np

parabola = {
    'f': lambda x: np.array(x**4-x**2),
    'df': lambda x: np.array(4*x**3-2*x),
    'ddf': lambda x: np.array(12*x**2-2)
}
