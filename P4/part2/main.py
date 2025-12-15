# Example run: # python3 main.py < test.in > test.out


def can_collect(grid, r, c):
    if grid[r][c] != "@":
        return False
    count = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i == 0 and j == 0:
                continue
            ni, nj = r + i, c + j
            if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]):
                if grid[ni][nj] == "@":
                    count += 1
    return count < 4


def main():
    # read from test.in
    with open(0) as file:
        lines = file.readlines()

    grid = [list(line.strip()) for line in lines if line.strip()]
    res = 0
    m, n = len(grid), len(grid[0])
    rolls_to_remove = set()
    while True:
        running_total = 0
        for i in range(m):
            for j in range(n):
                if can_collect(grid, i, j):
                    rolls_to_remove.add((i, j))
                    running_total += 1
        res += running_total
        if running_total == 0:
            break
        else:
            for r, c in rolls_to_remove:
                grid[r][c] = "."
            rolls_to_remove = set()
    print(res)


if __name__ == "__main__":
    main()
