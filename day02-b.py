import sys


def main():
    if len(sys.argv) != 2:
        sys.exit("Please provide a file name for input data")

    filename = sys.argv[1]
    with open(filename, "r") as inputfile:
        horizontal, depth, aim = 0, 0, 0

        for line in inputfile.readlines():
            command, distance = line.strip().split()
            print(f"{command} {distance}")
            if command == 'forward':
                horizontal += int(distance)
                depth += aim * int(distance)
            elif command == 'down':
                aim += int(distance)
            elif command == 'up':
                aim -= int(distance)

        print(f"{horizontal} {depth} -> {horizontal * depth}")


if __name__ == '__main__':
    main()
