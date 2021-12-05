import os, re


def process_input(raw_input):
    output = []
    for line in raw_input:
        numbers = re.findall('[0-9]+', line)
        output.append([int(num) for num in numbers])
    return output


def find_lines(lines, grid):
    for (x1, y1, x2, y2) in lines:
        if y1 == y2:
            min_x, max_x = min(x1, x2), max(x1, x2)
            for x in range(min_x, max_x + 1):
                grid[y1][x] += 1
        elif x1 == x2:
            min_y, max_y = min(y1, y2), max(y1, y2)
            for y in range(min_y, max_y + 1):
                grid[y][x1] += 1
        else:
            min_y, max_y = min(y1, y2), max(y1, y2)
            min_x, max_x = min(x1, x2), max(x1, x2)
            x_indices = [x for x in range(min_x, max_x + 1)]
            y_indices = [y for y in range(min_y, max_y + 1)]
            if x1 > x2:
                x_indices.reverse()
            if y1 > y2:
                y_indices.reverse()
            for (x, y) in zip(x_indices, y_indices):
                grid[y][x] += 1


def count_positions_greater_than(freq, grid):
    count = 0
    for row in grid:
        for elem in row:
            if elem >= freq:
                count += 1
    print(count)


with open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r') as input:
    raw_input = [line.strip() for line in input.readlines()]
    lines = process_input(raw_input)
    max_x = max([max(x1, x2) for (x1, _, x2, _) in lines]) + 1
    max_y = max([max(y1, y2) for (_, y1, _, y2) in lines]) + 1
    grid = [[0 for _ in range(max_x)] for _ in range(max_y)]

    find_lines(lines, grid)
    count_positions_greater_than(2, grid)
