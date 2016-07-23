import numpy as np

from numopt import steepest_descent
from numopt.functions import parabola


def test_steepest_descent():
    acc = 0.0001
    max_iter = 10000
    x0 = 0.9
    x, iteration = steepest_descent(x0, parabola['f'], parabola['df'], acc, max_iter)
    assert (np.linalg.norm(x - np.sqrt(2)/2) < acc)
