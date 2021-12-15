import os, sys
from queue import PriorityQueue

with open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r') as input:
    grid = [[int(risk) for risk in line.strip()] for line in input.readlines()]
    # grid = [[1, 1], [1, 1]]
    part_2_grid = [[0 for _ in range(len(grid[0]) * 5)]
                   for _ in range(len(grid) * 5)]

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            x_offset = len(grid)
            y_offset = len(grid[0])
            for i in range(0, 5):
                for j in range(0, 5):
                    num = grid[x][y] + i + j
                    part_2_grid[x + i * x_offset][
                        y + j * y_offset] = num % 9 if num > 9 else num
    neighbor_offsets = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    costs = [[sys.maxsize for _ in row] for row in part_2_grid]
    costs[0][0] = 0

    q = PriorityQueue()
    q.put((0, (0, 0)))

    visited = set()
    visited.add(((0, 0)))

    while not q.empty():
        (cost, (x, y)) = q.get()
        visited.add((x, y))

        for (x_offset, y_offset) in neighbor_offsets:
            nx = x + x_offset
            ny = y + y_offset
            if 0 <= nx < len(part_2_grid):
                if 0 <= ny < len(part_2_grid[0]):
                    if (nx, ny) not in visited:
                        old_cost = costs[nx][ny]
                        new_cost = cost + part_2_grid[nx][ny]
                        if new_cost < old_cost:
                            costs[nx][ny] = new_cost
                            q.put((new_cost, (nx, ny)))

    print(costs[-1][-1])
