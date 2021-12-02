import os, sys

with open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r') as input:
    commands = [command.split() for command in input.readlines()]
    depth = 0
    horizontal = 0
    for (cmd, dist) in commands:
        distance = int(dist)
        if cmd == "forward":
            horizontal += distance
        elif cmd == "up":
            depth -= distance
        elif cmd == "down":
            depth += distance
    print("depth: {}, horizontal: {}".format(depth, horizontal))
    print(depth * horizontal)