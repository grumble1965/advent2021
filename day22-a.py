import sys
import numpy as np

def main():
    if len(sys.argv) != 2:
        sys.exit("Please provide a file name for input data")

    reboot_steps = []

    filename = sys.argv[1]
    with open(filename, "r") as inputfile:
        while True:
            line = inputfile.readline()
            if not line:
                break
            tmp = line.strip()
            # print(tmp)
            words = tmp.split(',')
            direction, xrange = words[0].split()
            [xlow, xhigh] = xrange.split('=')[1].split('..')
            yrange = words[1]
            [ylow, yhigh] = yrange.split('=')[1].split('..')
            zrange = words[2]
            [zlow, zhigh] = zrange.split('=')[1].split('..')
            print(f"{direction} ({xlow}..{xhigh}) ({ylow}..{yhigh}) ({zlow}..{zhigh})")
            step_tuple = (
                0 if direction == 'off' else 1,
                (int(xlow), int(xhigh)),
                (int(ylow), int(yhigh)),
                (int(zlow), int(zhigh))
            )
            reboot_steps.append(step_tuple)

    # init reactor
    reactor = {}
    for x in range(-50, 51):
        for y in range(-50, 51):
            for z in range(-50, 51):
                reactor[(x,y,z)] = 0

    # run the reboot steps
    for step in reboot_steps:
        (dir, (xl, xh), (yl, yh), (zl, zh)) = step
        print(f"  {step}")
        for x in range(max([xl, -50]), min([xh + 1, 51])):
            for y in range(max([yl, -50]), min([yh + 1, 51])):
                for z in range(max([zl, -50]), min([zh + 1, 51])):
                    reactor[(x,y,z)] = dir

    # count cubes that are on
    on_cubes = sum(reactor.values())
    print(f"Reactor has {on_cubes} cubes that are on")


if __name__ == '__main__':
    main()
