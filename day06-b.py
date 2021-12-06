import sys


def main():
    if len(sys.argv) != 2:
        sys.exit("Please provide a file name for input data")

    ages = []
    filename = sys.argv[1]
    with open(filename, "r") as inputfile:
        ages_str = inputfile.readline().strip().split(',')
        ages_list = [int(a) for a in ages_str]

    ages = (ages_list.count(0),
            ages_list.count(1),
            ages_list.count(2),
            ages_list.count(3),
            ages_list.count(4),
            ages_list.count(5),
            ages_list.count(6),
            ages_list.count(7),
            ages_list.count(8))

    day = 0
    print(f"initial state: {ages}")
    while day < 256:
        day += 1
        (a0, a1, a2, a3, a4, a5, a6, a7, a8) = ages
        ages = (a1, a2, a3, a4, a5, a6, a7+a0, a8, a0)

        (a0, a1, a2, a3, a4, a5, a6, a7, a8) = ages
        pop = a0 + a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8

        print(f"after {day} days: {pop} - {ages}")

    (a0, a1, a2, a3, a4, a5, a6, a7, a8) = ages
    pop = a0 + a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8


if __name__ == '__main__':
    main()
