import os

with open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r') as input:
    inputs = [line.strip() for line in input.readlines()]
    result = []
    for line in inputs:

        [all_digits, reading] = line.split("|")
        digits_by_num_segments = {}
        for digit in all_digits.split():
            num_segments = len(digit)
            if num_segments not in digits_by_num_segments:
                digits_by_num_segments[num_segments] = [set(digit)]
            else:
                digits_by_num_segments[num_segments].append(set(digit))

        known_segments = ["" for _ in range(10)]
        known_segments[1] = digits_by_num_segments[2][0]
        known_segments[7] = digits_by_num_segments[3][0]
        known_segments[4] = digits_by_num_segments[4][0]
        known_segments[8] = digits_by_num_segments[7][0]

        for idx, digit in enumerate(digits_by_num_segments[6]):
            if not (known_segments[1] < digit):
                known_segments[6] = digit
                del (digits_by_num_segments[6][idx])

        top_right_segment = known_segments[1] - known_segments[6]

        for idx, digit in enumerate(digits_by_num_segments[5]):
            if not (top_right_segment < digit):
                known_segments[5] = digit
                del (digits_by_num_segments[5][idx])
        bottom_left_digit = known_segments[6] - known_segments[5]

        for digit in digits_by_num_segments[5]:
            digit_difference = known_segments[6] - digit
            if bottom_left_digit < digit_difference:
                known_segments[3] = digit
            else:
                known_segments[2] = digit
        bottom_left_digit = known_segments[6] - known_segments[5]
        for digit in digits_by_num_segments[6]:
            if bottom_left_digit < digit:
                known_segments[0] = digit
            else:
                known_segments[9] = digit

        decoded_reading = ""
        for number in reading.split():
            for idx, digits in enumerate(known_segments):
                if set(number) == digits:
                    decoded_reading += str(idx)

        result.append(int(decoded_reading))
    print(sum(result))