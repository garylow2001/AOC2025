# Example run: # python3 main.py < test.in > test.out


def main():
    # read from test.in
    with open(0) as file:
        lines = file.readlines()

    processed_lines = [line.strip() for line in lines if line.strip()]
    res = 0
    for line in processed_lines:
        n = len(line)
        max_digit = -1
        max_digit_pos = -1  # earliest pos of max digit
        # get max digit and pos
        for idx, digit in enumerate(line):
            if int(digit) > max_digit:
                max_digit = int(digit)
                max_digit_pos = idx
        second_max_digit = -1
        second_max_digit_pos = -1
        # if max digit is at end, find 2nd max before it
        if max_digit_pos == n - 1:
            for idx, digit in enumerate(line):
                if int(digit) > second_max_digit and idx != max_digit_pos:
                    second_max_digit = int(digit)
                    second_max_digit_pos = idx
            max_pair = second_max_digit * 10 + max_digit
            res += max_pair
        else:
            # find max digit after max digit pos
            for idx in range(max_digit_pos + 1, n):
                digit = line[idx]
                if int(digit) > second_max_digit:
                    second_max_digit = int(digit)
                    second_max_digit_pos = idx
            max_pair = max_digit * 10 + second_max_digit
            res += max_pair
    print(res)


if __name__ == "__main__":
    main()
