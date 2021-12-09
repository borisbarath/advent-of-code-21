import os, queue
from functools import reduce


def get_neighbors(map, x, y):
    num_rows, num_cols = len(map), len(map[0])
    neighbor_offsets = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    result = []
    for (x_offset, y_offset) in neighbor_offsets:
        if 0 <= x + x_offset < num_rows and 0 <= y + y_offset < num_cols:
            result.append((x + x_offset, y + y_offset))
    return result


with open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r') as input:
    height_map = [[int(height) for height in line.strip()]
                  for line in input.readlines()]
    local_minima = []
    minima_indices = []
    neighbor_offsets = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    for row_idx, row in enumerate(height_map):
        for col_idx, height in enumerate(row):
            is_minimum = True
            for (neighbor_x,
                 neighbor_y) in get_neighbors(height_map, row_idx, col_idx):
                is_minimum &= height_map[neighbor_x][neighbor_y] > height
            if is_minimum:
                local_minima.append((row_idx, col_idx))

    basin_sizes = []
    for (min_x, min_y) in local_minima:
        visited = set()
        visited.add(((min_x, min_y)))
        q = queue.Queue()
        [
            q.put(neighbor_coords)
            for neighbor_coords in get_neighbors(height_map, min_x, min_y)
        ]
        while not q.empty():
            (x, y) = q.get()
            visited.add((x, y))
            if height_map[x][y] != 9:
                [
                    q.put(neighbor)
                    for neighbor in get_neighbors(height_map, x, y)
                    if neighbor not in visited
                ]
        basin_size = sum([1 for (x, y) in visited if height_map[x][y] != 9])
        basin_sizes.append(basin_size)
    basin_sizes.sort()
    print(reduce(lambda x, y: x * y, basin_sizes[-3:]))
