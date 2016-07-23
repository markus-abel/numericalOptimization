import operator
import random
import numpy as np

from itertools import product


def hillclimber(x0, f, stop_criterium=0.0001, max_iter=1000, start_step_size=.5):
    """
    Hillclimb until either a local maxima is reached
    or the maximum of iteration is reached.
    """

    x = x0
    step_size = start_step_size
    iteration = 0

    while iteration < max_iter:
        steps = list(product([-step_size, 0, step_size], repeat=len(x)))
        values = [f(x+np.array(step)) for step in steps]
        index, value = max(enumerate(values), key=operator.itemgetter(1))
        iteration += 1
        if value > f(x):
            x += np.array(steps[index])
            continue
        else:
            step_size /= 2
            if step_size < stop_criterium:
                break

    return x, iteration


def shotgun_hillclimber(start_interval, f, stop_criterium=0.00001, max_iter=1000):
    """
    Meta-algotizhm built on top of the hill climbing. Restarts the hill climbing
    with random initial conditions from the `start_intverval`.
    """
    iteration = 0
    best_x = None

    while iteration < max_iter:
        iter_left = max_iter - iteration
        x0 = random_starts(start_interval)
        x, iters = hillclimber(x0, f,
                               stop_criterium=stop_criterium,
                               max_iter=iter_left,
                               start_step_size=.5)

        iteration += iters

        if not best_x:
            best_x = x
            continue
        if f(best_x) < f(x):
            best_x = x

    return x, iteration


def stochastic_hillclimb():
    """
    Selects a random neighbor, and decides (based on the amount of improvement
    in that neighbor) whether to move to that neighbor or to examine another.
    Needs 2D+ Example before implementation.
    """
    return None


def random_starts(start_interval):
    """Creates random start point from intervall"""
    return np.array([random.choice(np.linspace(
                        int(round(start_interval[0][i])),
                        int(round(start_interval[1][i])),
                        100
                      )) for i in range(len(start_interval[0]))
                     ], dtype='float64')
