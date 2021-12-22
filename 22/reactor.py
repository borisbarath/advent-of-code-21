import os


def overlap(c, newc):
    c_on, c_x, c_y, c_z = c
    _, newc_x, newc_y, newc_z = newc
    if (newc_x[0] > c_x[1] or newc_x[1] < c_x[0]) or (
            newc_y[0] > c_y[1]
            or newc_y[1] < c_y[0]) or newc_z[0] > c_z[1] or newc_z[1] < c_z[0]:
        return None
    min_x = max(c_x[0], newc_x[0])
    max_x = min(c_x[1], newc_x[1])
    min_y = max(c_y[0], newc_y[0])
    max_y = min(c_y[1], newc_y[1])
    min_z = max(c_z[0], newc_z[0])
    max_z = min(c_z[1], newc_z[1])
    result_on = 1 if c_on == 0 else 0
    return (result_on, (min_x, max_x), (min_y, max_y), (min_z, max_z))


def volume(cube):
    on, x, y, z = cube
    mul = 1 if on == 1 else -1
    return mul * (x[1] - x[0] + 1) * (y[1] - y[0] + 1) * (z[1] - z[0] + 1)


with open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r') as input:
    raw_ranges = input.readlines()
    cubes = []

    for rng in raw_ranges:
        status, xyz_raw = rng.split(' ')
        status = 1 if status == "on" else 0
        xyz = xyz_raw.strip().split(',')
        xyz_ranges = [[int(val) for val in rng_str[2:].split('..')]
                      for rng_str in xyz]
        cubes.append(tuple([status] + xyz_ranges))
# simple sanity check input:
# cubes = [(1, (1, 4), (1, 4), (1, 4)), (0, (4, 4), (1, 4), (1, 4)),
#          (1, (4, 4), (1, 4), (1, 4)), (0, (2, 3), (2, 3), (2, 3))]
result_cubes = []
for cube in cubes:
    sub_result = []
    for res_cube in result_cubes:
        overlap_cube = overlap(res_cube, cube)

        if overlap_cube is None:
            continue
        sub_result.append(overlap_cube)
    if cube[0] == 1:
        result_cubes.append(cube)
    result_cubes.extend(sub_result)

volumes = [volume(cube) for cube in result_cubes]
print(sum(volumes))
