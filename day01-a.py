import sys


def main():
    if len(sys.argv) != 2:
        sys.exit("Please provide a file name for input data")

    filename = sys.argv[1]
    with open(filename, "r") as inputfile:

        current, last = None, None
        increase_count = 0
        for line in inputfile.readlines():
            current, last = int(line.strip()), current
            if last is None:
                pass
            else:
                if current > last:
                    increase_count += 1

        print(f"total increases is {increase_count}")


if __name__ == '__main__':
    main()
