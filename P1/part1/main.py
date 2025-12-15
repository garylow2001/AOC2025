# Example run: # python3 main.py < test.in > test.out


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
        curr = (curr + i) % MOD
        if curr == 0:
            res += 1
    print(res)


if __name__ == "__main__":
    main()
