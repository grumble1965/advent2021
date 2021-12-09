import sys


def main():
    if len(sys.argv) != 2:
        sys.exit("Please provide a file name for input data")

    height_map = []
    filename = sys.argv[1]
    with open(filename, "r") as inputfile:
        while True:
            line = inputfile.readline()
            if not line:
                break
            tmp = line.strip()
            height_map.append([int(i) for i in tmp])
    # print(f"{height_map}")

    min_x, min_y = 0, 0
    max_x, max_y = len(height_map[0]) - 1, len(height_map) - 1
    low_points = []
    for y in range(min_y, max_y+1):
        for x in range(min_x, max_x+1):
            lower_than_above = (y <= min_y) or height_map[y-1][x] > height_map[y][x]
            lower_than_below = (y >= max_y) or height_map[y+1][x] > height_map[y][x]
            lower_than_left = (x <= min_x) or height_map[y][x-1] > height_map[y][x]
            lower_than_right = (x >= max_x) or height_map[y][x+1] > height_map[y][x]
            if lower_than_above and lower_than_below and lower_than_left and lower_than_right:
                ttt = (x, y)
                low_points.append(ttt)
    # print(f"{low_points}")

    risk_level = 0
    for (x, y) in low_points:
        risk_level += height_map[y][x] + 1
    print(f"Risk level = {risk_level}")


if __name__ == '__main__':
    main()
