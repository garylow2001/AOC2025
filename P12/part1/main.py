# Example run: # python3 main.py < test.in > test.out


def main():
    res = 0

    # read from test.in
    with open(0) as file:
        lines = file.readlines()

    processed_lines = [line.strip() for line in lines if line.strip()]
    # each pattern 1,2,3,4,5 is 3x3
    patterns = [processed_lines[i : i + 3] for i in range(1, 24, 4)]
    pattern_sizes = [sum(line.count("#") for line in p) for p in patterns]
    print(patterns, pattern_sizes)
    # process each criteria
    for line in processed_lines[24:]:
        criteria_line = line.split(" ")
        criteria_space_un = criteria_line[0].split(":")[0].split("x")
        criteria_space = (int(criteria_space_un[0]), int(criteria_space_un[1]))
        criteria_pattern_counts = list(map(int, criteria_line[1:]))
        num_patterns = sum(criteria_pattern_counts)
        is_fast_accept, is_fast_reject = False, False
        # fast acceptance: if all 3x3 can fit in criteria space
        num_fit_x = criteria_space[0] // 3
        num_fit_y = criteria_space[1] // 3
        if num_fit_x * num_fit_y >= num_patterns:
            is_fast_accept = True
            print("Fast accept")
        # fast reject: if total space in criteria space < total space of patterns
        total_space = criteria_space[0] * criteria_space[1]
        total_pattern_space = sum(
            pattern_sizes[i] * criteria_pattern_counts[i] for i in range(len(patterns))
        )
        if total_space < total_pattern_space:
            is_fast_reject = True
            print("Fast reject")
        if not is_fast_accept and not is_fast_reject:
            print("Need further analysis")
        res += int(is_fast_accept)  # count only fast accepts
    print(res)


if __name__ == "__main__":
    main()
