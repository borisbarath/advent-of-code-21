import os, sys
from collections import defaultdict


def movement_costs(largest_position):
    costs = [0]
    for i in range(1, largest_position + 1):
        costs.append(costs[i - 1] + i)
    return costs


with open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r') as input:
    positions = [int(position) for position in input.readlines()[0].split(',')]
    counter = defaultdict(int)
    largest_position = -sys.maxsize + 1
    smallest_position = sys.maxsize

    for position in positions:
        if position < smallest_position:
            smallest_position = position
        if position > largest_position:
            largest_position = position
        if position not in counter:
            counter[position] = 0
        counter[position] += 1

    movement_costs = movement_costs(largest_position)
    least_fuel = sys.maxsize
    for i in range(smallest_position, largest_position + 1):
        fuel = 0
        for position in counter:
            fuel += counter[position] * movement_costs[abs(position - i)]
        if fuel < least_fuel:
            least_fuel = fuel

    print(least_fuel)
