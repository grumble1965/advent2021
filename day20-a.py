import sys


def count_pixel(image):
    count = 0
    for row in image:
        row_count = row.count('#')
        count += row_count
    return count


def new_working_image(image, fill='.'):
    new_image = []
    empty_line = fill + fill + (fill*len(image[0])) + fill + fill
    for i in [1, 2]:
        new_image.append(empty_line)
    for row in image:
        new_image.append(fill + fill + row + fill + fill)
    for i in [1, 2]:
        new_image.append(empty_line)
    return new_image


def get_image_value(r, c, image):
    value = 0
    for dr, dc in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]:
        value *= 2
        if r+dr in range(len(image)) and c+dc in range(len(image[r+dr])) and image[r + dr][c + dc] == '#':
            value += 1
    return value


def main():
    if len(sys.argv) != 2:
        sys.exit("Please provide a file name for input data")

    image_alg = None
    input_image = []

    filename = sys.argv[1]
    with open(filename, "r") as inputfile:
        while True:
            line = inputfile.readline()
            if not line:
                break
            tmp = line.strip()
            # print(tmp)
            if image_alg is None:
                image_alg = tmp
            elif len(tmp) > 0:
                input_image.append(tmp)
            else:
                pass

    print(f"Read {len(image_alg)} characters of image enhancement algorithm")
    print("input_image:")
    for line in input_image:
        print(line)

    # enhance the input image
    fill = '.'
    working_image = new_working_image(input_image, fill)
    output_image = []
    # print(working_image)
    # print(output_image)
    for r_idx in range(1, len(working_image)-1):
        output_row = ''
        # output_row += fill
        for c_idx in range(1, len(working_image[r_idx])-1):
            image_value = get_image_value(r_idx, c_idx, working_image)
            output_row += image_alg[image_value]
        # output_row += fill
        output_image.append(output_row)
    print(f"\noutput_image has {count_pixel(output_image)} pixels lit:")
    for line in output_image:
       print(line)

    # enhance it again
    # fill = '.'
    working_image = new_working_image(output_image, fill)
    output_image = []
    # print(working_image)
    # print(output_image)
    for r_idx in range(1, len(working_image)-1):
        output_row = ''
        # output+row += '.'
        for c_idx in range(1, len(working_image[r_idx])-1):
            image_value = get_image_value(r_idx, c_idx, working_image)
            output_row += image_alg[image_value]
        # output_row += fill
        output_image.append(output_row)
    print(f"\noutput_image has {count_pixel(output_image)} pixels lit:")
    for line in output_image:
        print(line)


if __name__ == '__main__':
    main()
