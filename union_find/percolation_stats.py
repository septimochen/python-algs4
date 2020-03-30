from random import randint
from union_find.percolation import Percolation
from math import sqrt
import numpy as np


class PercolationStats(object):

    def __init__(self, n, trials):
        self.trial = trials
        self.col = 0
        self.row = 0

        x_trials = np.zeros(trials)

        for i in range(trials):
            temp = Percolation(n)
            while temp.percolates() is not True:
                self.col = randint(1, n)
                self.row = randint(1, n)
                temp.open(self.col, self.row)

            x_trials[i] = temp.num_open_sites/(n*n)

        self.mean = np.mean(x_trials)
        self.stdev = np.std(x_trials)

    @property
    def confidence_low(self):
        return self.mean - 1.96 * self.stdev / sqrt(self.trial)

    @property
    def confidence_high(self):
        return self.mean + 1.96 * self.stdev / sqrt(self.trial)


if __name__ == "__main__":
    perco_stats = PercolationStats(20, 100)
    print(f"mean is = {perco_stats.mean}")
    print(f"stdev is = {perco_stats.stdev}")
    print(f"95% confidence interval: {perco_stats.confidence_low}, {perco_stats.confidence_high}")
