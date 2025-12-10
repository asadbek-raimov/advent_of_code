class DSU1:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False   
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        return True


def read_points(filename):
    points = []
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            x, y, z = map(int, line.split(","))
            points.append((x, y, z))
    return points


def solve(filename: str, num_connections: int):
    points = read_points(filename)
    n = len(points)
    print(f"Loaded {n} junction boxes.")

    dsu = DSU(n)

    distances = []
    for i in range(n):
        x1, y1, z1 = points[i]
        for j in range(i + 1, n):
            x2, y2, z2 = points[j]
            d2 = (x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2
            distances.append((d2, i, j))

    distances.sort()

    processed = 0
    for dist, i, j in distances:
        dsu.union(i, j) 
        processed += 1
        if processed == num_connections:
            break

    comps = {}
    for i in range(n):
        root = dsu.find(i)
        comps[root] = comps.get(root, 0) + 1

    sizes = sorted(comps.values(), reverse=True)
    print("All circuit sizes (largest first):", sizes)

    if len(sizes) < 3:
        print("Not enough circuits to take 3 largest!")
        return None

    result = sizes[0] * sizes[1] * sizes[2]
    print("Product of three largest circuits:", result)
    return result


if __name__ == "__main__":
    pass
    

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False  
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        return True



def solve_part2(filename: str):
    points = read_points(filename)
    n = len(points)
    print(f"Loaded {n} junction boxes.")

    dsu = DSU(n)

    distances = []
    for i in range(n):
        x1, y1, z1 = points[i]
        for j in range(i + 1, n):
            x2, y2, z2 = points[j]
            d2 = (x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2
            distances.append((d2, i, j))

    # STEP 2 – sort all edges by distance ascending
    distances.sort()

    # STEP 3 – Kruskal-like: only count *successful* unions
    components = n
    last_pair = None  # indices of last merged boxes (i, j)

    for d2, i, j in distances:
        if dsu.union(i, j):
            components -= 1
            last_pair = (i, j)
            if components == 1:
                break

    if last_pair is None:
        print("Graph was already connected? Something's wrong.")
        return

    i, j = last_pair
    x1 = points[i][0]
    x2 = points[j][0]
    result = x1 * x2

    print(f"Last connection between boxes at: {points[i]} and {points[j]}")
    print(f"X coordinates: {x1} and {x2}")
    print(f"Product: {result}")
    return result


if __name__ == "__main__":
    solve_part2("./day_8/input.txt")