from random import shuffle
import numpy as np


class Quick:

    def __init__(self):
        pass

    @classmethod
    def partition(cls, arr, lo, hi):
        item = arr[lo]
        i = lo
        j = hi+1
        while True:
            while True:
                i += 1
                if not (i < hi and arr[i] < item):
                    break
            while True:
                j -= 1
                if not (j > lo and arr[j] > item):
                    break
            if i >= j:
                break
            arr[i], arr[j] = arr[j], arr[i]

        arr[lo], arr[j] = arr[j], arr[lo]
        return j

    @classmethod
    def quicksort(cls, arr, lo, hi):
        if lo >= hi:
            return
        j = cls.partition(arr, lo, hi)
        cls.quicksort(arr, lo, j - 1)
        cls.quicksort(arr, j + 1, hi)
        return arr

    @classmethod
    def sort(cls, arr):
        return cls.quicksort(arr, 0, len(arr) - 1)

    @classmethod
    def is_sorted(cls, arr):
        N = len(arr)

        for i in range(N - 1):
            if arr[i] > arr[i + 1]:
                return False
        return True


if __name__ == "__main__":
    # items = [5, 5, 4, 3, 1, 2, 9, 6, 7, 10, 11, 13, 8, 0]
    # items = ['a', 'B', 'f', 'c', 'e', 'd', 'D']
    items = np.random.randint(0, 100, 24)
    print('     items: ', items)
    print(Quick.is_sorted(items))
    print('sort items: ', Quick.sort(items))
    print('     items: ', items)
    print(Quick.is_sorted(items))
