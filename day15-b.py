import sys
import numpy as np


def print_board(board):
    """ Print the board with node costs """
    for r in board:
        print(r)


def new_tile_with_more_risk(arr):
    ones = np.ones_like(arr)
    res = np.empty_like(arr)
    res = np.add(arr, ones)
    for y in range(res.shape[0]):
        for x in range(res.shape[1]):
            while res[x, y] > 9:
                res[x, y] -= 9
    return res


def main():
    if len(sys.argv) != 2:
        sys.exit("Please provide a file name for input data")

    filename = sys.argv[1]
    with open(filename, "r") as inputfile:
        tile_tmp = []

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
            tile_tmp.append(row)
        tile = np.array(tile_tmp)
        print(tile, tile.shape)

    tile1 = new_tile_with_more_risk(tile)
    tile2 = new_tile_with_more_risk(tile1)
    tile3 = new_tile_with_more_risk(tile2)
    tile4 = new_tile_with_more_risk(tile3)
    tile5 = new_tile_with_more_risk(tile4)
    tile6 = new_tile_with_more_risk(tile5)
    tile7 = new_tile_with_more_risk(tile6)
    tile8 = new_tile_with_more_risk(tile7)

    row0 = np.concatenate((tile, tile1, tile2, tile3, tile4), axis=1)
    row1 = np.concatenate((tile1, tile2, tile3, tile4, tile5), axis=1)
    row2 = np.concatenate((tile2, tile3, tile4, tile5, tile6), axis=1)
    row3 = np.concatenate((tile3, tile4, tile5, tile6, tile7), axis=1)
    row4 = np.concatenate((tile4, tile5, tile6, tile7, tile8), axis=1)

    board = np.concatenate((row0, row1, row2, row3, row4))
    print(board, board.shape)
    row_max, col_max = board.shape

    # build q (cost array)
    q = np.zeros_like(board)
    # print(q)
    q[0, 0] = 0
    for row_iter in range(1, row_max):
        """ Starting at top left of board, move down a row at a time.
            From there, move up and right diagonally to top row. """
        x, y = 0, row_iter
        while x < col_max and y >= 0:
            # print(f"{(x,y)}")
            m1 = q[y, x-1] if x > 0 else 999999
            m2 = q[y-1, x] if y > 0 else 999999
            if m1 == 0 or m2 == 0:
                print(f"{x,y} touches 0-cost node")
            m = min([m1, m2])
            q[y, x] = m + board[y, x]
            x += 1
            y -= 1
    for col_iter in range(1, col_max):
        """ Starting at bottom left of board, move right a column at a time.
            From there, move up and right diagonally to last column. """
        # print(i)
        x, y = col_iter, row_max - 1
        while x < col_max and y >= 0:
            # print(f"{(x,y)}")
            m1 = q[y, x-1] if x > 0 else 999999
            m2 = q[y-1, x] if y > 0 else 999999
            if m1 == 0 or m2 == 0:
                print(f"{x,y} touches 0-cost node")
            m = min([m1, m2])
            q[y, x] = m + board[y, x]
            x += 1
            y -= 1
    print(q)


if __name__ == '__main__':
    main()
