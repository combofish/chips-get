import sys
import numpy as np
from datetime import datetime

def python_sum(n):
    a = list(range(n))
    b = list(range(n))
    c = []

    for i in range(len(a)):
        a[i] = pow(i,2)
        b[i] = pow(i,3)
        c.append(a[i] + b[i])

    return c

def numpy_sum(n):
    a = pow(np.arange(n), 2)
    b = pow(np.arange(n), 3)
    c = a + b

    return c


if __name__ == '__main__':
    size = int(sys.argv[1])

    start = datetime.now()
    c = python_sum(size)
    delta = datetime.now() - start
    print("The last 2 elements of the sum: ", c[-2:])
    print("PythonSum elapsed time in microseconds: ", delta.microseconds)

    start = datetime.now()
    c = numpy_sum(size)
    delta = datetime.now() - start
    print("The last 2 elements of the sum: ", c[-2:])
    print("NumPySum elapsed time in microseconds: ", delta.microseconds)
