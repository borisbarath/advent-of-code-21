import os


def part_1(x_coords, y_coords):
    highest_position = 0
    hitting_positions = set()
    for x_start in range(1, x_coords[1] + 1):
        for y_start in range(1000, y_coords[0] - 1, -1):
            x_speed, y_speed = x_start, y_start
            x, y = 0, 0
            highest_try_position = 0
            while x <= x_coords[1] and y >= y_coords[0]:
                if x_speed == 0 and x < x_coords[0]:
                    break
                if x_coords[0] <= x <= x_coords[1] and y_coords[
                        0] <= y <= y_coords[1]:
                    hitting_positions.add((x_start, y_start))
                    if highest_position < highest_try_position:
                        highest_position = highest_try_position
                    break
                x += x_speed
                y += y_speed
                if y > highest_try_position:
                    highest_try_position = y
                if x_speed > 0:
                    x_speed -= 1
                y_speed -= 1
    print(highest_position)


def part_2(x_coords, y_coords):
    hitting_positions = set()
    for x_start in range(1, x_coords[1] + 1):
        for y_start in range(1000, y_coords[0] - 1, -1):
            x_speed, y_speed = x_start, y_start
            x, y = 0, 0
            while x <= x_coords[1] and y >= y_coords[0]:
                if x_speed == 0 and x < x_coords[0]:
                    break
                if x_coords[0] <= x <= x_coords[1] and y_coords[
                        0] <= y <= y_coords[1]:
                    hitting_positions.add((x_start, y_start))
                    break
                x += x_speed
                y += y_speed
                if x_speed > 0:
                    x_speed -= 1
                y_speed -= 1
    print(len(hitting_positions))


with open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r') as input:
    target_coords = input.read()[15:].split(", y=")
    x_coords = [int(x) for x in target_coords[0].split('..')]
    y_coords = [int(y) for y in target_coords[1].split('..')]

    part_1(x_coords, y_coords)
    part_2(x_coords, y_coords)
