class WeightedUnionFind(object):

    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1 for _ in range(n)]
        self.count = n

    def components_count(self):
        return self.count

    def find(self, p):
        self.validate(p)
        while p != self.parent[p]:
            p = self.parent[p]
        return p

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def validate(self, p):
        n = len(self.parent)
        if p < 0 or p >= n:
            raise IndexError("the value is invalid.")

    def union(self, p, q):
        root_p = self.find(p)
        root_q = self.find(q)
        if root_p == root_q:
            pass
        else:
            if self.size[root_p] < self.size[root_q]:
                self.parent[root_p] = root_q
                self.size[root_q] += self.size[root_p]
            else:
                self.parent[root_q] = root_p
                self.size[root_p] += self.size[root_q]
        self.count -= 1


if __name__ == "__main__":
    num = 10
    uf = WeightedUnionFind(num)
    for node_p, node_q in [(1, 2), (3, 4), (4, 5), (2, 7), (1, 7), (8, 9)]:
        if uf.find(node_p) == uf.find(node_q):
            continue
        else:
            uf.union(node_p, node_q)
            print(f"{node_p} union {node_q}")
    print(uf.components_count())










