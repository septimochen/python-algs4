import numpy as np
from algs4_sorts.stopwatch import StopWatch
from algs4_sorts.insertion_sort import Insertion
from algs4_sorts.selection_sort import Selection
from algs4_sorts.shell import Shell


class SortCompare:

    @staticmethod
    def time(alg, arr):
        timer = StopWatch()
        if alg == 'Insertion':
            Insertion.sort(arr)
        elif alg == 'Selection':
            Selection.sort(arr)
        elif alg == 'Shell':
            Shell.sort(arr)
        return timer.elapsed_time()

    def time_random_input(self, alg, n, t):
        total = 0.0
        for i in range(t):
            arr = np.random.uniform(0, 10000, size=n)
            total += self.time(alg, arr)
        return total


if __name__ == "__main__":
    import sys
    agls1 = sys.argv[1]
    agls2 = sys.argv[2]

    N = int(sys.argv[3])
    T = int(sys.argv[4])

    sc = SortCompare()
    t1 = sc.time_random_input(agls1, N, T)
    t2 = sc.time_random_input(agls2, N, T)

    print("for {} random floats:".format(N))
    print("{} is {:.2f} times faster than {}".format(agls1, t2/t1, agls2))
