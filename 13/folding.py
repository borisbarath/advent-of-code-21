import os

with open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r') as input:
    lines = [line.strip() for line in input]

    fold_commands = []
    dot_coords = []

    for idx, line in enumerate(lines):
        if line == "":
            fold_commands = [(cmd[11], int(cmd[13:]))
                             for cmd in lines[idx + 1:]]
            break
        [x, y] = line.split(',')
        dot_coords.append((int(x), int(y)))

    for (axis, line) in fold_commands:
        folded_dot_coords = set()
        for (x, y) in dot_coords:
            if axis == "x":
                folded_dot_coords.add((x if x < line else 2 * line - x, y))
            else:
                folded_dot_coords.add((x, y if y < line else 2 * line - y))
        dot_coords = folded_dot_coords

    max_x = max([x for x, _ in dot_coords])
    max_y = max([y for _, y in dot_coords])
    paper = [[" " for x in range(max_x + 1)] for y in range(max_y + 1)]

    for (x, y) in dot_coords:
        paper[y][x] = "#"

    for line in paper:
        print(''.join(line))
