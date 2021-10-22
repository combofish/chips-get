# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random

import matplotlib.pyplot as plt
import numpy as np

from ransac import ransac


def random_data(num_size):
    x = np.linspace(0, 10, num_size)
    y = 3 * x + 10

    random_x = []
    random_y = []

    for i in range(num_size):
        random_x.append(x[i] + random.uniform(-0.5, 0.5))
        random_y.append(y[i] + random.uniform(-0.5, 0.5))

    for i in range(num_size):
        random_x.append(random.uniform(0, 10))
        random_y.append(random.uniform(10, 40))

    random_x = np.array(random_x)
    random_y = np.array(random_y)

    return random_x, random_y


if __name__ == '__main__':
    num_size = 100
    random_x, random_y = random_data(num_size=num_size)
    a, b = ransac(random_x, random_y,
                  iters=10000,
                  sigma=0.25,
                  P=0.99)
    y_estimate = a * random_x + b

    fig = plt.figure()
    ax1 = fig.add_subplot(1, 1, 1)
    ax1.scatter(random_x, random_y)
    ax1.plot(random_x, y_estimate)
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    plt.show()
