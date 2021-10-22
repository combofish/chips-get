import math
import random


def count_interior_point(x, y, a, b, sigma=0.25):
    """
    Count the number of interior points.
    :param x:
    :param y:
    :param a:
    :param b:
    :param sigma:
    :return:
    """
    number = 0
    for i in range(len(x)):
        y_estimate = a * x[i] + b
        if abs(y_estimate - y[i]) < sigma:
            number += 1

    return number


def ransac(x, y, iters=10000, sigma=0.25, P=0.99):
    """
    y = best_a * x + best_b

    :param x:
    :param y:
    :param iters:
    :param sigma:
    :param P:
    :return:
    """
    beat_a = 0
    best_b = 0
    pre_interior_point_number = 0

    for i in range(iters):
        sample_index = random.sample(range(len(x)), 2)
        x1, y1 = x[sample_index[0]], y[sample_index[0]]
        x2, y2 = x[sample_index[1]], y[sample_index[1]]

        a = (y2 - y1) / (x2 - x1)
        b = y1 - a * x1
        interior_points_num = count_interior_point(x, y, a, b, sigma=sigma)
        if interior_points_num > pre_interior_point_number:
            iters = math.log(1 - P) / math.log(1 - math.pow(interior_points_num / len(x), 2))
            pre_interior_point_number = interior_points_num
            beat_a = a
            best_b = b

        if interior_points_num > int(len(x) /2):
            break

    return beat_a, best_b
