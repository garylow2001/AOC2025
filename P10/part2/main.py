# Example run: # python3 main.py < test.in > test.out
from collections import deque
import z3


def parse_final(final_str):
    # convert to list of joltages e.g. {3,5,4,7} -> [3,5,4,7]
    final_str = final_str[1:-1].split(",")
    return list(map(int, final_str))


def parse_button(button_str):
    # convert to list of indexes to increment the counter e.g. "(1,3)" -> [1,3]
    ints_in_str = button_str[1:-1].split(",")
    return list(map(int, ints_in_str))


def increment_state(state, button):
    # returns new tuple (immutable) state after applying button
    new_state = list(state)
    for index in button:
        new_state[index] += 1
    return tuple(new_state)


def solve(final, buttons):
    # what if we represent final and buttons as matrices and find RREF
    # a1x1 + a2x2 + ... + anxn = final
    # xi is the button vector, ai is the number of times we press button i
    # sum of a1 + a2 + ... + an = min steps -> {a1, a2, ..., an} = b, the vector of counts
    # X.b = F   where X is matrix of buttons, b is vector of counts, F is final state
    solver = z3.Optimize()
    vars = z3.Ints(" ".join([f"x{i}" for i in range(len(buttons))]))
    for v in vars:
        solver.add(v >= 0)  # non-negative
    for i, joltage in enumerate(final):
        equation = 0
        for b, button in enumerate(buttons):
            if i in button:
                equation += vars[b]
        solver.add(equation == joltage)
    solver.minimize(z3.Sum(vars))
    solver.check()
    return solver.model().eval(z3.Sum(vars)).as_long()


def main():
    res = 0

    # read from test.in
    with open(0) as file:
        lines = file.readlines()

    processed_lines = [line.strip() for line in lines if line.strip()]
    for line in processed_lines:
        sections = line.split(" ")
        final = sections[-1]
        final = parse_final(final)
        buttons = sections[1:-1]  # ignore last rating
        buttons = [parse_button(b) for b in buttons]
        sol = solve(final, buttons)
        res += sol

    print(res)


if __name__ == "__main__":
    main()
