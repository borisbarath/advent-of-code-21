import os, queue


def compute_score(line):
    score = 0
    for bracket in line:
        score = score * 5 + scores[bracket]
    return score


opposing_brackets = {"(": ")", "[": "]", "{": "}", "<": ">"}
scores = {")": 1, "]": 2, "}": 3, ">": 4}

with open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r') as input:
    lines = [line.strip() for line in input.readlines()]
    corrupting_chars = []
    completing_lines = []
    for line in lines:
        open_queue = queue.LifoQueue()
        corrupt = False
        for char in line:
            if char in "{[<(":
                open_queue.put(char)
            else:
                last_opening_bracket = open_queue.get()
                if not opposing_brackets[last_opening_bracket] == char:
                    corrupting_chars.append(char)
                    corrupt = True
                    break
        if not corrupt and not open_queue.empty():
            missing_chars = ""
            while not open_queue.empty():
                missing_chars += opposing_brackets[open_queue.get()]
            completing_lines.append(missing_chars)

    scores = [compute_score(line) for line in completing_lines]
    scores.sort()
    print(scores[len(scores) // 2])