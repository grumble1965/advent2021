import sys


def main():
    if len(sys.argv) != 2:
        sys.exit("Please provide a file name for input data")

    filename = sys.argv[1]
    with open(filename, "r") as inputfile:

        while True:
            line = inputfile.readline()
            if not line:
                break
            tmp = line.strip()
            # print(f"{tmp}")

            _, _, x_term, y_term = tmp.split()
            x_lefts, x_rights = x_term.replace('x=', '').replace(',', '').split('..')
            xs = [int(x_lefts), int(x_rights)]
            x_min, x_max = min(xs), max(xs)
            # print(f"{x_min}  {x_max}")
            y_highs, y_lows = y_term.replace('y=', '').split('..')
            ys = [int(y_highs), int(y_lows)]
            y_min, y_max = min(ys), max(ys)
            # print(f"{y_min}  {y_max}")

            # shoot_probe(x_max, x_min, y_max, y_min, 17, -4)
            success = []
            for vx in range(0, x_max+1):
                for vy in range(y_min-1, 200):
                    hit, steps, max_y = shoot_probe(x_max, x_min, y_max, y_min, vx, vy)
                    if hit:
                        # print("hit!")
                        tt = (vx, vy, max_y)
                        success.append(tt)
            # print(f"{success}")

            best_y = -99999
            best_vel = (None, None)
            for x, y, max_y in success:
                if max_y > best_y:
                    best_y = max_y
                    best_vel = (x, y)
            print(f"Best shot with velocity {best_vel} reached y = {best_y}")


def fire_probe(vx_0, vy_0):
    x, y = 0, 0
    vx, vy = vx_0, vy_0
    yield x, y
    while True:
        x += vx
        y += vy

        if vx > 0:
            vx -= 1
        elif vx < 0:
            vx += 1
        vy -= 1
        yield x, y


def shoot_probe(x_max, x_min, y_max, y_min, vx_0, vy_0):
    # print(f"Shoot at ({vx_0},{vy_0})", end='')
    i = 0
    max_y = -999
    hit = None
    for x, y in fire_probe(vx_0, vy_0):
        # print(f"Step {i}: {x},{y}")
        if y > max_y:
            max_y = y
        if x_min <= x <= x_max and y_min <= y <= y_max:
            # print(f"Hit target after {i} steps!")
            hit = True
            break
        if y < y_min:
            # print(f"Missed target after {i} steps")
            hit = False
            break
        i += 1
    # print(f" Hit = {hit}, Steps = {i}, Max_y = {max_y}")
    return hit, i, max_y


if __name__ == '__main__':
    main()
