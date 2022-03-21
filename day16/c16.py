# code='utf-8'

import numpy as np

def generate(beg, end):
    return np.random.uniform(beg, end)

if __name__=='__main__':

    # iterate over iteration times
    iteration = 1000000

    count = 0

    for i in range(1, iteration+1):
        x = generate(0, 1)
        y = generate(0, 1)

        # construct circle within square
        r_sq = x**2 + y**2

        # within circle radius*radius
        if r_sq <= 1: 
            count += 1

        c_area = count/i*4.0
        pi = c_area/r_sq

    print("{:.3f}".format(pi))



