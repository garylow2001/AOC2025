# Example run: # python3 main.py < test.in > test.out


def main():
    # read from test.in
    with open(0) as file:
        lines = [line.strip() for line in file.readlines()]
    grid = [list(line) for line in lines]
    curr_tach = grid[0].index("S")
    n = len(grid)
    m = len(grid[0])

    cache = {}

    # find all paths
    def dfs(row, tach_pos):
        if row == n:
            return 1
        if (row, tach_pos) in cache:
            return cache[(row, tach_pos)]
        elif grid[row][tach_pos] == "^":
            left = dfs(row + 1, tach_pos - 1) if tach_pos - 1 >= 0 else 0
            right = dfs(row + 1, tach_pos + 1) if tach_pos + 1 < m else 0
            total = left + right
            cache[(row, tach_pos)] = total
            return total
        else:
            total = dfs(row + 1, tach_pos)
            cache[(row, tach_pos)] = total
            return total

    print(dfs(0, curr_tach))


if __name__ == "__main__":
    main()
