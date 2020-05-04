from algs4_search.st import Node, STkeyIterator


class SequentialSearchST:

    def __init__(self):
        self.first = None
        self.size = 0

    def contains(self, key):
        x = self.first
        while x:
            if key == x.key:
                return True
            x = x.next
        return False

    def get(self, key):
        x = self.first
        while x:
            if key == x.key:
                return x.value
            x = x.next
        return None

    def put(self, key, val):
        x = self.first
        while x:
            if key == x.key:
                x.value = val
                return
            x = x.next
        self.first = Node(key, val, next_node=self.first)
        self.size += 1

    def delete(self, key):
        prev = None
        curr = self.first
        while curr:
            if key == curr.key:
                if prev:
                    prev.next = curr.next
                else:
                    self.first = curr.next
                self.size -= 1
            prev = curr
            curr = curr.next

    def keys(self):
        return STkeyIterator(self.first)

    def is_empty(self):
        return self.size == 0


if __name__ == "__main__":
    import sys

    st = SequentialSearchST()
    i = 0
    with open(sys.argv[1]) as f:
        for line in f:
            for key in line.split():
                st.put(key, i)
                i += 1

    for key in st.keys():
        print(key + ": " + str(st.get(key)))