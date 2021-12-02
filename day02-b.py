import sys


def main():
    if len(sys.argv) != 2:
        sys.exit("Please provide a file name for input data")

    filename = sys.argv[1]
    with open(filename, "r") as inputfile:
        horizontal, depth, aim = 0, 0, 0

        for line in inputfile.readlines():
            command_str, distance_str = line.strip().split()
            distance = int(distance_str)
            print(f"{command_str} {distance}")
            if command_str == 'forward':
                horizontal += int(distance)
                depth += aim * int(distance)
            elif command_str == 'down':
                aim += int(distance)
            elif command_str == 'up':
                aim -= int(distance)

        print(f"{horizontal} {depth} -> {horizontal * depth}")


if __name__ == '__main__':
    main()
