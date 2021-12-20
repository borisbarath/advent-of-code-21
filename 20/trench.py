from collections import defaultdict
import os


def new_value(x, y, pixels, algorithm):
    b = ""
    for i in range(-1, 2):
        for j in range(-1, 2):
            b += pixels[(x + i, y + j)]
    idx = int("".join(b), 2)
    return algorithm[idx]


def enhance(pixels, algorithm, default):
    new_pixels = defaultdict(lambda: default)
    old_pixels = pixels.copy()
    for (x, y) in old_pixels.keys():
        for i in range(-1, 2):
            for j in range(-1, 2):
                new_pixels[(x + i, y + j)] = new_value(x + i, y + j, pixels,
                                                       algorithm)
    return new_pixels


def find_white_pixels(pixels):
    return sum([int(val) for val in pixels.values()])


with open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r') as input:
    lines = input.readlines()
    alg_raw = lines[0].strip()
    pixels = defaultdict(lambda: "0")
    alg = ["1" if char == "#" else "0" for char in alg_raw]
    image = [["1" if char == "#" else "0" for char in line.strip()]
             for line in lines[2:]]
    for x in range(len(image)):
        for y in range(len(image[x])):
            pixels[(x, y)] = image[x][y]
    for iter in range(50):
        if iter % 2 == 0 or alg[0] == "0":
            default = alg[0]
        else:
            default = "0"
        pixels = enhance(pixels, alg, default)

print(find_white_pixels(pixels))
