import sys
import numpy as np

def main():
    if len(sys.argv) != 2:
        sys.exit("Please provide a file name for input data")

    floor = []
    filename = sys.argv[1]
    with open(filename, "r") as inputfile:
        while True:
            line = inputfile.readline()
            if not line:
                break
            tmp = line.strip()
            #print(tmp)
            line = [ch for ch in tmp]
            floor.append(line)
    # print(f"{floor}")

    arr = np.array(floor)
    print(arr)

    step = 0
    while True:
        step += 1
        moved_east, moved_south = crab_step(arr)
        if moved_east == 0 and moved_south == 0:
            break
        else:
            pass
            # print(arr)

    print(f"Crabs stopped after {step} steps")


def crab_step(arr):
    can_move_east = set()
    next_east = set()
    for r in range(arr.shape[0]):
        for c in range(arr.shape[1]):
            if c + 1 < arr.shape[1]:
                next_col = c + 1
            else:
                next_col = 0
            if arr[r, c] == '>' and arr[r, next_col] == '.':
                can_move_east.add((r, c))
                next_east.add((r, next_col))
    for r, c in can_move_east:
        arr[r, c] = '.'
    for r, c in next_east:
        arr[r, c] = '>'
    # print(f"moved {len(next_east)} east")
    # move south
    can_move_south = set()
    next_south = set()
    for r in range(arr.shape[0]):
        for c in range(arr.shape[1]):
            if r + 1 < arr.shape[0]:
                next_row = r + 1
            else:
                next_row = 0
            if arr[r, c] == 'v' and arr[next_row, c] == '.':
                can_move_south.add((r, c))
                next_south.add((next_row, c))
    for r, c in can_move_south:
        arr[r, c] = '.'
    for r, c in next_south:
        arr[r, c] = 'v'
    return len(next_east), len(next_south)


if __name__ == '__main__':
    main()
