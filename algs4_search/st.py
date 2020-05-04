class Node:
    def __init__(self, key, value, next_node):
        self.key = key
        self.value = value
        self.next = next_node


class STkeyIterator:
    def __init__(self, current):
        self.current = current

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration()
        else:
            key = self.current.key
            self.current = self.current.next
            return key


class STValueIterator:
    def __init__(self, current):
        self.current = current

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration()
        else:
            value = self.current.value
            self.current = self.current.value
            return value
