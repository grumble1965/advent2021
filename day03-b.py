import sys


def compute_counters(input_list):
    counters, starting = [], True
    for line in input_list:
        bits = line.strip()

        if starting:
            for ch in bits:
                counters.append(0)
            starting = False

        for idx in range(len(bits)):
            if bits[idx] == '1':
                counters[idx] += 1
            elif bits[idx] == '0':
                counters[idx] -= 1

    return counters


def filter_list(bit_position, keep_bit, input_list):
    tmp_list = []
    for element in input_list:
        if element[bit_position] == keep_bit:
            tmp_list.append(element)
    return tmp_list


def main():
    if len(sys.argv) != 2:
        sys.exit("Please provide a file name for input data")

    filename = sys.argv[1]
    with open(filename, "r") as inputfile:
        lines = []
        for line in inputfile.readlines():
            lines.append(line.strip())

        counters = compute_counters(lines)
        bit_length = len(counters)

        o2_generator_list = lines
        bit_position = 0
        while len(o2_generator_list) > 1:
            counters = compute_counters(o2_generator_list)
            if counters[bit_position] >= 0:
                keep_bit = '1'
            else:
                keep_bit = '0'
            o2_generator_list = filter_list(bit_position, keep_bit, o2_generator_list)
            bit_position += 1
        o2_generator_list[0]

        co2_scrubber_list = lines
        bit_position = 0
        while len(co2_scrubber_list) > 1:
            counters = compute_counters(co2_scrubber_list)
            if counters[bit_position] >= 0:
                keep_bit = '0'
            else:
                keep_bit = '1'
            co2_scrubber_list = filter_list(bit_position, keep_bit, co2_scrubber_list)
            bit_position += 1
        co2_scrubber_list[0]

        o2_reading, co2_reading = 0, 0
        for idx in range(bit_length):
            o2_reading = o2_reading * 2 + (1 if o2_generator_list[0][idx] == '1' else 0)
            co2_reading = co2_reading * 2 + (1 if co2_scrubber_list[0][idx] == '1' else 0)

        print(f"o2 = {o2_reading}  co2 = {co2_reading}  life support = {o2_reading * co2_reading}")


if __name__ == '__main__':
    main()
