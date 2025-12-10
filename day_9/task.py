from collections import deque

def read_points(filename):
    points = []
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            x_str, y_str = line.split(",")
            x = int(x_str)
            y = int(y_str)
            points.append((x, y))
    return points


def largest_rectangle_area(points):
    n = len(points)
    max_area = 0

    for i in range(n):
        x1, y1 = points[i]
        for j in range(i + 1, n):
            x2, y2 = points[j]
            width = abs(x1 - x2) + 1
            height = abs(y1 - y2) + 1
            area = width * height
            if area > max_area:
                max_area = area

    return max_area


def main():
    points = read_points("./day_9/input.txt")
    print(f"Loaded {len(points)} red tiles.")
    ans = largest_rectangle_area(points)
    print("Largest rectangle area (part 1):", ans)


# ---------- PART 2 WITH COORDINATE COMPRESSION BELOW ----------

def read_red_points(filename="./day_9/input.txt"):
    return read_points(filename)


def build_allowed_grid(red_points):
    # 1) Coordinate compression
    xs = [x for x, _ in red_points]
    ys = [y for _, y in red_points]

    ux = sorted(set(xs))
    uy = sorted(set(ys))
    x_to_ix = {x: i for i, x in enumerate(ux)}
    y_to_iy = {y: i for i, y in enumerate(uy)}

    W = len(ux)
    H = len(uy)

    print("Compressed grid size:", "W =", W, "H =", H)

    # red points in compressed grid coordinates
    red_grid = [(x_to_ix[x], y_to_iy[y]) for (x, y) in red_points]

    # 2) Mark the boundary on the compressed grid
    boundary = [[False] * W for _ in range(H)]

    n = len(red_grid)
    for i in range(n):
        x1, y1 = red_grid[i]
        x2, y2 = red_grid[(i + 1) % n]

        if x1 == x2:
            # vertical segment in compressed y indices
            step = 1 if y2 > y1 else -1
            for yy in range(y1, y2 + step, step):
                boundary[yy][x1] = True
        elif y1 == y2:
            # horizontal segment in compressed x indices
            step = 1 if x2 > x1 else -1
            for xx in range(x1, x2 + step, step):
                boundary[y1][xx] = True
        else:
            raise ValueError("Non-orthogonal segment in input!")

    # 3) Flood-fill outside on a padded grid
    outside = [[False] * (W + 2) for _ in range(H + 2)]
    q = deque()
    q.append((0, 0))
    outside[0][0] = True

    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while q:
        py, px = q.popleft()
        for dy, dx in dirs:
            ny, nx = py + dy, px + dx
            if 0 <= ny < H + 2 and 0 <= nx < W + 2 and not outside[ny][nx]:
                gy, gx = ny - 1, nx - 1
                if 0 <= gy < H and 0 <= gx < W:
                    if boundary[gy][gx]:
                        continue
                outside[ny][nx] = True
                q.append((ny, nx))

    # 4) Build allowed grid (inside or boundary)
    allowed = [[False] * W for _ in range(H)]
    for y in range(H):
        for x in range(W):
            py, px = y + 1, x + 1
            if boundary[y][x]:
                allowed[y][x] = True
            else:
                if not outside[py][px]:
                    allowed[y][x] = True  # interior

    return allowed, red_grid, ux, uy, W, H


def build_prefix_sum(allowed, W, H):
    ps = [[0] * (W + 1) for _ in range(H + 1)]
    for y in range(H):
        row_sum = 0
        for x in range(W):
            if allowed[y][x]:
                row_sum += 1
            ps[y + 1][x + 1] = ps[y][x + 1] + row_sum
    return ps


def rect_sum(ps, x1, y1, x2, y2):
    return (ps[y2 + 1][x2 + 1]
            - ps[y1][x2 + 1]
            - ps[y2 + 1][x1]
            + ps[y1][x1])


def solve_part2(filename="./day_9/input.txt"):
    red_points = read_red_points(filename)

    allowed, red_grid, ux, uy, W, H = build_allowed_grid(red_points)
    ps = build_prefix_sum(allowed, W, H)

    n = len(red_grid)
    max_area = 0

    # Try all pairs of red tiles as opposite corners
    for i in range(n):
        cx1, cy1 = red_grid[i]
        x1_real, y1_real = red_points[i]
        for j in range(i + 1, n):
            cx2, cy2 = red_grid[j]
            x2_real, y2_real = red_points[j]

            # compressed bounding box
            x1c = min(cx1, cx2)
            x2c = max(cx1, cx2)
            y1c = min(cy1, cy2)
            y2c = max(cy1, cy2)

            # quick prune: compressed area can't beat best
            compressed_area = (x2c - x1c + 1) * (y2c - y1c + 1)
            if compressed_area == 0:
                continue

            # check if all compressed cells in this box are allowed
            allowed_cells = rect_sum(ps, x1c, y1c, x2c, y2c)
            if allowed_cells != compressed_area:
                continue

            # compute REAL area in original coordinates
            width = abs(x1_real - x2_real) + 1
            height = abs(y1_real - y2_real) + 1
            real_area = width * height

            if real_area > max_area:
                max_area = real_area

    print("Largest rectangle area using only red/green tiles:", max_area)
    return max_area


if __name__ == "__main__":
    # main()  # part 1
    solve_part2("./day_9/input.txt")