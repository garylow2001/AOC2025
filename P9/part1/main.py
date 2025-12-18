# Example run: # python3 main.py < test.in > test.out


def main():
    # read from test.in
    with open(0) as file:
        lines = [line.strip() for line in file.readlines()]
    coords = [tuple(map(int, l.split(","))) for l in lines]
    n = len(coords)
    max_area = 0
    for i in range(n):
        for j in range(i + 1, n):
            coord1 = coords[i]
            coord2 = coords[j]
            area = (abs(coord1[0] - coord2[0]) + 1) * (abs(coord1[1] - coord2[1]) + 1)
            max_area = max(max_area, area)
    print(max_area)


if __name__ == "__main__":
    main()
