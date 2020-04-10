import numpy as np


class Heap:
    @classmethod
    def heapfy(cls, arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[i] < arr[left]:
            largest = left
        if right < n and arr[largest] < arr[right]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            cls.heapfy(arr, n, largest)

    @classmethod
    def sort(cls, arr):
        N = len(arr)

        for i in range(N, -1, -1):
            cls.heapfy(arr, N, i)

        for i in range(N - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            cls.heapfy(arr, i, 0)
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
    items = np.random.randint(0, 1000, 1000)
    print("     items: ", items)
    print(Heap.is_sorted(items))
    print("sort items: ", Heap.sort(items))
    print("     items: ", items)
    print(Heap.is_sorted(items))
