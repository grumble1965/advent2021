import sys


def main():
    if len(sys.argv) != 2:
        sys.exit("Please provide a file name for input data")

    filename = sys.argv[1]
    with open(filename, "r") as inputfile:
        raw = []
        for line in inputfile.readlines():
            raw.append(int(line.strip()))

    cooked = []
    for idx in range(0, len(raw)-2):
        cooked.append(raw[idx] + raw[idx+1] + raw[idx+2])

    current, last = None, None
    increased = 0
    for sum in cooked:
        current, last = sum, current
        if last is not None:
            if current > last:
                increased += 1
    print(f"total increased = {increased}")

if __name__ == '__main__':
    main()
