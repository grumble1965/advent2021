import sys
from queue import LifoQueue


def print_board(board):
    for row in board:
        print(row)


def valid_point(board, y, x):
    return y in range(len(board)) and x in range(len(board[0]))


def main():
    if len(sys.argv) != 2:
        sys.exit("Please provide a file name for input data")

    board = []
    filename = sys.argv[1]
    with open(filename, "r") as inputfile:
        while True:
            line = inputfile.readline()
            if not line:
                break
            tmp = line.strip()
            tt = [int(ch) for ch in tmp ]
            board.append(tt)
    # print(f"{board}")

    step, limit = 0, 100
    flashes = 0
    print_board(board)
    while step < limit:
        # bump all, record flashes
        # print(f"step {step}")
        flash_me = []
        for y in range(len(board)):
            for x in range(len(board[y])):
                board[y][x] += 1
                if board[y][x] > 9:
                    if (x,y) not in flash_me:
                        flash_me.append((x, y))
        # print(f"flashes-> {flash_me}")

        flashed = []
        while len(flash_me) > 0:
            for (x, y) in flash_me:
                board[y][x] = 0
                flashes += 1
                flashed.append((x, y))

                for (dx,dy) in [(-1,-1), (0,-1), (1,-1), (-1,0), (1,0), (-1,1), (0,1), (1,1)]:
                    nx, ny = x + dx, y + dy
                    if valid_point(board, ny, nx) and (nx, ny) not in flashed:
                        board[ny][nx] += 1

            flash_me = []
            for y in range(len(board)):
                for x in range(len(board[y])):
                    if board[y][x] > 9:
                        if (x, y) not in flash_me and (x, y) not in flashed:
                            flash_me.append((x, y))

        step += 1
        # print_board(board)

    print(f"After {limit} steps, total flashes = {flashes}")


if __name__ == '__main__':
    main()
