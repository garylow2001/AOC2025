# Example run: # python3 main.py < test.in > test.out


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))  # indexes of coords
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return
        if self.size[rx] < self.size[ry]:
            rx, ry = ry, rx  # ensure rx is larger, then can set ry under rx
        self.parent[ry] = rx
        self.size[rx] += self.size[ry]

    def check_all_connected(self):
        root = self.find(0)  # root of first element
        # check if all have same root
        for i in range(1, len(self.parent)):
            if self.find(i) != root:
                return False
        return True


def main():
    # read from test.in
    with open(0) as file:
        lines = [line.strip() for line in file.readlines()]
    coords = [tuple(map(int, l.split(","))) for l in lines]
    n = len(coords)
    dim = len(coords[0])
    dist_pairs = []
    for i in range(n):
        for j in range(i + 1, n):
            coord1 = coords[i]
            coord2 = coords[j]
            dist = sum((coord1[k] - coord2[k]) ** 2 for k in range(dim))
            dist_pairs.append((coord1, coord2, dist))
    dist_pairs.sort(key=lambda x: x[2])
    uf = UnionFind(n)
    last_c1 = 0
    last_c2 = 0
    for i in range(n * n):
        c1, c2, d = dist_pairs[i]
        last_c1, last_c2 = c1, c2
        print(f"Connecting {c1} and {c2} with distance {d}")
        idx1 = coords.index(c1)
        idx2 = coords.index(c2)
        uf.union(idx1, idx2)
        if uf.check_all_connected():
            break
    print(last_c1[0] * last_c2[0])


if __name__ == "__main__":
    main()
