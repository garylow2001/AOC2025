# Example run: # python3 main.py < test.in > test.out


def main():
    # read from test.in
    with open(0) as file:
        lines = file.readlines()

    processed_lines = [line.strip() for line in lines if line.strip()]
    ranges = []
    for p in processed_lines:
        for r in p.split(","):
            ranges.append(tuple(map(int, r.split("-"))))

    res = 0
    for r in ranges:
        start, end = r
        for num in range(start, end + 1):
            strnum = str(num)
            num_digits = len(strnum)
            if num_digits % 2 == 0:
                left = strnum[: num_digits // 2]
                right = strnum[num_digits // 2 :]
                if left == right:
                    res += num
    print(res)


if __name__ == "__main__":
    main()
