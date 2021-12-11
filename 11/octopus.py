import os, queue, pprint


def get_neighbors(map, x, y, neighbors_to_exclude):
    num_rows, num_cols = len(map), len(map[0])
    result = []
    for x_offset in range(-1, 2):
        for y_offset in range(-1, 2):
            if 0 <= x + x_offset < num_rows and 0 <= y + y_offset < num_cols:
                if (x + x_offset, y + y_offset) not in neighbors_to_exclude:
                    result.append((x + x_offset, y + y_offset))
    return result


def zero_energies(energies):
    result = []
    for row in energies:
        result_row = []
        for energy in row:
            result_row.append(0 if energy > 9 else energy)
        result.append(result_row)
    return result


def increase_energy(energies):
    result = []
    for row in energies:
        result_row = []
        for energy in row:
            result_row.append(energy + 1)
        result.append(result_row)
    return result


with open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r') as input:
    energies = [[int(num) for num in line.strip()]
                for line in input.readlines()]

    total_flashes = 0
    simultaneous_flashes = []
    for iteration in range(1000):
        # First, the energy level of each octopus increases by 1.
        new_energies = increase_energy(energies)

        flashed_octopuses = set()
        neighbors_to_increase = queue.Queue()

        for row_idx, row in enumerate(new_energies):
            for col_idx, energy in enumerate(row):
                # Then, any octopus with an energy level greater than 9 flashes.
                if energy > 9:
                    flashed_octopuses.add(((row_idx, col_idx)))

        for (x, y) in flashed_octopuses:
            neighbors = get_neighbors(new_energies, x, y, flashed_octopuses)
            for neighbor in neighbors:
                neighbors_to_increase.put(neighbor)

        # This process continues as long as new octopuses keep having their energy level increased beyond 9.
        while not neighbors_to_increase.empty():
            (x, y) = neighbors_to_increase.get()
            # This increases the energy level of all adjacent octopuses by 1, including octopuses that are diagonally adjacent.
            new_energies[x][y] += 1
            # If this causes an octopus to have an energy level greater than 9, it also flashes.
            # (An octopus can only flash at most once per step.)
            if new_energies[x][y] > 9 and not (x, y) in flashed_octopuses:
                flashed_octopuses.add(((x, y)))
                neighbors = get_neighbors(new_energies, x, y,
                                          flashed_octopuses)
                for neighbor in neighbors:
                    neighbors_to_increase.put(neighbor)

        new_energies = zero_energies(new_energies)
        if (len(flashed_octopuses) == 100):
            print("Synchronised flash at", iteration + 1)
            break
        # make a queue of neighbors. while queue not empty: go through the queue. increase each value by 1.
        # if >9 and not in flashed_octopuses flash and add to flashed and add its neighbors to the queue

        energies = new_energies
    print(total_flashes)
