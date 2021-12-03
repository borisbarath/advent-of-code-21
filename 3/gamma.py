import os


def get_one_counts(readings):
    count_ones = [0 for _ in range(len(readings[0]) - 1)]
    for reading in readings:
        for bit_index in range(len(reading)):
            if reading[bit_index] == "1":
                count_ones[bit_index] += 1
    return count_ones


def get_gamma_epsilon(readings):
    count_ones = get_one_counts(readings)
    gamma = ""
    epsilon = ""
    for bit_count in count_ones:
        if bit_count < len(readings) // 2:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"
    print(gamma)
    print(epsilon)
    print(int(gamma, 2) * int(epsilon, 2))
    print("================================")


def most_common_bit_per_position(readings):
    count_ones = get_one_counts(readings)
    most_common_bit_per_position = ""
    for bit_count in count_ones:
        if bit_count > 0 and len(readings) / bit_count == 2:
            most_common_bit_per_position += "1"
        # if equal counts, take ones
        elif bit_count <= len(readings) // 2:
            most_common_bit_per_position += "0"
        else:
            most_common_bit_per_position += "1"
    return most_common_bit_per_position


def least_common_bit_per_position(readings):
    count_ones = get_one_counts(readings)
    least_common_bit_per_position = ""
    for bit_count in count_ones:
        if bit_count > 0 and len(readings) / bit_count == 2:
            least_common_bit_per_position += "0"
        # if equal counts, take ones
        elif bit_count <= len(readings) // 2:
            least_common_bit_per_position += "1"
        else:
            least_common_bit_per_position += "0"

    return least_common_bit_per_position


def get_num_with_most_common_bits(readings):
    filtered_readings = readings
    for index in range(len(readings[0])):
        readings_to_filter = filtered_readings
        most_common_bits = most_common_bit_per_position(readings_to_filter)
        filtered_readings = []
        for reading in readings_to_filter:
            if reading[index] == most_common_bits[index]:
                filtered_readings.append(reading)
        if len(filtered_readings) == 1:
            return (filtered_readings[0])


def get_num_with_least_common_bits(readings):
    filtered_readings = readings
    for index in range(len(readings[0])):
        readings_to_filter = filtered_readings
        least_common_bits = least_common_bit_per_position(readings_to_filter)
        filtered_readings = []
        for reading in readings_to_filter:
            if reading[index] == least_common_bits[index]:
                filtered_readings.append(reading)
        if len(filtered_readings) == 1:
            return (filtered_readings[0])


def get_oxygen_co2(readings):
    oxygen_generator = get_num_with_most_common_bits(readings)

    co2_scrubber = get_num_with_least_common_bits(readings)

    print(oxygen_generator)
    print(co2_scrubber)
    print(int(oxygen_generator, 2) * int(co2_scrubber, 2))
    print("================================")


with open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r') as input:
    readings = [reading for reading in input.readlines()]
    get_gamma_epsilon(readings)
    get_oxygen_co2(readings)
