import numpy as np


class Selection(object):

    @classmethod
    def sort(cls, arr):
        N = len(arr)
        for i in range(N - 1):
            min_index = i
            for j in range(i, N):
                if arr[j] < arr[min_index]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
        return arr

    @classmethod
    def is_sorted(cls, arr):
        N = len(arr)

        for i in range(N - 1):
            if arr[i] > arr[i + 1]:
                return False
        return True

    # @classmethod
    # def sort(cls, arr):
    #     N = len(arr)
    #     for i in range(N - 1):
    #         min_index = i
    #         for j in range(i, N):
    #             if arr[j] < arr[min_index]:
    #                 min_index = j
    #         arr[i], arr[min_index] = arr[min_index], arr[i]
    #     return arr
    #
    # @classmethod
    # def is_sorted(cls, arr):
    #     for i in range(1, len(arr)):
    #         if arr[i] < arr[i-1]:
    #             return False
    #     return True


if __name__ == "__main__":
    # items = [5, 5, 4, 3, 1, 2, 9, 6, 7, 10, 11, 13, 8, 0]
    # items = ['a', 'B', 'f', 'c', 'e', 'd', 'D']
    items = np.random.randint(0, 100, 24)
    print('     items: ', items)
    print(Selection.is_sorted(items))
    print('sort items: ', Selection.sort(items))
    print('     items: ', items)
    print(Selection.is_sorted(items))
