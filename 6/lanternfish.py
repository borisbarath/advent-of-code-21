import os
from collections import defaultdict

with open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r') as input:
    starting_state = [int(days) for days in input.readlines()[0].split(',')]
    simulation_day = defaultdict(int)
    for item in starting_state:
        if item not in simulation_day:
            simulation_day[item] = 0
        simulation_day[item] += 1

    for _ in range(256):
        new_day = defaultdict(int)
        for days, count in simulation_day.items():
            if days == 0:
                new_day[6] += count
                new_day[8] += count
            else:
                new_day[days - 1] += count
        simulation_day = new_day
    print(sum(simulation_day.values()))