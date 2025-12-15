# Example run: # python3 main.py < test.in > test.out


def find_max_digit(s: str, curr: int, i: int) -> tuple[int, int]:
    n = len(s)
    max_digit = -1
    max_digit_pos = -1
    # search from curr + 1 to n - (12 - i) inclusive
    # sanitary check: last index we can take should be n - 1 (end range is n)
    # when i = 11, n - (12 - 11) + 1 = n - (1) + 1 = n
    # when i = 0, n - (12 - 0) + 1 = n - 12 + 1 = n - 11
    for idx in range(curr + 1, n - (12 - i) + 1):
        digit = s[idx]
        if int(digit) > max_digit:
            max_digit = int(digit)
            max_digit_pos = idx
    return max_digit, max_digit_pos


def main():
    # read from test.in
    with open(0) as file:
        lines = file.readlines()

    processed_lines = [line.strip() for line in lines if line.strip()]
    res = 0
    """
    some reasoning here:
    1. on the first take we take index i, there needs to be 11 digits after i
    2. so that means that i is at most n - 12 (0-based index)
    3. on the second take, i is at most n - 11 (0-based index)
    4. we have a "curr" and each time we update i to curr
    5. ensure that we always have enough digit by using the range [curr: n - (12 - i)]
    """
    for line in processed_lines:
        # find the biggest 12-digit number
        curr = -1  # current index we have taken from
        curr_max = 0
        for i in range(12):
            digit, index = find_max_digit(line, curr, i)
            curr = index
            curr_max = curr_max * 10 + digit
        res += curr_max
    print(res)


if __name__ == "__main__":
    main()
