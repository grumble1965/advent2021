import sys
import numpy as np


def print_board(board):
    """ Print the board with node costs """
    for r in board:
        print(r)


def main():
    if len(sys.argv) != 2:
        sys.exit("Please provide a file name for input data")

    start = None
    finish = None
    board = None

    filename = sys.argv[1]
    with open(filename, "r") as inputfile:
        board_tmp = []

        while True:
            line = inputfile.readline()
            if not line:
                break
            tmp = line.strip()
            # print(f"{tmp}")

            row = []
            for ch in tmp:
                if ch.isdigit():
                    row.append(int(ch))
            board_tmp.append(row)
        board = np.array(board_tmp)

    print(board)
    start = (0, 0)
    finish = board.shape

    # build q (cost array)
    q = np.zeros(finish)
    # print(q)
    q[0, 0] = 0
    for i in range(1, finish[0]):
        x, y = 0, i
        while x < finish[0] and y >= 0:
            # print(f"{(x,y)}")
            m1 = q[x-1, y] if x > 0 else 1e999
            m2 = q[x, y-1] if y > 0 else 1e999
            if m1 == 0 or m2 == 0:
                print(f"{x,y} fucked")
            m = min([m1, m2])
            q[x, y] = m + board[x, y]
            x += 1
            y -= 1
    for i in range(finish[0], 1, -1):
        # print(i)
        x, y = finish[0] + 1 - i, finish[0] - 1
        while x < finish[0] and y >= 0:
            # print(f"{(x,y)}")
            m1 = q[x-1, y] if x > 0 else 1e999
            m2 = q[x, y-1] if y > 0 else 1e999
            if m1 == 0 or m2 == 0:
                print(f"{x,y} fucked")
            m = min([m1, m2])
            q[x, y] = m + board[x, y]
            x += 1
            y -= 1
    print(q)




if __name__ == '__main__':
    main()
