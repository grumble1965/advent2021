import sys


def main():
    if len(sys.argv) != 2:
        sys.exit("Please provide a file name for input data")

    filename = sys.argv[1]
    with open(filename, "r") as inputfile:

        counters, starting = [], True
        for line in inputfile.readlines():
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

        print(f"{counters}")
        gamma, epsilon = 0, 0
        for idx in range(len(counters)):
            if counters[idx] > 0:
                gamma = gamma * 2 + 1
                epsilon = epsilon * 2 + 0
            elif counters[idx] < 0:
                gamma = gamma * 2 + 0
                epsilon = epsilon * 2 + 1
        print(f"gamma = {gamma}  epsilon = {epsilon}  power = {gamma*epsilon}")

if __name__ == '__main__':
    main()
