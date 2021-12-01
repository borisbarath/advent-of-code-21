import os, sys

with open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r') as input:
    measurements = [int(depth) for depth in input.readlines()]
    increased_measurements = [
        1 if nxt > curr else 0
        for (curr,
             nxt) in zip(measurements, measurements[1:] + [-sys.maxsize - 1])
    ]
    print("the depth increased {} times".format(sum(increased_measurements)))

    increases = 0
    for i in range(2, len(measurements)):
        if (i < len(measurements) - 1):
            window = sum(measurements[i - 2:i + 1])
            next_window = sum(measurements[i - 1:i + 2])
            if window < next_window:
                increases += 1
    print("the depth increased {} times with a sliding window of 3".format(
        increases))
