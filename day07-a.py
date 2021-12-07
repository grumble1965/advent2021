import sys

def main():
    if len(sys.argv) != 2:
        sys.exit("Please provide a file name for input data")

    filename = sys.argv[1]
    with open(filename, "r") as inputfile:
        crabs_str = inputfile.readline().strip().split(',')
        crabs_int = [int(s) for s in crabs_str]

    left, right = 99999, -99999
    for i in crabs_int:
        if left > i:
            left = i
        if right < i:
            right = i
    print(f"crabs range from {left} to {right}")

    crabs = {}
    for idx in range(left, right+1):
        crabs[idx] = 0
    for i in crabs_int:
        crabs[i] += 1
    print(f"{crabs}")

    fuel_costs = {}
    for idx in range(left, right+1):
        sum = 0
        for i,c in crabs.items():
            sum += (c * abs(i - idx))
        fuel_costs[idx] = sum
    print(f"{fuel_costs}")

    min_idx, min_fuel = None, 1e99
    for i,f in fuel_costs.items():
        if f < min_fuel:
            min_idx, min_fuel = i, f
    print(f"final location is {min_idx} costing {min_fuel}")


if __name__ == '__main__':
    main()
