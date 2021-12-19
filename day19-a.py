import sys
import numpy as np


def main():
    if len(sys.argv) != 2:
        sys.exit("Please provide a file name for input data")

    filename = sys.argv[1]
    with open(filename, "r") as inputfile:

        scanners = []
        mode = 0
        beacon_data = None

        while True:
            line = inputfile.readline()
            if not line:
                break
            tmp = line.strip()

            if mode == 0:
                # look for scanner banner
                if tmp.startswith('--- scanner '):
                    scanner_number = tmp.split(' ')[2]
                    # print(f"scanner {scanner_number}")
                    mode = 1
                    beacon_data = []
            elif mode == 1:
                # read beacon data
                if tmp == '':
                    arr = np.array(beacon_data)
                    scanners.append(arr)
                    mode = 0
                else:
                    data = tmp.split(',')
                    data_tuple = int(data[0]), int(data[1]), int(data[2])
                    beacon_data.append(data_tuple)
            else:
                print(f"??? {tmp}")
    # clean up last beacon
    arr = np.array(beacon_data)
    scanners.append(arr)

    # print(f"{len(scanners)} scanners: {scanners}")

    # align scanner 1 with scanner 0
    alignment_metrics = {}
    base_set = set()
    s0_points = scanners[0]
    for p in s0_points:
        x, y, z = p
        base_set.add((x, y, z))
    # print(base_set)

    s1_points = scanners[1]
    for s0x, s0y, s0z in s0_points:
        for s1x, s1y, s1z in s1_points:
            xo = s0x - s1x
            yo = s0y - s1y
            zo = s0z - s1z
            # print(f"Trying {xo},{yo}")
            s1_set = base_set.copy()
            for p in s1_points:
                x, y, z = p
                s1_set.add((x + xo, y + yo, z + zo))
            # print(s1_map)
            overlap = len(s1_set)
            alignment_metrics[(xo, yo, zo)] = overlap
    # print(f"{alignment_metrics}")

    best_alignment, best_offset = None, (None, None)
    for offset, result in alignment_metrics.items():
        if best_alignment is None:
            best_offset, best_alignment = offset, result
        elif result < best_alignment:
            best_offset, best_alignment = offset, result
    print(f"Scanner 1 with Scanner 0 aligns best @ {best_offset} = {best_alignment}")


if __name__ == '__main__':
    main()
