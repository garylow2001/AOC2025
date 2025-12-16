# Example run: # python3 main.py < test.in > test.out


def main():
    # read from test.in
    with open(0) as file:
        lines = file.readlines()

    processed_lines = [line.strip() for line in lines if line.strip()]
    res = 0
    intervals = []
    ingredients_to_check = []
    for line in processed_lines:
        if "-" in line:
            start, end = line.split("-")
            intervals.append([int(start), int(end)])
        else:
            ingredients_to_check.append(int(line))
    intervals.sort(key=lambda x: x[0])
    # merge intervals
    merged_intervals = [intervals[0]]
    for i in range(1, len(intervals)):
        if intervals[i][0] <= merged_intervals[-1][1] + 1:
            merged_intervals[-1][1] = max(merged_intervals[-1][1], intervals[i][1])
        else:
            merged_intervals.append(intervals[i])
    print(merged_intervals)
    # linear search suffices
    for ingredient in ingredients_to_check:
        for start, end in merged_intervals:
            if start <= ingredient <= end:
                res += 1
                break
    print(res)


if __name__ == "__main__":
    main()
