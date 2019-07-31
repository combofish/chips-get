from numba import jit
import sys
import numpy as np
import random
import time

@jit
def estimate_nbr_points_in_quarter_circle(nbr_estimates):
    nbr_trials_in_quarter_unit_circle = 0

    for step in range(int(nbr_estimates)):
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        is_in_unit_circle = pow(x,2) + pow(y,2) <= 1.0
        nbr_trials_in_quarter_unit_circle += is_in_unit_circle

    return nbr_trials_in_quarter_unit_circle

@jit
def estimate_nbr_points_in_quarter_circle_numpy(nbr_samples):
    np.random.seed()
    xs = np.random.uniform(0, 1, nbr_samples)
    ys = np.random.uniform(0, 1, nbr_samples)
    estimate_inside_quarter_unit_circle = pow(xs, 2) + pow(ys, 2) <= 1
    nbr_trials_in_quarter_unit_circle = np.sum(estimate_inside_quarter_unit_circle)

    return nbr_trials_in_quarter_unit_circle

if __name__ == '__main__':
    # arg = 100000
    arg = int(sys.argv[1])
    t1 = time.time()
    pi_estimate = estimate_nbr_points_in_quarter_circle(arg) / arg * 4
    t2 = time.time()
    pi_estimate_numpy = estimate_nbr_points_in_quarter_circle_numpy(arg) / arg * 4
    t3 = time.time()
    
    print("pi_estimate = ",pi_estimate, " time cost : ", t2 - t1)
    print("pi_estimate_numpy = ", pi_estimate_numpy, " time cost : ", t3 - t2)
