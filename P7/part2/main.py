# Example run: # python3 main.py < test.in > test.out


def main():
    # read from test.in
    with open(0) as file:
        lines = [line.strip() for line in file.readlines()]
    grid = [list(line) for line in lines]
    curr_tach = [True if char == "S" else False for char in grid[0]]
    n = len(grid)
    m = len(grid[0])
    split_count = 0
    for i in range(1, n):
        new_tach = [False] * m
        for j in range(m):
            if grid[i][j] == "^" and curr_tach[j]:
                # split
                split_count += 1
                if j - 1 >= 0:
                    new_tach[j - 1] = True
                if j + 1 < m:
                    new_tach[j + 1] = True
            elif curr_tach[j]:
                new_tach[j] = True
        curr_tach = new_tach
    print(split_count)


if __name__ == "__main__":
    main()
