import sys


def add_horizontal_line(a, b):
    c = ''
    for i in range(len(a)):
        if a[i] == '#' or b[i] == '#':
            ch = '#'
        else:
            ch = '.'
        c += ch
    return c


def main():
    if len(sys.argv) != 2:
        sys.exit("Please provide a file name for input data")

    dots = set()
    folds = []
    filename = sys.argv[1]
    with open(filename, "r") as inputfile:
        while True:
            line = inputfile.readline()
            if not line:
                break
            tmp = line.strip()
            # print(f"{tmp}")
            if tmp.count(',') > 0:
                (x,y) = tmp.split(',')
                dots.add((int(x), int(y)))
            elif tmp.count('=') > 0:
                _, _, symmetry = tmp.split(' ')
                axis, val = symmetry.split('=')
                folds.append((axis, int(val)))
    # print(dots)
    # print(folds)

    x_max, y_max = -1, -1
    for (x, y) in dots:
        if x > x_max:
            x_max = x
        if y > y_max:
            y_max = y
    # print(f"(0,0) to ({x_max},{y_max})")

    board = []
    for y in range(y_max+1):
        line = []
        for x in range(x_max+1):
            line.append('.')
        for x in [dx for (dx, dy) in dots if dy == y]:
            line[x] = '#'
        # print(line)
        board.append("".join(line))
    # for ll in board:
    #     print(ll)

    for (axis, fold_line) in folds:
        print(f"fold {axis} = {fold_line}")
        if axis == 'y':
            new_board = board[0:fold_line]
            for y in range(fold_line+1, len(board)):
                y_dest = fold_line - (y - fold_line)
                if y_dest >= 0:
                    c = add_horizontal_line(new_board[y_dest], board[y])
                    new_board[y_dest] = c
            y_max = fold_line
        elif axis == 'x':
            new_board = []
            for line in board:
                # print(f"{line[0:fold_line]} | {line[fold_line+1:]}")
                tmp = ''
                for ch in line[fold_line+1:]:
                    tmp = ch + tmp
                c = add_horizontal_line(line[0:fold_line], tmp)
                new_board.append(c)
            x_max = fold_line
        else:
            print(f"unknown axis {axis}")
        dot_count = 0
        for ll in new_board:
            # print(ll)
            dot_count += ll.count('#')
        # print(f"dot count = {dot_count}")
        board = new_board
        # break


    for ll in board:
        print(ll)


if __name__ == '__main__':
    main()
