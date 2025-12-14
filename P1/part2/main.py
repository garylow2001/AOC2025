# Example run: # python3 main.py < test.in > test.out
# Not enough stars to start this puzzle


def main():
    res = 0

    # read from test.in
    with open(0) as file:
        lines = file.readlines()

    processed_lines = [line.strip() for line in lines if line.strip()]
    # convert lines to array of increments
    incr = [
        int(line[1:]) if line[0] == "R" else -int(line[1:]) for line in processed_lines
    ]
    curr = 50
    MOD = 100  # circular range of numbers from 0 to 99
    for i in incr:
        if i < 0:
            # turn left, possibly go below 0
            counts = i // -MOD  # number of full cycles
            # count if remaining part crosses zero
            leftover_incr = i % -MOD
            start = curr
            if start > 0 and curr + leftover_incr <= 0:
                counts += 1
            res += counts
            print(f"left turn by {i} from {start} to {curr + i}, counts: {counts}")
        else:
            # turn right, possibly go above 99
            counts = i // MOD  # number of full cycles from turns itself
            # count if remaining part crosses zero
            leftover_incr = i % MOD
            start = curr
            if curr + leftover_incr >= 100:
                counts += 1
            res += counts
            print(f"right turn by {i} from {start} to {curr + i}, counts: {counts}")
        curr = (curr + i) % MOD
    print("Total times crossed 0:", res)


if __name__ == "__main__":
    main()
