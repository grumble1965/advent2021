import sys


def board_has_bingo(b):
    r1 = b[0] == -1 and b[1] == -1 and b[2] == -1 and b[3] == -1 and b[4] == -1
    r2 = b[5] == -1 and b[6] == -1 and b[7] == -1 and b[8] == -1 and b[9] == -1
    r3 = b[10] == -1 and b[11] == -1 and b[12] == -1 and b[13] == -1 and b[14] == -1
    r4 = b[15] == -1 and b[16] == -1 and b[17] == -1 and b[18] == -1 and b[19] == -1
    r5 = b[20] == -1 and b[21] == -1 and b[22] == -1 and b[23] == -1 and b[24] == -1
    c1 = b[0] == -1 and b[5] == -1 and b[10] == -1 and b[15] == -1 and b[20] == -1
    c2 = b[1] == -1 and b[6] == -1 and b[11] == -1 and b[16] == -1 and b[21] == -1
    c3 = b[2] == -1 and b[7] == -1 and b[12] == -1 and b[17] == -1 and b[22] == -1
    c4 = b[3] == -1 and b[8] == -1 and b[13] == -1 and b[18] == -1 and b[23] == -1
    c5 = b[4] == -1 and b[9] == -1 and b[14] == -1 and b[19] == -1 and b[24] == -1
    return r1 or r2 or r3 or r4 or r5 or c1 or c2 or c3 or c4 or c5


def main():
    if len(sys.argv) != 2:
        sys.exit("Please provide a file name for input data")

    filename = sys.argv[1]
    with open(filename, "r") as inputfile:
        calls = [int(i) for i in inputfile.readline().split(',')]
        num_boards = 0
        boards = []
        while True:
            line = inputfile.readline()
            if not line:
                break
            line1 = inputfile.readline().split()
            line2 = inputfile.readline().split()
            line3 = inputfile.readline().split()
            line4 = inputfile.readline().split()
            line5 = inputfile.readline().split()
            boards.append([int(i) for i in line1 + line2 + line3 + line4 + line5])
            num_boards += 1

    # print(f"Balls called: {calls}\n")
    # for bb in boards:
    #     print(f"{bb}")

    winners = []
    ball = None
    while len(calls) > 0 and len(winners) == 0:
        # draw a ball
        ball = calls.pop(0)

        # mark all boards in play
        for bb_idx in range(len(boards)):
            if bb_idx not in winners:
                bb = boards[bb_idx]
                if ball in bb:
                    # replace with -1,
                    idx = bb.index(ball)
                    boards[bb_idx][idx] = -1
                    bb[idx] = -1

        # check all boards in play for bingos
        for bb_idx in range(len(boards)):
            if bb_idx not in winners:
                bb = boards[bb_idx]
                if board_has_bingo(bb):
                    winners.append(bb_idx)

    board_sum = 0
    for num in boards[winners[0]]:
        board_sum += (num if num >= 0 else 0)
    print(f"final score = {board_sum} * {ball} = {board_sum * ball}")


if __name__ == '__main__':
    main()
