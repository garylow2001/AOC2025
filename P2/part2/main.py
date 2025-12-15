# Example run: # python3 main.py < test.in > test.out


def check_repetition(s: str) -> bool:
    # split into range from 0 to half of len s and check if repeated till end
    n = len(s)
    for i in range(1, n // 2 + 1):  # exclusive range for s[:i] -> end at s[i-1]
        if n % i == 0:
            if s[:i] * (n // i) == s:
                return True
    return False


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
            if check_repetition(strnum):
                res += num
    print(res)


if __name__ == "__main__":
    main()
