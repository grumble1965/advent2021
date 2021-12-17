import sys


hex_nibble_to_bits = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101',
                      '6': '0110', '7': '0111', '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
                      'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}


def bit_string_to_int(bit_str):
    res = 0
    for ch in bit_str:
        res = res * 2
        res = res + 1 if ch == '1' else res
    return res


def main():
    if len(sys.argv) != 2:
        sys.exit("Please provide a file name for input data")

    filename = sys.argv[1]
    with open(filename, "r") as inputfile:

        while True:
            line = inputfile.readline()
            if not line:
                break
            tmp = line.strip()
            # print(f"{tmp}")

            bit_str = ''
            for ch in tmp:
                bit_str += hex_nibble_to_bits[ch]
            bit_arr = [ch for ch in bit_str]
            # print(f"{tmp} -> {bit_arr}")

            deal_with_packet(bit_arr)

            print()

            # print(f"{version} {type_id} : {body}")


def deal_with_packet(bit_arr):
    tt, new_bit_arr, consumed, value, version = parse_bit_string(bit_arr)
    if tt == 'Literal':
        print(f"{tt}, {value} {new_bit_arr}")
        bit_arr = new_bit_arr
    elif tt == 'Operator Length':
        print(f"{tt} {value} bits:  {new_bit_arr}")
        length_remaining = value
        while length_remaining > 0:
            bit_arr = new_bit_arr
            tt, new_bit_arr, consumed, value, ver_tmp = parse_bit_string(bit_arr)
            print(f"{consumed} bits for {tt} {value}")
            length_remaining -= consumed
            version += ver_tmp
    elif tt == 'Operator Number':
        print(f"{tt} {value} sub packets:  {new_bit_arr}")
        for subpkt in range(value):
            bit_arr = new_bit_arr
            tt, new_bit_arr, consumed, value, ver_tmp = parse_bit_string(bit_arr)
            print(f"sub packet # {subpkt}  for {tt} {value}")
            version += ver_tmp
    else:
        print("Unknown packet type")
        bit_arr = new_bit_arr[1:]
    print(f"total version = {version}")


def parse_bit_string(bit_arr):
    consumed = 0
    version = bit_string_to_int(bit_arr[0:3])
    consumed += 3
    type_id = bit_string_to_int(bit_arr[3:6])
    consumed += 3
    body = bit_arr[6:]
    if type_id == 4:
        literal = 0
        while True:
            last_nibble = body.pop(0)
            b3, b2, b1, b0 = body.pop(0), body.pop(0), body.pop(0), body.pop(0)
            consumed += 5
            literal = literal * 16
            literal += bit_string_to_int([b3, b2, b1, b0])
            if last_nibble == '0':
                break
        # print(f"Literal pkt {literal} with {body} left over")
        return 'Literal', body, consumed, literal, version
    else:
        try:
            length_type_id = body.pop(0)
            consumed += 1
            if length_type_id == '0':
                # total length in bits
                length, subpkt = body[0:15], body[15:]
                consumed += 15
                total_length = bit_string_to_int(length)
                # print(f"Operator pkt : total length of subpkts = {total_length}/{length} with {subpkt} left over")
                return 'Operator Length', subpkt, consumed, total_length, version
            elif length_type_id == '1':
                # number of subpackets
                num_pkts, subpkt = body[0:11], body[11:]
                consumed += 11
                total_pkts = bit_string_to_int(num_pkts)
                # print(f"Operator pkt : total number of subpkts = {total_pkts} with {subpkt} left over")
                return 'Operator Number', subpkt, consumed, total_pkts, version
            else:
                return "Unknown", body, consumed, None
        except Exception as s:
            return "Unknown", body, consumed, None


if __name__ == '__main__':
    main()
