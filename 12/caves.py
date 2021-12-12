import os
from collections import defaultdict


def dfs_paths(visited, edges, path, current_node, visited_small):
    finished_paths = 0

    if current_node == "start" and current_node in visited:
        return 0
    if current_node.islower():
        if current_node in visited:
            if visited_small:
                return finished_paths
            visited_small = True

    local_visited = visited.copy()
    local_visited.add(current_node)
    local_path = []
    local_path.extend(path)
    local_path.append(current_node)

    if current_node == "end":
        return 1

    for neighbor in edges[current_node]:
        finished_paths += dfs_paths(local_visited, edges, local_path, neighbor,
                                    visited_small)
    return finished_paths


with open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r') as input:
    edges = defaultdict(set)
    lines = [line.strip() for line in input]

    for line in lines:
        [node_1, node_2] = line.split("-")
        edges[node_1].add(node_2)
        edges[node_2].add(node_1)

        visited = set()
    print(dfs_paths(visited, edges, [], "start", False))
