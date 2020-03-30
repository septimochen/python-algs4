import numpy as np


class Shell:

    @classmethod
    def sort(cls, arr):
        N = len(arr)
        h = 1
        while h < N // 3:
            h = 3 * h + 1

        while h >= 1:
            for i in range(h, N):
                j = i
                while j >= h and arr[j] < arr[j - h]:
                    arr[j], arr[j - h] = arr[j - h], arr[j]
                    j -= h
            h = h // 3
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
    items = np.random.randint(0, 100, 100)
    print('     items: ', items)
    print(Shell.is_sorted(items))
    print('sort items: ', Shell.sort(items))
    print('     items: ', items)
    print(Shell.is_sorted(items))
