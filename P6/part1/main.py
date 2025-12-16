# Example run: # python3 main.py < test.in > test.out


def main():
    # read from test.in
    with open(0) as file:
        lines = file.readlines()

    processed_lines = [line.strip() for line in lines if line.strip()]
    n = len(processed_lines)
    operations = [p for p in processed_lines[-1].split(" ") if p]
    digits = []
    for line in processed_lines[: n - 1]:
        nums_to_add = [int(x) for x in line.split(" ") if x]
        digits.append(nums_to_add)
    res = 0
    for i in range(len(operations)):
        if operations[i] == "*":
            curr = 1
            for j in range(len(digits)):
                curr *= digits[j][i]
            res += curr
        if operations[i] == "+":
            curr = 0
            for j in range(len(digits)):
                curr += digits[j][i]
            res += curr
    print(res)


if __name__ == "__main__":
    main()
