import numpy as np

from numopt import newton
from numopt.functions import parabola


def test_newton():
    acc = 0.0001
    x0 = 0.9
    x, iterartaion = newton(
        x0, parabola['f'], parabola['df'], parabola['ddf'], acc
    )
    assert (np.linalg.norm(x - np.sqrt(2)/2) < acc)
