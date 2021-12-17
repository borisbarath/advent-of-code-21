import os
from functools import reduce


def b2i(binary):
    return (int(binary, 2))


class Packet:
    msg_id = -1,
    version = -1,
    length_type_id = -1
    subpackets = []
    value = -1

    def sum_versions(self):
        result = self.version
        for subpacket in self.subpackets:
            result += subpacket.sum_versions()
        return result

    def get_value(self):
        if self.msg_id == 4:
            return self.value
        values = list(map(lambda p: p.get_value(), self.subpackets))

        if self.msg_id == 0:
            return sum(values)
        elif self.msg_id == 1:
            return reduce((lambda x, y: x * y), values)
        elif self.msg_id == 2:
            return min(values)
        elif self.msg_id == 3:
            return max(values)
        elif self.msg_id == 5:
            return 1 if values[0] > values[1] else 0
        elif self.msg_id == 6:
            return 1 if values[0] < values[1] else 0
        elif self.msg_id == 7:
            return 1 if values[0] == values[1] else 0


def parse_literal(message):
    bit_groups = []
    group_start = 0
    group_length = 5
    while message[group_start] != "0":
        bit_groups.append(message[group_start + 1:group_start + group_length])
        group_start += group_length
    bit_groups.append(message[group_start + 1:group_start + group_length])
    value = b2i(''.join(bit_groups))
    parsed_length = group_start + group_length
    return value, parsed_length


def parse_input(message):
    msg_id = b2i(message[3:6])
    message_body = message[6:]
    parsed_packet = Packet()
    parsed_packet.version = b2i(message[:3])
    parsed_packet.msg_id = msg_id
    if msg_id == 4:
        value, _ = parse_literal(message_body)
        parsed_packet.value = value
        return parsed_packet

    parsed_packet.length_type_id = b2i(message_body[0])
    if message_body[0] == "0":
        subpacket_length = b2i(message_body[1:16])
        parsed_packet.subpackets, _ = parse_subpackets(message_body[16:],
                                                       subpacket_length, -1)
    else:
        num_subpackets = b2i(message_body[1:12])
        parsed_packet.subpackets, _ = parse_subpackets(message_body[12:], -1,
                                                       num_subpackets)
    return parsed_packet


def parse_subpackets(body, sub_len_bits, sub_num):
    subpackets = []
    i = 0
    if sub_len_bits != -1:
        processed_bits = 0
        while processed_bits < sub_len_bits and b2i(body[i:]) != 0:
            packet = Packet()
            packet.version = b2i(body[i:i + 3])
            packet.msg_id = b2i(body[i + 3:i + 6])
            i += 6
            if packet.msg_id == 4:
                value, parsed_length = parse_literal(body[i:])
                i += parsed_length
                packet.value = value
                subpackets.append(packet)
                processed_bits = i
            else:
                packet.length_type_id = b2i(body[i])
                i += 1
                if packet.length_type_id == 0:
                    subpacket_length = b2i(body[i:i + 15])
                    i += 15
                    sub_subpackets, bits_processed = parse_subpackets(
                        body[i:], subpacket_length, -1)
                    i += bits_processed
                else:
                    num_subpackets = b2i(body[i:i + 11])
                    i += 11
                    sub_subpackets, bits_processed = parse_subpackets(
                        body[i:], -1, num_subpackets)
                    i += bits_processed
                packet.subpackets = sub_subpackets
                subpackets.append(packet)
                processed_bits = i

    elif sub_num != -1:
        processed_packets = 0
        while processed_packets < sub_num and b2i(body[i:]) != 0:
            packet = Packet()
            packet.version = b2i(body[i:i + 3])
            packet.msg_id = b2i(body[i + 3:i + 6])
            i += 6
            if packet.msg_id == 4:
                value, parsed_length = parse_literal(body[i:])
                i += parsed_length
                packet.value = value
                processed_packets += 1
                subpackets.append(packet)
            else:
                packet.length_type_id = b2i(body[i])
                i += 1
                if packet.length_type_id == 0:
                    subpacket_length = b2i(body[i:i + 15])
                    i += 15
                    sub_subpackets, bits_processed = parse_subpackets(
                        body[i:], subpacket_length, -1)
                    i += bits_processed
                else:
                    num_subpacket = b2i(body[i:i + 11])
                    i += 11
                    sub_subpackets, bits_processed = parse_subpackets(
                        body[i:], -1, num_subpacket)
                    i += bits_processed
                packet.subpackets = sub_subpackets
                processed_packets += 1
                subpackets.append(packet)
    return subpackets, i


with open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r') as input:
    hex_input = input.readlines()[0]
    hex_size = len(hex_input) * 4
    bin_input = (bin(int(hex_input, 16))[2:]).zfill(hex_size)

    parsed_packet = parse_input(bin_input)
    print(parsed_packet.sum_versions())
    print(parsed_packet.get_value())