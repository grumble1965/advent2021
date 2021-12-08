import sys

def main():
    if len(sys.argv) != 2:
        sys.exit("Please provide a file name for input data")

    sum1478 = 0
    filename = sys.argv[1]
    with open(filename, "r") as inputfile:
        while True:
            line = inputfile.readline()
            if not line:
                break

            display = line.strip().split()
            patterns = display[0:10]
            digits = display[11:]

            sum1, sum4, sum7, sum8 = 0, 0, 0, 0
            for dd in digits:
                if len(dd) == 2:
                    sum1 += 1
                elif len(dd) == 4:
                    sum4 += 1
                elif len(dd) == 3:
                    sum7 += 1
                elif len(dd) == 7:
                    sum8 += 1
            sum1478 += (sum1 + sum4 + sum7 + sum8)

    print(f"sum = {sum1478}")


if __name__ == '__main__':
    main()
