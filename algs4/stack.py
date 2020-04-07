from .linklist import LinkIterator, Node


class Stack(object):

    def __init__(self):
        self.first = None
        self.n = 0

    def __str__(self):
        return " ".join(i for i in self)

    def __iter__(self):
        return LinkIterator(self.first)

    def size(self):
        return self.n

    def is_empty(self):
        return self.first is None

    def push(self, item):
        oldfirst = self.first
        self.first = Node(item, oldfirst)
        self.n += 1

    def pop(self):
        if self.is_empty():
            raise ValueError("Stack underflow")
        else:
            item = self.first.item
            self.first = self.first.next
            self.n -= 1
            return item

    
