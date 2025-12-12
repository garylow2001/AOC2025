# Example run: # python3 main.py < test.in > test.out
from collections import deque
from functools import cache


def main():
    # read from test.in
    with open(0) as file:
        lines = file.readlines()
    processed_lines = [line.strip() for line in lines if line.strip()]

    adj_list = {}

    for line in processed_lines:
        processed_line = line.split(" ")
        node = processed_line[0][:-1]  # remove colon
        edges = processed_line[1:]
        for e in edges:
            if node not in adj_list:
                adj_list[node] = []
            adj_list[node].append(e)

    # start from "you" find all paths to "out"
    @cache
    def getPaths(a, b):
        if a == b:
            return 1
        total_paths = 0
        for neighbor in adj_list.get(a, []):
            total_paths += getPaths(neighbor, b)
        return total_paths

    path1 = getPaths("svr", "dac") * getPaths("dac", "fft") * getPaths("fft", "out")
    path2 = getPaths("svr", "fft") * getPaths("fft", "dac") * getPaths("dac", "out")
    res = path1 + path2
    print(res)


if __name__ == "__main__":
    main()
