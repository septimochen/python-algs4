import sys
from algs4.stack import Stack
from algs4_sorts.min_pq import MinPQ
from algs4.transaction import Transaction

if __name__ == "__main__":
    M = int(sys.argv[1])
    pq = MinPQ()
    f = open(sys.argv[2], "r")
    for line in f.readlines():
        pq.insert(Transaction(line))
        if pq.size() > M:
            pq.del_min()

    stack = Stack()
    while not pq.is_empty():
        stack.push(pq.del_min())
    for t in stack:
        print(t)

