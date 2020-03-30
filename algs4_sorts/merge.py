import numpy as np


class Merge:

    @classmethod
    def merge_sort(cls, arr, lo, hi):
        if lo >= hi:
            return
        mid = (lo + hi) // 2
        cls.merge_sort(arr, lo, mid)
        cls.merge_sort(arr, mid+1, hi)
        cls.merge(arr, lo, mid, hi)
        return arr

    @classmethod
    def merge(cls, arr, lo, mid, hi):
        aux = list(arr)
        i = lo
        j = mid + 1
        k = lo
        while k <= hi:
            if i > mid:
                arr[k] = aux[j]
                j += 1
            elif j > hi:
                arr[k] = aux[i]
                i += 1
            elif aux[i] >= aux[j]:
                arr[k] = aux[j]
                j += 1
            else:
                arr[k] = aux[i]
                i += 1
            k += 1

    @classmethod
    def sort(cls, arr):
        N = len(arr)
        return cls.merge_sort(arr, 0, N-1)

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
    items = np.random.randint(0, 1000, 1000)
    print('     items: ', items)
    print(Merge.is_sorted(items))
    print('sort items: ', Merge.sort(items))
    print('     items: ', items)
    print(Merge.is_sorted(items))
