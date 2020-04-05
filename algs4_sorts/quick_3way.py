import numpy as np


class Quick3way:

    @classmethod
    def sort(cls, arr):
        return cls.quicksort(arr, 0, len(arr) - 1)

    @classmethod
    def quicksort(cls, arr, lo, hi):
        if hi <= lo:
            return
        lt = lo
        i = lo + 1
        gt = hi
        v = arr[lo]

        while i <= gt:
            if arr[i] <= v:
                arr[i], arr[lt] = arr[lt], arr[i]
                i += 1
                lt += 1
            elif arr[i] >= v:
                arr[i], arr[gt] = arr[gt], arr[i]
                gt -= 1
            else:
                i += 1
        cls.quicksort(arr, lo, lt - 1)
        cls.quicksort(arr, gt + 1, hi)
        return arr

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
    print(Quick3way.is_sorted(items))
    print('sort items: ', Quick3way.sort(items))
    print('     items: ', items)
    print(Quick3way.is_sorted(items))
