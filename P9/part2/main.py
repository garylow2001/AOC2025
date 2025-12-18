# Example run: # python3 main.py < test.in > test.out
from collections import deque


def main():
    # read from test.in
    with open(0) as file:
        lines = [line.strip() for line in file.readlines()]
    coords = [tuple(map(int, l.split(","))) for l in lines]
    rows = []
    cols = []
    for r, c in coords:
        rows.append(r)
        cols.append(c)
    print(
        len(rows), len(cols), len(set(rows)), len(set(cols))
    )  # ~500 total, ~250 unique
    # coordinate compression on rows and cols, index maps to actual value
    sorted_rows = sorted(set(rows))
    sorted_cols = sorted(set(cols))
    # map maps original value to compressed value
    row_map = {v: i for i, v in enumerate(sorted_rows)}
    col_map = {v: i for i, v in enumerate(sorted_cols)}
    print(row_map, col_map)
    compressed_coords = [
        (row_map[r], col_map[c]) for r, c in coords
    ]  # list of compressed coordinates
    print(compressed_coords)
    # build up the grid
    green_r = {}  # for row, connects two points in coords by horizontal line
    green_c = {}  # for col, connects two points in coords by vertical line
    for r in row_map.values():
        coord_for_r = sorted(
            list(filter(lambda x: x[0] == r, compressed_coords)), key=lambda x: x[1]
        )
        min_c = min(c[1] for c in coord_for_r)
        max_c = max(c[1] for c in coord_for_r)
        print(f"Row {r} connects {min_c} to {max_c}")
        green_r[r] = list(c for c in range(min_c, max_c + 1))

    for c in col_map.values():
        coord_for_c = sorted(
            list(filter(lambda x: x[1] == c, compressed_coords)), key=lambda x: x[0]
        )
        min_r = min(r[0] for r in coord_for_c)
        max_r = max(r[0] for r in coord_for_c)
        print(f"Col {c} connects {min_r} to {max_r}")
        green_c[c] = list(r for r in range(min_r, max_r + 1))
    print(green_r)
    print(green_c)

    # debug with grid output
    new_grid = [["."] * (len(col_map)) for _ in range(len(row_map))]  # initialize grid
    for ir in range(min(row_map.values()), max(row_map.values()) + 1):
        for ic in range(min(col_map.values()), max(col_map.values()) + 1):
            if (ir, ic) in compressed_coords:
                new_grid[ir][ic] = "#"
            elif ir in green_r and ic in green_r[ir]:
                new_grid[ir][ic] = "X"
            elif ic in green_c and ir in green_c[ic]:
                new_grid[ir][ic] = "X"

    # flood fill new grid with "X" starting with first interior point
    # hacky: we guaranteed that this is an interior point by previously checking it on the printed grid alr
    interior_r, interior_c = (
        min(compressed_coords)[0] + 1,
        min(compressed_coords)[1] + 1,
    )
    queue = deque()
    queue.append((interior_r, interior_c))
    visited = set()
    while queue:
        r, c = queue.popleft()
        if (r, c) in visited:
            continue
        visited.add((r, c))
        new_grid[r][c] = "X"
        # check neighbors
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(new_grid) and 0 <= nc < len(new_grid[0]):
                if new_grid[nr][nc] == ".":  # not on border
                    queue.append((nr, nc))

    # print new grid
    for line in new_grid:
        print("".join(line))

    # function to check if area is valid by going through perimeter and check for green cells
    def is_area_valid(r1, c1, r2, c2, grid):
        # standardise top left point
        topleft = (min(r1, r2), min(c1, c2))
        topright = (min(r1, r2), max(c1, c2))
        bottomleft = (max(r1, r2), min(c1, c2))
        bottomright = (max(r1, r2), max(c1, c2))
        valid_points = ["X", "#"]
        # top edge
        if not all(
            grid[topleft[0]][c] in valid_points
            for c in range(topleft[1], topright[1] + 1)
        ):
            return False
        # bottom edge
        if not all(
            grid[bottomleft[0]][c] in valid_points
            for c in range(bottomleft[1], bottomright[1] + 1)
        ):
            return False
        # left edge
        if not all(
            grid[r][topleft[1]] in valid_points
            for r in range(topleft[0], bottomleft[0] + 1)
        ):
            return False
        # right edge
        if not all(
            grid[r][topright[1]] in valid_points
            for r in range(topright[0], bottomright[0] + 1)
        ):
            return False
        return True

    # check against each set of points the area and if it is valid
    max_area = 0
    for i in range(len(compressed_coords)):
        for j in range(i + 1, len(compressed_coords)):
            r1, c1 = compressed_coords[i]
            r2, c2 = compressed_coords[j]
            actual_r1 = sorted_rows[r1]
            actual_c1 = sorted_cols[c1]
            actual_r2 = sorted_rows[r2]
            actual_c2 = sorted_cols[c2]
            area = (abs((actual_r2 - actual_r1)) + 1) * (
                abs((actual_c2 - actual_c1)) + 1
            )
            print(
                actual_r1,
                actual_c1,
                actual_r2,
                actual_c2,
                area,
                is_area_valid(r1, c1, r2, c2, new_grid),
            )
            max_area = (
                max(max_area, area)
                if is_area_valid(r1, c1, r2, c2, new_grid)
                else max_area
            )
    print(max_area)


if __name__ == "__main__":
    main()
