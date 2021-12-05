import sys


def printmap(map):
    for row in map:
        print(f"{row}")
    print()


def main():
    if len(sys.argv) != 2:
        sys.exit("Please provide a file name for input data")

    filename = sys.argv[1]
    thermal_lines = []
    maxX = -99999
    maxY = -99999
    with open(filename, "r") as inputfile:
        while True:
            line = inputfile.readline().strip()
            if not line:
                break
            p1r, p2r = line.split('->')
            xStr, yStr = p1r.split(',')
            x, y = int(xStr), int(yStr)
            if x > maxX:
                maxX = x
            if y > maxY:
                maxY = y
            p1 = (int(x), int(y))
            xStr, yStr = p2r.split(',')
            x, y = int(xStr), int(yStr)
            if x > maxX:
                maxX = x
            if y > maxY:
                maxY = y
            p2 = (int(x), int(y))
            thermal_lines.append( (p1, p2) )
    # print(thermal_lines)

    # initialize the map
    map = [[0 for x in range(maxX+1)] for y in range(maxY+1)]
    # printmap(map)

    # mark horizontal lines
    for ll in thermal_lines:
        (p1, p2) = ll
        if p1[1] == p2[1]:
            y = p1[1]
            start = p1[0] if p1[0] < p2[0] else p2[0]
            end = p2[0] if p2[0] > p1[0] else p1[0]
            for x in range(start, end+1):
                map[y][x] += 1
            # print(p1, ' -> ', p2)
            # printmap(map)
        elif p1[0] == p2[0]:
            x = p1[0]
            start = p1[1] if p1[1] < p2[1] else p2[1]
            end = p2[1] if p2[1] > p1[1] else p1[1]
            for y in range(start, end+1):
                map[y][x] += 1
            # print(p1, ' -> ', p2)
            # printmap(map)
        else:
            if p1[0] < p2[0]:
                p_left, p_right = p1, p2
            else:
                p_left, p_right = p2, p1
            if p_left[1] < p_right[1]:
                y_delta = 1
            else:
                y_delta = -1
            x, y = p_left[0], p_left[1]
            while x <= p_right[0]:
                map[y][x] += 1
                x, y = x+1, y+y_delta

    # compute output
    count = 0
    for r in map:
        for c in r:
            if c > 1:
                count += 1

    print(f"{count}")


if __name__ == '__main__':
    main()
