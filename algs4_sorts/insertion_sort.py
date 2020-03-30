import numpy as np


class Insertion(object):

    @classmethod
    def sort(cls, arr):
        N = len(arr)

        for i in range(1, N):
            j = i
            while j > 0 and arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                j -= 1
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
    print(Insertion.is_sorted(items))
    print('sort items: ', Insertion.sort(items))
    print('     items: ', items)
    print(Insertion.is_sorted(items))
