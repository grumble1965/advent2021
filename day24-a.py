import itertools
import sys
import math
from itertools import permutations


def get_register_value(registers, src):
    (w, x, y, z) = registers
    result = None
    if src == 'w':
        result = w
    elif src == 'x':
        result = x
    elif src == 'y':
        result = y
    elif src == 'z':
        result = z
    else:
        print(f"Unknown register {src}")
    return result


def get_register_or_int_value(registers, src):
    if src in ['w', 'x', 'y', 'z']:
        return get_register_value(registers, src)
    else:
        return int(src)


def write_register(registers, dest, val):
    (w, x, y, z) = registers
    if dest == 'w':
        w = val
    elif dest == 'x':
        x = val
    elif dest == 'y':
        y = val
    elif dest == 'z':
        z = val
    else:
        print(f"Unknown register {dest}")
    return w, x, y, z


def alu(code, registers, inputs):
    (w, x, y, z) = registers
    for inst in code:
        opcode = inst[0]
        operands = inst[1:]
        # print(f"{inst} = {opcode} {operands}")
        if opcode == 'inp':
            source_val = inputs.pop(0)
            (w, x, y, z) = write_register((w, x, y, z), operands[0], source_val)
        elif opcode == 'add':
            source1 = int(get_register_value((w, x, y, z), operands[0]))
            source2 = int(get_register_or_int_value((w, x, y, z), operands[1]))
            result = int(source1 + source2)
            (w, x, y, z) = write_register((w, x, y, z), operands[0], result)
        elif opcode == 'mul':
            source1 = int(get_register_value((w, x, y, z), operands[0]))
            source2 = int(get_register_or_int_value((w, x, y, z), operands[1]))
            result = int(source1 * source2)
            (w, x, y, z) = write_register((w, x, y, z), operands[0], result)
        elif opcode == 'div':
            source1 = int(get_register_value((w, x, y, z), operands[0]))
            source2 = int(get_register_or_int_value((w, x, y, z), operands[1]))
            result = int(source1 / source2)
            (w, x, y, z) = write_register((w, x, y, z), operands[0], result)
        elif opcode == 'mod':
            source1 = int(get_register_value((w, x, y, z), operands[0]))
            source2 = int(get_register_or_int_value((w, x, y, z), operands[1]))
            result = int(source1 % source2)
            (w, x, y, z) = write_register((w, x, y, z), operands[0], result)
        elif opcode == 'eql':
            source1 = int(get_register_value((w, x, y, z), operands[0]))
            source2 = int(get_register_or_int_value((w, x, y, z), operands[1]))
            result = 1 if source1 == source2 else 0
            (w, x, y, z) = write_register((w, x, y, z), operands[0], result)
        else:
            print(f"Unknown opcode {opcode}")
    registers = (w, x, y, z)
    return registers, inputs


def main():
    if len(sys.argv) != 2:
        sys.exit("Please provide a file name for input data")

    code = []
    filename = sys.argv[1]
    with open(filename, "r") as inputfile:
        while True:
            line = inputfile.readline()
            if not line:
                break
            tmp = line.strip()
            # print(tmp)
            words = tmp.split()
            code.append(words)

    segments = [idx for idx in range(len(code)) if code[idx] == ['inp', 'w']]
    chunk = []
    for idx in range(len(segments)):
        if idx + 1 == len(segments):
            # print(f"i{idx+1} = code[{segments[idx]}:]")
            chunk.append(code[segments[idx]:])
        else:
            # print(f"i{idx+1} = code[{segments[idx]}:{segments[idx+1]}]")
            chunk.append(code[segments[idx]:segments[idx+1]])

    # print(code)
    # registers = (0, 0, 0, 0)
    # inputs = [1, 3, 5, 7, 9, 2, 4, 6, 8, 9, 9, 9, 9, 9]
    # (registers, inputs) = alu(code, registers, inputs)
    # print(f"Result: {registers}  {inputs}")

    # p = itertools.product([9, 8, 7, 6, 5, 4, 3, 2, 1], repeat=14)
    # for pp in p:
    #     registers = (0, 0, 0, 0)
    #     inputs = list(pp)
    #     # print(f"Trying input {inputs}")
    #     (registers, inputs) = alu(code.copy(), registers, inputs)
    #     w, x, y, z = registers
    #     if z == 0:
    #         print(f"{list(pp)} worked")
    #         break

    z_search_range = 1000

    # i14_goals = []
    # i14_end_state = [0]
    # for i14 in range(1, 10):
    #     for z in range(z_search_range):
    #         registers_in = (0, 0, 0, z)
    #         inputs = [i14]
    #         # print(f"Trying input {inputs} {registers}")
    #         (registers_out, inputs) = alu(chunk[13].copy(), registers_in, inputs.copy())
    #         w1, x1, y1, z1 = registers_out
    #         if z1 in i14_end_state:
    #             # print(i14, registers_in, registers_out)
    #             tt = (i14, z)
    #             i14_goals.append(tt)
    # print(f"i14 goals: ({len(i14_goals)}) {i14_goals}")
    #
    # i13_goals = []
    # i13_end_state = [z for i14,z in i14_goals]
    # for i13 in range(1, 10):
    #     for z in range(z_search_range):
    #         registers_in = (0, 0, 0, z)
    #         inputs = [i13]
    #         # print(f"Trying input {inputs} {registers}")
    #         (registers_out, inputs) = alu(chunk[12].copy(), registers_in, inputs.copy())
    #         w1, x1, y1, z1 = registers_out
    #         if z1 in i13_end_state:
    #             # print(i13, registers_in, registers_out)
    #             tt = (i13, z)
    #             i13_goals.append(tt)
    # print(f"i13 goals: ({len(i13_goals)}) {i13_goals}")
    #
    # i12_goals = []
    # i12_end_state = []
    # for i13, z in i13_goals:
    #     i12_end_state.append(z)
    # for i12 in range(1, 10):
    #     for z in range(z_search_range):
    #         registers_in = (0, 0, 0, z)
    #         inputs = [i12]
    #         # print(f"Trying input {inputs} {registers}")
    #         (registers_out, inputs) = alu(chunk[11].copy(), registers_in, inputs.copy())
    #         w1, x1, y1, z1 = registers_out
    #         if z1 in i12_end_state:
    #             # print(i12, registers_in, registers_out)
    #             tt = (i12, z)
    #             i12_goals.append(tt)
    # print(f"i12 goals: ({len(i12_goals)}) {i12_goals}")

    # i13i14_goals = []
    # i13i14_end_state = [0]
    # for i13 in range(1, 10):
    #     for i14 in range(1, 10):
    #         for z in range(10 ** int(math.log10(len(i13i14_end_state))+3)):
    #             registers_in = (0, 0, 0, z)
    #             inputs = [i13, i14]
    #             # print(f"Trying input {inputs} {registers}")
    #             (registers_inner, inputs_inner) = alu(chunk[12].copy(), registers_in, inputs.copy())
    #             (registers_out, inputs) = alu(chunk[13].copy(), registers_inner, inputs_inner)
    #             w1, x1, y1, z1 = registers_out
    #             if z1 in i13i14_end_state:
    #                 # print(i14, registers_in, registers_out)
    #                 tt = (i13, i14, z)
    #                 i13i14_goals.append(tt)
    # print(f"i13i14 goals: ({len(i13i14_goals)}) {i13i14_goals}")
    #
    # i11i12_goals = []
    # i11i12_end_state = [z for i13, i14, z in i13i14_goals]
    # for i11 in range(1, 10):
    #     for i12 in range(1, 10):
    #         for z in range(10 ** int(math.log10(len(i11i12_end_state))+2)):
    #             registers_in = (0, 0, 0, z)
    #             inputs = [i11, i12]
    #             # print(f"Trying input {inputs} {registers}")
    #             (registers_inner, inputs_inner) = alu(chunk[10].copy(), registers_in, inputs.copy())
    #             (registers_out, inputs) = alu(chunk[11].copy(), registers_inner, inputs_inner)
    #             w1, x1, y1, z1 = registers_out
    #             if z1 in i11i12_end_state:
    #                 # print(i14, registers_in, registers_out)
    #                 tt = (i11, i12, z)
    #                 i11i12_goals.append(tt)
    # print(f"i11i12 goals: ({len(i11i12_goals)}) {i11i12_goals}")
    #
    # i9i10_goals = []
    # i9i10_end_state = [z for i11, i12, z in i11i12_goals]
    # for i9 in range(1, 10):
    #     for i10 in range(1, 10):
    #         for z in range(10 ** int(math.log10(len(i9i10_end_state))+2)):
    #             registers_in = (0, 0, 0, z)
    #             inputs = [i9, i10]
    #             # print(f"Trying input {inputs} {registers}")
    #             (registers_inner, inputs_inner) = alu(chunk[8].copy(), registers_in, inputs.copy())
    #             (registers_out, inputs) = alu(chunk[9].copy(), registers_inner, inputs_inner)
    #             w1, x1, y1, z1 = registers_out
    #             if z1 in i9i10_end_state:
    #                 # print(i14, registers_in, registers_out)
    #                 tt = (i9, i10, z)
    #                 i9i10_goals.append(tt)
    # print(f"i9i10 goals: ({len(i9i10_goals)}) {i9i10_goals}")

    forward_1_5_results = {}
    for pp in itertools.product(range(10), repeat=5):
        (i1, i2, i3, i4, i5) = pp
        registers_in = (0, 0, 0, 0)
        inputs = [i1, i2, i3, i4, i5]
        (reg_1, in_1) = alu(chunk[0].copy(), registers_in, inputs.copy())
        (reg_2, in_2) = alu(chunk[1].copy(), reg_1, in_1)
        (reg_3, in_3) = alu(chunk[2].copy(), reg_2, in_2)
        (reg_4, in_4) = alu(chunk[3].copy(), reg_3, in_3)
        (reg_5, in_5) = alu(chunk[4].copy(), reg_4, in_4)
        w5, x5, y5, z5 = reg_5
        if z5 in forward_1_5_results:
            o1, o2, o3, o4, o5 = forward_1_5_results[z5]
            oo = o1*10000 + o2*1000 + o3*100 * o4*10 + o5
            ii = i1*10000 + i2*1000 + i3*100 * i4*10 + i5
            if ii > oo:
                forward_1_5_results[z5] = (i1, i2, i3, i4, i5)
        else:
            forward_1_5_results[z5] = (i1, i2, i3, i4, i5)
    z_values = set()
    z_values.update(forward_1_5_results.keys())
    print(f"z1-5 min = {min(z_values)} max = {max(z_values)} total = {len(z_values)}")

    forward_6_10_results = {}
    for z5, i1_i5 in forward_1_5_results.items():
        (i1, i2, i3, i4, i5) = i1_i5
        for pp in itertools.product(range(10), repeat=5):
            (i6, i7, i8, i9, i10) = pp
            registers_in = (0, 0, 0, z5)
            inputs = [i6, i7, i8, i9, i10]
            (reg_6, in_6) = alu(chunk[5].copy(), registers_in, inputs.copy())
            (reg_7, in_7) = alu(chunk[6].copy(), reg_6, in_6)
            (reg_8, in_8) = alu(chunk[7].copy(), reg_7, in_7)
            (reg_9, in_9) = alu(chunk[8].copy(), reg_8, in_8)
            (reg_10, in_10) = alu(chunk[9].copy(), reg_9, in_9)
            w10, x10, y10, z10 = reg_10
        if z10 in forward_6_10_results:
            o1, o2, o3, o4, o5, o6, o7, o8, o9, o10 = forward_6_10_results[z10]
            oo = o1*1000000000 + o2*100000000 + o3*10000000 + o4*1000000 + o5*100000 + o6*10000 + o7*1000 * o8*100 + o9*10 + o10
            ii = i1*1000000000 + i2*100000000 + i3*10000000 + i4*1000000 + i5*100000 + i6*10000 + i7*1000 * i8*100 + i9*10 + i10
            if ii > oo:
                forward_6_10_results[z10] = (i1, i2, i3, i4, i5, i6, i7, i8, i9, i10)
        else:
            forward_6_10_results[z10] = (i1, i2, i3, i4, i5, i6, i7, i8, i9, i10)
    z_values = set()
    z_values.update(forward_6_10_results.values())
    print(f"z6-10 min = {min(z_values)} max = {max(z_values)} total = {len(z_values)}")

    forward_results = {}
    for pp in itertools.product(range(10), repeat=4):
        (i11, i12, i13, i14) = pp
        registers_in = (0, 0, 0, 0)
        inputs = [i11, i12, i13, i14]
        (reg_11, in_11) = alu(chunk[10].copy(), registers_in, inputs.copy())
        (reg_12, in_12) = alu(chunk[11].copy(), reg_11, in_11)
        (reg_13, in_13) = alu(chunk[12].copy(), reg_12, in_12)
        (reg_14, in_14) = alu(chunk[13].copy(), reg_13, in_13)
        w14, x14, y14, z14 = reg_14
        forward_results[pp] = z14
    z_values = set()
    z_values.update(forward_results.values())
    print(f"z11-14 min = {min(z_values)} max = {max(z_values)} total = {len(z_values)}")



if __name__ == '__main__':
    main()
