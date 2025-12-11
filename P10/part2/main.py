# Example run: # python3 main.py < test.in > test.out
from collections import deque


def parse_final(final_str):
    # convert to bitmap for example [.##.] -> 0b0110 = 6
    final_str = final_str[1:-1]
    bitmap = 0b0
    for i, ch in enumerate(final_str):
        if ch == "#":
            bitmap |= 1 << i
    return bitmap


def parse_button(button_str):
    # convert to bitmask to xor later, for example "(1,3)" -> 0b1010 = 10
    ints_in_str = button_str[1:-1].split(",")
    bitmask = 0b0
    for num_str in ints_in_str:
        num = int(num_str)
        bitmask |= 1 << num  # convert to 0-based index
    return bitmask


def solve(final, buttons):
    # final and buttons are in binary
    initial = 0b0
    queue = deque()
    visited = set()
    for b in buttons:
        next_step = initial ^ b
        visited.add(next_step)
        queue.append((next_step, 1))  # (state, num_steps)
    while queue:
        state, num_steps = queue.popleft()
        if state == final:
            return num_steps
        for b in buttons:
            next_step = state ^ b
            if next_step not in visited:
                visited.add(next_step)
                queue.append((next_step, num_steps + 1))
    print("cant be solved")
    return -1  # impossible to reach, explored all states already


def main():
    res = 0

    # read from test.in
    with open(0) as file:
        lines = file.readlines()

    processed_lines = [line.strip() for line in lines if line.strip()]
    for line in processed_lines:
        sections = line.split(" ")
        final = sections[0]
        final = parse_final(final)
        buttons = sections[1:-1]  # ignore last rating
        buttons = [parse_button(b) for b in buttons]
        sol = solve(final, buttons)
        res += sol

    print(res)


if __name__ == "__main__":
    main()
