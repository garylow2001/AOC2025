# Example run: # python3 main.py < test.in > test.out


def main():
    # read from test.in
    with open(0) as file:
        lines = file.readlines()
    # operations and digit counts
    last_line = lines[-1].split(" ")
    operations = []
    digit_count = []
    curr = 1
    for i in range(len(last_line)):
        if last_line[i] == "+" or last_line[i] == "*":
            operations.append(last_line[i])
            if i != 0:
                digit_count.append(curr)
            curr = 1
        else:
            curr += 1
    digit_count.append(curr)

    # read digits
    n = len(lines)
    processed_lines = []
    for line in lines[: n - 1]:
        curr_pointer = 0
        nl = []
        for dc in digit_count:
            nl.append(line[curr_pointer : curr_pointer + dc])
            curr_pointer += dc + 1
        processed_lines.append(nl)
    processed_lines = list(map(list, zip(*processed_lines)))
    # reconstruct digits
    # within each section, go backwards and construct number
    new_digits = []
    for section_id, section in enumerate(processed_lines):
        reconstructed_numbers = []
        dc = digit_count[section_id]
        for dec_place in range(dc - 1, -1, -1):
            # 2 -> 1 -> 0
            curr_num = []
            for num in section:
                curr_num.append(num[dec_place])
            curr_num = int("".join(curr_num))
            reconstructed_numbers.append(curr_num)
        new_digits.append(reconstructed_numbers)

    # perform operations
    res = 0
    for i, op in enumerate(operations):
        if op == "+":
            section_sum = sum(new_digits[i])
            res += section_sum
        elif op == "*":
            section_prod = 1
            for num in new_digits[i]:
                section_prod *= num
            res += section_prod
    print(res)


if __name__ == "__main__":
    main()
