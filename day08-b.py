import sys
from itertools import permutations

seven_seg = {'0': 'abcefg', '1': 'cf', '2': 'acdeg', '3': 'acdfg', '4': 'bcdf', '5': 'abdfg', '6': 'abdefg', '7': 'acf',
             '8': 'abcdfg'}


def assign(mapping, key_k, value_v):
    new_map = {}
    for k, v in mapping.items():
        if k == key_k:
            new_map[k] = [value_v]
        else:
            v_new = v
            if value_v in v:
                v_new.remove(value_v)
            new_map[k] = v_new
    return new_map


def remove(mapping, key_k, value_v):
    new_map = {}
    for k, v in mapping.items():
        if k == key_k:
            v_new = v
            if value_v in v:
                v_new.remove(value_v)
            new_map[k] = v_new
        else:
            new_map[k] = v
    return new_map


def main():
    if len(sys.argv) != 2:
        sys.exit("Please provide a file name for input data")

    total_sum = 0
    filename = sys.argv[1]
    with open(filename, "r") as inputfile:
        while True:
            line = inputfile.readline()
            if not line:
                break

            display = line.strip().split()
            patterns = display[0:10]
            digits = display[11:]

            frequency = {'a': 0, 'b': 0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0}
            for pp in patterns:
                for ch in pp:
                    frequency[ch] += 1
            # print(f"{frequency}")

            mapping = {}
            for pp in patterns:
                mapping[pp] = [i for i in range(0, 10)]

            for pp in patterns:
                if len(pp) == 2:
                    mapping = assign(mapping, pp, 1)
                elif len(pp) == 3:
                    mapping = assign(mapping, pp, 7)
                elif len(pp) == 4:
                    mapping = assign(mapping, pp, 4)
                elif len(pp) == 5:
                    mapping = remove(mapping, pp, 0)
                    mapping = remove(mapping, pp, 1)
                    mapping = remove(mapping, pp, 4)
                    mapping = remove(mapping, pp, 6)
                    mapping = remove(mapping, pp, 7)
                    mapping = remove(mapping, pp, 8)
                    mapping = remove(mapping, pp, 9)
                elif len(pp) == 6:
                    mapping = remove(mapping, pp, 1)
                    mapping = remove(mapping, pp, 2)
                    mapping = remove(mapping, pp, 3)
                    mapping = remove(mapping, pp, 4)
                    mapping = remove(mapping, pp, 5)
                    mapping = remove(mapping, pp, 7)
                    mapping = remove(mapping, pp, 8)
                elif len(pp) == 7:
                    mapping = assign(mapping, pp, 8)

            digit1, digit4, digit7 = None, None, None
            for k, v in mapping.items():
                if v == [1]:
                    digit1 = k
                if v == [4]:
                    digit4 = k
                if v == [7]:
                    digit7 = k

            segment_b = None
            segment_e = None
            segment_f = None
            segments_ac = []
            segments_dg = []
            for k, v in frequency.items():
                if v == 4:
                    segment_e = k
                elif v == 6:
                    segment_b = k
                elif v == 7:
                    segments_dg.append(k)
                elif v == 8:
                    segments_ac.append(k)
                elif v == 9:
                    segment_f = k
            # print(f"segment_b = {segment_b}")
            # print(f"segment_e = {segment_e}")
            # print(f"segment_f = {segment_f}")

            tmp = [ch for ch in digit7]
            for ch in digit1:
                tmp.remove(ch)
            segment_a = tmp[0]
            # print(f"segment_a = {segment_a}")

            segments_ac.remove(segment_a)
            segment_c = segments_ac[0]
            # print(f"segment_c = {segment_c}")

            tmp = [ch for ch in digit4]
            tmp.remove(segment_b)
            tmp.remove(segment_c)
            tmp.remove(segment_f)
            segment_d = tmp[0]
            # print(f"segment_d = {segment_d}")

            segments_dg.remove(segment_d)
            segment_g = segments_dg[0]
            # print(f"segment_g = {segment_g}")

            new_0 = segment_a + segment_b + segment_c + segment_e + segment_f + segment_g
            new_1 = segment_c + segment_f
            new_2 = segment_a + segment_c + segment_d + segment_e + segment_g
            new_3 = segment_a + segment_c + segment_d + segment_f + segment_g
            new_4 = segment_b + segment_c + segment_d + segment_f
            new_5 = segment_a + segment_b + segment_d + segment_f + segment_g
            new_6 = segment_a + segment_b + segment_d + segment_e + segment_f + segment_g
            new_7 = segment_a + segment_c + segment_f
            new_8 = segment_a + segment_b + segment_c + segment_d + segment_e + segment_f + segment_g
            new_9 = segment_a + segment_b + segment_c + segment_d + segment_f + segment_g
            # print(f"{new_0} {new_1} {new_2} {new_3} {new_4} {new_5} {new_6} {new_7} {new_8} {new_9}")

            p0 = list(permutations(new_0))
            p0 = [''.join(permutation) for permutation in p0]
            p1 = list(permutations(new_1))
            p1 = [''.join(permutation) for permutation in p1]
            p2 = list(permutations(new_2))
            p2 = [''.join(permutation) for permutation in p2]
            p3 = list(permutations(new_3))
            p3 = [''.join(permutation) for permutation in p3]
            p4 = list(permutations(new_4))
            p4 = [''.join(permutation) for permutation in p4]
            p5 = list(permutations(new_5))
            p5 = [''.join(permutation) for permutation in p5]
            p6 = list(permutations(new_6))
            p6 = [''.join(permutation) for permutation in p6]
            p7 = list(permutations(new_7))
            p7 = [''.join(permutation) for permutation in p7]
            p8 = list(permutations(new_8))
            p8 = [''.join(permutation) for permutation in p8]
            p9 = list(permutations(new_9))
            p9 = [''.join(permutation) for permutation in p9]

            p_map = {0: p0, 1: p1, 2: p2, 3: p3, 4: p4, 5: p5, 6: p6, 7: p7, 8: p8, 9: p9}
            this_sum = 0
            for dd in digits:
                for k, v in p_map.items():
                    if dd in v:
                        this_sum = this_sum * 10 + k
            total_sum += this_sum

    print(f"total sum = {total_sum}")


if __name__ == '__main__':
    main()
