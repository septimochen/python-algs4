class BinarySearchST(object):
    init_capacity = 2

    def __init__(self):
        self._keys = [None] * self.init_capacity
        self._val = [None] * self.init_capacity
        self.n = 0

    def rank(self, arr, key):
        lo = 0
        hi = self.n - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if key < arr[mid]:
                hi = mid - 1
            elif key > arr[mid]:
                lo = mid + 1
            else:
                return mid
        return lo

    def resize(self, capacity):
        self._keys = self._keys + [None] * (capacity - len(self._keys))
        self._val = self._val + [None] * (capacity - len(self._val))

    def contains(self, key):
        return self.get(key) is not None

    def get(self, key):
        i = self.rank(self._keys, key)
        if i < self.n and self._keys[i] == key:
            return self._val[i]
        return None

    def put(self, key, value):
        i = self.rank(self._keys, key)
        if i < self.n and self._keys[i] == key:
            self._val[i] = value
            return

        if self.n == len(self._keys):
            self.resize(self.n * 2)

        j = self.n
        while j > i:
            self._keys[j], self._val[j] = self._keys[j - 1], self._val[j - 1]
            j -= 1
        self._keys[i], self._val[i] = key, value
        self.n += 1

    def delete(self, key):
        self.put(key, None)

    def is_empty(self):
        return self.n == 0

    def size(self):
        return self.n

    def keys(self):
        return self._keys[:self.n]


if __name__ == "__main__":
    import sys

    st = BinarySearchST()
    num = 0
    with open(sys.argv[1]) as f:
        for line in f:
            for word in line.split():
                st.put(word, num)
                num += 1

    for k in st.keys():
        print(k + ": " + str(st.get(k)))
