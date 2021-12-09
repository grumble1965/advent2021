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
    # print(f"{risk_level}")

    basins = []
    for lp in low_points:
        # print(f"lp = {lp}")
        basin_area = 0
        Q = [lp]
        Seen = []
        while len(Q) > 0:
            # print(f"Q = {Q}")
            (x, y) = Q.pop()
            if not height_map[y][x] == 9 and (x, y) not in Seen:
                basin_area += 1
                Seen.append( (x, y) )
                # add west
                if x > min_x:
                    Q.append((x-1, y))
                # add east
                if x < max_x:
                    Q.append((x+1, y))
                # add north
                if y > min_y:
                    Q.append((x, y-1))
                # add south
                if y < max_y:
                    Q.append((x, y+1))
        # print(f"basin at {lp} has area {basin_area}")
        basins.append(basin_area)

    basins.sort(reverse=True)
    print(f"Product = {basins[0] * basins[1] * basins[2]}")


if __name__ == '__main__':
    main()
