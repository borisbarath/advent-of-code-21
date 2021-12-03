import os

with open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r') as input:
    commands = [command.split() for command in input.readlines()]
    depth = 0
    horizontal = 0
    aim = 0
    for (cmd, dist) in commands:
        distance = int(dist)
        if cmd == "forward":
            horizontal += distance
            depth += aim * distance
        elif cmd == "up":
            aim -= distance
        elif cmd == "down":
            aim += distance
    print("depth: {}, horizontal: {}, aim: {}".format(depth, horizontal, aim))
    print(depth * horizontal)