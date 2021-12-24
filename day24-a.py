import itertools
import sys
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

    # for i14 in range(1, 10):
    #     for z in range(10000):
    #         registers_in = (0, 0, 0, z)
    #         inputs = [i14]
    #         # print(f"Trying input {inputs} {registers}")
    #         (registers_out, inputs) = alu(code.copy(), registers_in, inputs.copy())
    #         w1, x1, y1, z1 = registers_out
    #         if z1 == 0:
    #             print(i14, registers_in, registers_out)

    for i13 in range(1, 10):
        for z in range(10000):
            registers_in = (0, 0, 0, z)
            inputs = [i13]
            # print(f"Trying input {inputs} {registers}")
            (registers_out, inputs) = alu(code.copy(), registers_in, inputs.copy())
            w1, x1, y1, z1 = registers_out
            if z1 in range(13, 22):
                print(i13, registers_in, registers_out)



if __name__ == '__main__':
    main()
