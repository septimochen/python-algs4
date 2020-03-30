from union_find.weighted_quick_uf import WeightedUnionFind


class Percolation(object):

    def __init__(self, n):
        if n <= 0:
            raise Exception("the size should be greater than 0! ")
        self.uf = WeightedUnionFind(n * n + 2)
        self.ufBackwash = WeightedUnionFind(n * n + 2)
        self.n2 = n
        self.id = [False for _ in range(n * n)]

        self.num_open_sites = 0

    def open(self, row, col):
        n = self.n2
        if row > n or row < 1 or col > n or col < 1:
            raise Exception("out of bounds")
        if self.id[n * (row - 1) + col - 1] is False:
            self.id[n * (row - 1) + col - 1] = True

            self.num_open_sites += 1

            if row != 1 and self.id[n * (row - 2) + col - 1]:
                self.uf.union(n * (row - 1) + col - 1, n * (row - 2) + col - 1)
                self.ufBackwash.union(n * (row - 1) + col - 1, n * (row - 2) + col - 1)

            if col != 1 and self.id[n * (row - 1) + col - 2]:
                self.uf.union(n * (row - 1) + col - 1, n * (row - 1) + col - 2)
                self.ufBackwash.union(n * (row - 1) + col - 1, n * (row - 1) + col - 2)

            if row < n and self.id[n * row + col - 1]:
                self.uf.union(n * row + col - 1, n * (row - 1) + col - 1)
                self.ufBackwash.union(n * row + col - 1, n * (row - 1) + col - 1)

            if col < n and self.id[n * (row - 1) + col]:
                self.uf.union(n * (row - 1) + col - 1, n * (row - 1) + col)
                self.ufBackwash.union(n * (row - 1) + col - 1, n * (row - 1) + col)

            if row == 1:
                self.uf.union(n * (row - 1) + col - 1, n * n + 1)
                self.ufBackwash.union(n * (row - 1) + col - 1, n * n + 1)

            if row == n:
                self.uf.union(n * (row - 1) + col - 1, n * n)

    def is_open(self, row, col):
        n = self.n2
        if row > n or row < 1 or col > n or col < 1:
            raise Exception("out of bounds")

        return self.id[n * (row - 1) + col - 1]

    def is_full(self, row, col):
        n = self.n2
        if row > n or row < 1 or col > n or col < 1:
            raise Exception("out of bounds")

        return self.id[n * (row - 1) + col - 1] and self.ufBackwash.connected((n * (row - 1) + col - 1), (n * n + 1))

    def percolates(self):
        n = self.n2
        # print(f"top: {self.uf.find(n * n + 1)}, bottom: {self.uf.find(n * n)}")
        # return self.uf.find(n * n) == self.uf.find(n * n + 1)
        return self.uf.connected(n * n, n * n + 1)


if __name__ == "__main__":
    perco = Percolation(4)
    print(perco.percolates())

    perco.open(1, 1)
    perco.open(2, 1)
    print(perco.percolates())

    perco.open(3, 1)
    perco.open(3, 2)
    print(perco.percolates())
    print(perco.is_full(3, 2))

    perco.open(4, 2)
    # print(perco.uf)
    print(perco.percolates())


