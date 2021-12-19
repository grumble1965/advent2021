import sys
from adt import adt, Case


@adt
class Pair:
    INTINT: Case[int, int]
    INTPAIR: Case[int, "Pair"]
    PAIRINT: Case["Pair", int]
    PAIRPAIR: Case["Pair", "Pair"]

    @property
    def to_string(self):
        return self.match(
            intint=lambda _i, _j: f"[{_i},{_j}]",
            intpair=lambda _i, _q: f"[{_i},{_q.to_string}]",
            pairint=lambda _p, _j: f"[{_p.to_string},{_j}]",
            pairpair=lambda _p, _q: f"[{_p.to_string},{_q.to_string}]")

    @property
    def can_split(self):
        return self.match(
            intint=lambda _i, _j: _i >= 10 or _j >= 10,
            intpair=lambda _i, _q: _i >= 10 or _q.can_split,
            pairint=lambda _p, _j: _p.can_split or _j >= 10,
            pairpair=lambda _p, _q: _p.can_split or _q.can_split)

    @property
    def split(self):
        return self.match(
            intint=lambda i, j: Pair.PAIRINT(Pair.INTINT(i//2, i - i//2), j) if i >= 10 else Pair.INTPAIR(i, Pair.INTINT(j//2, j - j//2)) if j >= 10 else Pair.INTINT(i-1, j-1),
            intpair=lambda i, q: (Pair.PAIRPAIR(Pair.INTINT(i//2, i-(i//2)), q) if i >= 10 else Pair.INTPAIR(i, q.split) if q.can_split else Pair.INTPAIR(i, q)),
            pairint=lambda p, j: (Pair.PAIRINT(p.split, j) if p.can_split else Pair.PAIRPAIR(p, Pair.INTINT(j//2, j-(j//2))) if j >= 10 else Pair.PAIRINT(p, j)),
            pairpair=lambda p, q: (Pair.PAIRPAIR(p.split, q) if p.can_split else Pair.PAIRPAIR(p, q.split) if q.can_split else Pair.PAIRPAIR(p, q))
        )

    @property
    def can_explode(self):
        # string = self.to_string
        # for idx in range(len(string)):
        #     opens, closes = string[:idx].count('['), string[:idx].count(']')
        #     if opens - closes >= 5:
        #         return True
        # return False
        return self.max_depth > 4

    @property
    def max_depth(self):
        return self.match(
            intint=lambda i, j: 1,
            intpair=lambda i, q: 1 + q.max_depth,
            pairint=lambda p, j: 1 + p.max_depth,
            pairpair=lambda p, q: 1 + max([p.max_depth, q.max_depth])
        )

    @property
    def magnitude(self):
        return self.match(
            intint=lambda i, j: 3*i + 2*j,
            intpair=lambda i, q: 3*i + 2*q.magnitude,
            pairint=lambda p, j: 3*p.magnitude + 2*j,
            pairpair=lambda p, q: 3*p.magnitude + 2*q.magnitude
        )


def parse_string(string_input):
    # find comma that separates this pair
    start, good_parse = 0, None
    lhs, rhs = '', ''
    result = None
    while True:
        next_comma = string_input.find(',', start)
        if next_comma == -1:
            # print("no comma found!  Oh no!")
            good_parse = False
            break  # no commas!
        lhs, rhs = string_input[1:next_comma], string_input[next_comma + 1:-1]
        # print(f"trying {string_input} = [ {lhs} , {rhs} ]")
        if lhs.count('[') == lhs.count(']') and rhs.count('[') == rhs.count(']'):
            # print("this is the comma where both sides are balanced!")
            good_parse = True
            break
        # nope - loop for the next comma
        start = next_comma + 1
    if good_parse:
        if lhs.count(',') == 0 and rhs.count(',') == 0:
            result = Pair.INTINT(int(lhs), int(rhs))
        elif lhs.count(',') == 0:
            result = Pair.INTPAIR(int(lhs), parse_string(rhs))
        elif rhs.count(',') == 0:
            result = Pair.PAIRINT(parse_string(lhs), int(rhs))
        else:
            result = Pair.PAIRPAIR(parse_string(lhs), parse_string(rhs))
    return result


def snail_addition(pair1, pair2):
    return Pair.PAIRPAIR(pair1, pair2)


def snail_explode(pair):
    # create the string representation and parse it
    ss = pair.to_string
    left = [idx for idx in range(len(ss)) if ss[idx] == '[']
    right = [idx for idx in range(len(ss)) if ss[idx] == ']']
    comma = [idx for idx in range(len(ss)) if ss[idx] == ',']
    digits = [idx for idx in range(len(ss)) if ss[idx].isdigit()]
    numbers, current_number_idx, current_number_start = [], None, None
    for dd in digits:
        if current_number_idx is None:
            current_number_idx = dd
            current_number_start = dd
        elif dd - 1 == current_number_idx:
            current_number_idx = dd
        else:
            numbers.append(current_number_start)
            current_number_idx = dd
            current_number_start = dd
    if current_number_idx is not None:
        numbers.append(current_number_start)
    non_numbers = left + right + comma
    # print(f"{left} {right} {comma} {digits} {numbers} {non_numbers}")

    # find the explodable subpair
    explode_start, explode_end, open_count = None, None, 0
    for idx in range(len(ss)):
        if ss[idx] == '[':
            open_count += 1
        elif ss[idx] == ']':
            open_count -= 1
        if open_count == 5:
            explode_start = idx
            explode_end = [jdx for jdx in right if jdx > explode_start][0]
            break
    # print(f"{ss[0:explode_start]} *{ss[explode_start:explode_end+1]}* {ss[explode_end+1:]}")
    tmp_pair = ss[explode_start+1:explode_end].split(',')
    lnum, rnum = int(tmp_pair[0]), int(tmp_pair[1])
    print(f"left, right = {lnum}, {rnum}")

    # find idx of next number to left
    next_left_list = [jdx for jdx in numbers if jdx < explode_start]
    next_left_idx = next_left_list[-1] if next_left_list else None
    next_left = None
    if next_left_idx is not None:
        combined = [jdx for jdx in non_numbers if jdx > next_left_idx]
        next_left_len = min(combined)
        next_left = int(ss[next_left_idx:next_left_len])

    # find idx of next number to right
    next_right_list = [jdx for jdx in numbers if jdx > explode_end]
    next_right_idx = next_right_list[0] if next_right_list else None
    next_right = None
    if next_right_idx is not None:
        combined = [jdx for jdx in non_numbers if jdx > next_right_idx]
        next_right_len = min(combined)
        next_right = int(ss[next_right_idx:next_right_len])

    print(f"next left: {next_left}  next right: {next_right}")


    return pair.INTINT(-99, -99)


def snail_reduce(pair):
    while pair.can_explode or pair.can_split:
        if pair.can_explode:
            pair = snail_explode(pair)
        elif pair.can_split:
            pair = pair.split
    return pair


def main():
    if len(sys.argv) != 2:
        sys.exit("Please provide a file name for input data")

    filename = sys.argv[1]
    with open(filename, "r") as inputfile:

        snail_sum = None
        while True:
            line = inputfile.readline()
            if not line:
                break
            tmp = line.strip()
            # print(f"{tmp}")

            pair = parse_string(tmp)

            # testing magnitude
            # print(f"magnitude {pair.to_string} = {pair.magnitude}")

            # testing explode
            print(f"explode {pair.to_string} = {snail_explode(pair).to_string}")


            # if snail_sum is None:
            #     snail_sum = pair
            # else:
            #     snail_sum = snail_addition(snail_sum, pair)
            # print("snail_sum = ", snail_sum.to_string,
            #       "splittable" if snail_sum.can_split else "not splittable", ',',
            #       "explodable" if snail_sum.can_explode else "not explodable")
            #
            # foo = snail_sum
            # while foo.can_split:
            #     foo = foo.split
            #     print(foo.to_string)

        # print(snail_sum)
        # print(snail_sum.to_string)
        # foo = snail_reduce(snail_sum)
        # print(foo.to_string)


if __name__ == '__main__':
    main()
