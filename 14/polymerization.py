import os
from collections import defaultdict

with open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r') as input:
    lines = input.readlines()

    starting_chain = lines[0].strip()
    rules = {}
    for line in lines[2:]:
        rules[line[0:2]] = line[6]

    counts = defaultdict(int)
    letter_counts = defaultdict(int)
    for char in starting_chain:
        letter_counts[char] += 1
    for i in range(0, len(starting_chain) - 1):
        counts[starting_chain[i:i + 2]] += 1

    for _ in range(40):
        new_counts = defaultdict(int)
        for (first, second), count in counts.items():
            middle = rules[first + second]
            letter_counts[middle] += count
            new_counts[first + middle] += count
            new_counts[middle + second] += count
        counts = new_counts

    print(letter_counts)
    print(max(letter_counts.values()) - min(letter_counts.values()))